import pytest
from time import sleep
from utilities import XLUtility
from datetime import (
    datetime,
    timedelta
)
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_018_SessionBookedDifferentTimezone:
    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.driver.maximize_window()
        self.logIn()

    def test_session_booked_different_timezone(self):
        common = CommonMethods(self.driver)
        self.log.info("starting test {}...".format(__name__))

        # get the required data
        client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 36, 2)
        user_name = XLUtility.readData(self.path_1, 'client_portal_data', 36, 3)
        password = XLUtility.readData(self.path_1, 'client_portal_data', 36, 4)
        service = XLUtility.readData(self.path_1, 'client_portal_data', 36, 5)
        # time_zone = XLUtility.readData(self.path_1, 'client_portal_data', 36, 6)
        client_name = XLUtility.readData(self.path_1, 'client_portal_data', 36, 7)

        # Change clinic time zone
        self.login_page_obj.clk_settings_btn()
        self.settings_page_obj.clk_practice_details()
        self.settings_page_obj.clk_settings_basics()
        # self.settings_page_obj.input_time_zone(time_zone)
        self.settings_page_obj.clk_settings_save()

        self.login_page_obj.clk_clients_btn()
        self.client_page_obj.sel_client_name(client_name)
        self.client_page_obj.clk_navigate_sessions_notes()
        sleep(1)
        self.notes_page_obj.clk_session_notes()
        sleep(1)
        # delete any previous session notes
        common.delete_session_notes()
        self.notes_page_obj.clk_client_add_session()
        # set the meeting time
        current_date_time = datetime.now()
        hours_added = timedelta(hours=0)
        meeting_date_time = current_date_time - hours_added
        meeting_hour = meeting_date_time.hour
        meeting_date = meeting_date_time.date()
        if meeting_hour < 12:
            meeting_time = str(meeting_hour) + ":00am"
        else:
            meeting_time = str(meeting_hour - 12) + ":00pm"

        date_time = str(meeting_date) + " " + meeting_time
        print("datetime", date_time)

        # Complete the Session details form
        sleep(1)

        self.calendar_page_obj.txt_date_time(date_time)
        sleep(2)
        self.calendar_page_obj.sel_service(service)
        sleep(2)
        self.calendar_page_obj.clk_video_session()
        sleep(1)
        self.calendar_page_obj.clk_create_session()
        sleep(3)

        # Log in to client portal
        self.driver.get(client_portal_url)
        self.client_portal_page_obj.clk_sign_in_tab()
        self.client_portal_page_obj.input_username(user_name)
        self.client_portal_page_obj.input_password(password)
        self.client_portal_page_obj.clk_account_sign_in()
        sleep(1)

        # check session booked on client portal
        self.client_portal_page_obj.clk_my_account()
        sleep(1)
        self.client_portal_page_obj.clk_join_session()
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
