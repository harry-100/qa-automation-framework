
from pageObjects.calendar.full_calendar.calender_page import CalendarPage
from pageObjects.calendar.full_calendar.client_page import ClientPage
from pageObjects.calendar.full_calendar.login_page import LoginPage
from pageObjects.client.contact_clinical.pharma_data_page import PharmaDataPage
from pageObjects.manage.forms.forms_page import FormsPage
from pageObjects.manage.forms.forms_add_form_page import AddFormsPage
from pageObjects.workflow.workflow_page import WorkFlowPage
from pageObjects.notes.notes_page import NotesPage
from pageObjects.manage.handwritten_notes_page import HandWrittenNotesPage
from pageObjects.client.finances.finances_page import FinancesPage
from pageObjects.settings.settings_page import SettingsPage
from pageObjects.client.waitlist_tags.waitlist_tags_page import WaitlistTagsPage
from pageObjects.marketing_site.marketing_page import MarketingPage
from pageObjects.marketing_site.generate_report_page import GenerateReportPage
from pageObjects.client.client_portal.client_portal_page import ClientPortalPage
#from pageObjects.client.client_lists.clients_list_page import ClientsListPage
from pageObjects.client.client_lists.clients_list_page import ClientsListPage
from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from utilities import config
from utilities.custom_logger import LogGen
from time import strftime
from datetime import date, datetime
import os
import pytest

log = LogGen.loggen()
path = "testData/test_data.xlsx"
path_1 = "testData/test_data_1.xlsx"
dateFormat = strftime("%Y-%m-%d %H:%M:%S")
pathScreenShot = "screenshots/"


def logIn(self):
    self.driver.get(self.base_url)
    self.login_page_obj.set_username(self.username)
    self.login_page_obj.set_password(self.password)
    sleep(1)
    self.login_page_obj.click_sign_in()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    dateTimeObj = datetime.now()
    timestampStr = dateTimeObj.strftime("%Y-%m-%d %H:%M:%S")
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.split("::")[-2] + timestampStr
            _capture_screenshot(file_name)
        report.extra = extra


def _capture_screenshot(name):
    file_dir = os.path.dirname(os.path.realpath('file'))
    file_name = os.path.join(file_dir + '/screenshots/')
    web_driver.get_screenshot_as_file(file_name + name + ".png")


@fixture()
def one_time_setup(request, args):
    log.info("system started")

    if request.cls is None:
        return

    global web_driver

    request.cls.log = log
    request.cls.path = path
    request.cls.path_1 = path_1
    request.cls.dateFormat = dateFormat
    request.cls.pathScreenShot = pathScreenShot

    conf = config.loadConfig()

    if args.get("browser") == "chrome":
        options = Options()
        options.binary_location = args.get("binary")
        # options.add_argument("--headless")

        request.cls.driver = webdriver.Chrome(
            options=options,
            executable_path=args.get("driver")
        )

    elif args.get("browser") == "firefox":
        request.cls.driver = webdriver.Firefox(
            executable_path=args.get("driver")
        )

    elif args.get("browser") == "safari":
        request.cls.driver = webdriver.Safari(
            #executable_path="/Applications/Safari Technology Preview.app/Contents/MacOS/safaridriver"
            executable_path="/usr/bin/safaridriver"
        )

    request.cls.base_url = conf.get("baseUrl")
    request.cls.username = conf.get("username")
    request.cls.password = conf.get("password")
    request.cls.client_portal_url = conf.get("client_portal_url")
    web_driver = request.cls.driver

    # Page Objects
    request.cls.login_page_obj = LoginPage(request.cls.driver)
    request.cls.calendar_page_obj = CalendarPage(request.cls.driver)
    request.cls.client_page_obj = ClientPage(request.cls.driver)
    request.cls.pharma_data_page_obj = PharmaDataPage(request.cls.driver)
    request.cls.manage_forms_page_obj = FormsPage(request.cls.driver)
    request.cls.manage_forms_add_form_page_obj = AddFormsPage(request.cls.driver)
    request.cls.workflow_page_obj = WorkFlowPage(request.cls.driver)
    request.cls.notes_page_obj = NotesPage(request.cls.driver)
    request.cls.handwritten_notes_page_obj = HandWrittenNotesPage(request.cls.driver)
    request.cls.finances_page_obj = FinancesPage(request.cls.driver)
    request.cls.marketingsite_page_obj = MarketingPage(request.cls.driver)
    request.cls.report_page_obj = GenerateReportPage(request.cls.driver)
    request.cls.settings_page_obj = SettingsPage(request.cls.driver)
    request.cls.waitlist_tags_page_obj = WaitlistTagsPage(request.cls.driver)
    request.cls.client_portal_page_obj = ClientPortalPage(request.cls.driver)
    request.cls.clients_list_page_obj = ClientsListPage(request.cls.driver)

    request.cls.driver.implicitly_wait(2)

    # Functions
    request.cls.logIn = logIn

    request.cls.log.info("starting tests...")

    yield request.cls.driver

    request.cls.log.info("Running one time tearDown")
    request.cls.driver.quit()
    request.cls.log.info("Closing browser...")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", help="browser")
    parser.addoption("--driver", action="store", help="driver")
    parser.addoption("--binary", action="store", help="binary")


# parser.addoption("--html", action="store", help="html")


@fixture(scope="session")
def args(request):
    return {
        "browser": request.config.getoption("browser"),
        "driver": request.config.getoption("driver"),
        "binary": request.config.getoption("binary")
    }
