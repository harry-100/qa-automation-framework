import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session for 3 linked clients with no email
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_014CreateSessionThreeClientsNoEmail:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_create_session_3clients_noemail(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# clear any existing session
		common.delete_existing_session()
		client_name_1 = XLUtility.readData(self.path, 'session_data', 28, 2)
		# Start creating session
		# Switch to clients page
		sleep(1)
		self.client_page_obj.clk_btn_clients()
		sleep(1)
		self.client_page_obj.sel_client_name(client_name_1)
		# Start creating session
		sleep(2)
		self.client_page_obj.clk_book_session()
		sleep(1)

		today_date = date.today()
		current_weekday = today_date.weekday()

		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			date_time = str(meeting_date) + " 9:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			date_time = str(meeting_date) + " 9:00am"

		service = XLUtility.readData(self.path, 'session_data', 28, 4)
		common.create_client_session(service, date_time)
		sleep(1)
		self.client_page_obj.clk_client_session_details()
		sleep(2)

		self.client_page_obj.clk_btn_clients()
		client_name_2 = XLUtility.readData(self.path, 'session_data', 28, 5)
		self.client_page_obj.sel_client_name(client_name_2)

		self.client_page_obj.clk_client_session_details()
		sleep(2)

		self.client_page_obj.clk_btn_clients()
		client_name_3 = XLUtility.readData(self.path, 'session_data', 28, 6)
		self.client_page_obj.sel_client_name(client_name_3)

		self.client_page_obj.clk_client_session_details()

		session_information_1 = self.calendar_page_obj.clk_session_info()
		sleep(1)
		self.calendar_page_obj.clk_more_information()
		sleep(1)
		self.calendar_page_obj.clk_delete_session()
		sleep(1)
		self.calendar_page_obj.clk_delete_session_warn()

		exp_date_time = "Thu, " + meeting_date.strftime("%b %-d") + " - 9:00am to 10:00am"
		if exp_date_time in session_information_1:

			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_014CreateSessionThreeClientsNoEmail " +
				self.dateFormat + ".png"

			)
			self.log.info("{} failed!".format(__name__))
			assert False
