import pytest
from time import sleep
from utilities import XLUtility
from datetime import (
    date,
    timedelta
)
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_010_CreateSessionClinicPortalShowsClientPortal:
    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.driver.maximize_window()
        self.logIn()

    def test_create_session_clinic_portal_shows_client_portal(self):
        common = CommonMethods(self.driver)
        self.log.info("starting test {}...".format(__name__))

        # get the required data
        user_name = XLUtility.readData(self.path_1, 'client_portal_data', 32, 3)
        password = XLUtility.readData(self.path_1, 'client_portal_data', 32, 4)
        service = XLUtility.readData(self.path_1, 'client_portal_data', 32, 5)
        session_time = XLUtility.readData(self.path_1, 'client_portal_data', 32, 6)
        client_name = XLUtility.readData(self.path_1, 'client_portal_data', 32, 7)

        self.login_page_obj.clk_clients_btn()
        sleep(1)
        self.client_page_obj.sel_client_name(client_name)
        self.client_page_obj.clk_navigate_sessions_notes()
        sleep(1)
        self.notes_page_obj.clk_session_notes()
        sleep(1)
        # delete any previous session notes
        common.delete_session_notes()
        self.notes_page_obj.clk_client_add_session()
        today_date = date.today()
        meeting_date = today_date + timedelta(days=1)
        date_time = str(meeting_date) + " " + session_time

        # Complete the Session details form
        sleep(1)
        self.calendar_page_obj.txt_date_time(date_time)
        sleep(2)
        self.calendar_page_obj.sel_service(service)
        sleep(2)
        self.calendar_page_obj.clk_video_session()
        sleep(1)
        self.calendar_page_obj.clk_create_session()
        sleep(2)

        # Log in to client portal
        self.driver.get(self.client_portal_url)
        self.client_portal_page_obj.clk_sign_in_tab()
        self.client_portal_page_obj.input_username(user_name)
        self.client_portal_page_obj.input_password(password)
        self.client_portal_page_obj.clk_account_sign_in()
        sleep(1)

        # check session booked on client portal
        self.client_portal_page_obj.clk_my_account()
        sleep(1)
        message = self.client_portal_page_obj.get_warning_message()
        exp_message = (
            "The Video Session link is active 30 minutes before the session start time until"
            " 30 minutes after the session end time"
        )

        # delete the session created
        self.driver.get(self.base_url)
        self.login_page_obj.clk_clients_btn()
        self.client_page_obj.sel_client_name(client_name)
        self.client_page_obj.clk_navigate_sessions_notes()
        sleep(1)
        common.delete_session_notes()

        if message == exp_message:
            self.log.info("{} passed!".format(__name__))
            assert True
        else:
            self.log.info("{} failed!".format(__name__))
            assert False
