import pytest
from time import sleep
from utilities import XLUtility
from datetime import (
    datetime,
    timedelta
)
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session note.
@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_017_SessionNotCancellable:
    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.driver.set_window_size(411, 823)
        self.logIn()

    def test_session_not_cancellable(self):
        common = CommonMethods(self.driver)
        self.log.info("starting test {}...".format(__name__))

        # get the required data
        user_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 34, 3)
        password = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 34, 4)
        service = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 34, 5)
        client_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 34, 7)

        self.login_page_obj.clk_navigation_btn()
        self.client_page_obj.clk_all_clients_mobile()
        self.client_page_obj.mobile_sel_client_name(client_name)
        self.client_page_obj.clk_view_client_mobile()
        self.notes_page_obj.clk_session_notes()

        # delete prior session notes
        common.delete_mobile_prior_session_note()

        self.notes_page_obj.clk_client_add_session()

        # set the meeting time
        current_date_time = datetime.now()
        hours_added = timedelta(hours=3)
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
        sleep(2)

        # Log in to client portal
        self.driver.get(self.client_portal_url)
        self.client_portal_page_obj.clk_mobile_menu()
        self.client_portal_page_obj.clk_sign_in_tab()
        self.client_portal_page_obj.input_username(user_name)
        self.client_portal_page_obj.input_password(password)
        self.client_portal_page_obj.clk_account_sign_in()
        sleep(1)
        self.client_portal_page_obj.clk_mobile_menu()
        self.client_portal_page_obj.clk_my_account()

        # check session booked on client portal
        self.client_portal_page_obj.clk_my_account()
        sleep(2)
        self.client_portal_page_obj.clk_cancel_session()
        message = self.client_portal_page_obj.get_message_session_cancel()
        exp_message = "This session can no longer be canceled."

        # delete the session created
        self.driver.get(self.base_url)
        self.login_page_obj.clk_navigation_btn()
        self.client_page_obj.clk_all_clients_mobile()
        self.client_page_obj.mobile_sel_client_name(client_name)
        self.client_page_obj.clk_view_client_mobile()
        self.notes_page_obj.clk_session_notes()
        sleep(1)
        self.notes_page_obj.mobile_clk_first_session_notes()
        sleep(1)
        self.notes_page_obj.clk_delete_session()
        sleep(1)
        self.notes_page_obj.clk_confirm_delete_session()

        if message == exp_message:
            self.log.info("{} passed!".format(__name__))
            assert True
        else:
            self.log.info("{} failed!".format(__name__))
            assert False
