import pytest
from time import sleep
from utilities import XLUtility
from datetime import (
	datetime,
	timedelta
)
from pageObjects.common_functions.common_methods import CommonMethods

# 
@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_015_MinimumCancellationTime:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_minimum_cancellation_time(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# get the required data
		client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 30, 2)
		user_name = XLUtility.readData(self.path_1, 'client_portal_data', 30, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 30, 4)
		service = XLUtility.readData(self.path_1, 'client_portal_data', 30, 5)
		client_name = XLUtility.readData(self.path_1, 'client_portal_data', 30, 7)
		min_cancellation_time = XLUtility.readData(self.path_1, 'client_portal_data', 30, 8)

		# set the minimum cancellation time
		self.login_page_obj.clk_settings_btn()
		self.settings_page_obj.clk_client_portal()
		self.settings_page_obj.input_min_cancellation_time(min_cancellation_time)
		sleep(1)
		self.settings_page_obj.clk_client_portal_settings_save()

		# set the meeting time
		current_date_time = datetime.now()
		hours_added = timedelta(hours=11)
		future_date_time = current_date_time + hours_added
		meeting_hour = future_date_time.hour
		meeting_date = future_date_time.date()
		if meeting_hour < 12:
			meeting_time = str(meeting_hour) + ":00am"
		else:
			meeting_time = str(meeting_hour - 12) + ":00pm"

		date_time = str(meeting_date) + " " + meeting_time
		print("datetime", date_time)

		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		# delete any previous session notes
		common.delete_session_notes()
		self.notes_page_obj.clk_client_add_session()

		# Complete the Session details form
		common.create_client_session(service, date_time)
		sleep(1)

		# Log in to client portal
		self.driver.get(client_portal_url)
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)

		self.client_portal_page_obj.clk_my_account()
		self.client_portal_page_obj.clk_cancel_session()
		message_cancel_session = self.client_portal_page_obj.get_message_session_cancel()
		exp_mesage = "Please note this session is considered a late cancellation, charges may apply."
		if message_cancel_session == exp_mesage:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
