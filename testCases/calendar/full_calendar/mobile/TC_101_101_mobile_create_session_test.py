import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_101_CreateSession():

	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.logIn()

	def test_create_session(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		self.driver.set_window_size(411, 823)

		today_date = date.today()
		current_weekday = today_date.weekday()

		# delete any existing session
		common.mobile_delete_existing_session()

		# delete the sessions from client side
		client_name = XLUtility.readData(self.path, 'session_mobile_data', 2, 3)
		sleep(1)
		self.login_page_obj.clk_navigation_btn()
		sleep(1)
		self.client_page_obj.clk_all_clients_mobile()
		sleep(1)
		self.client_page_obj.mobile_sel_client_name(client_name)
		sleep(1)
		self.client_page_obj.clk_view_client_mobile()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		common.delete_mobile_prior_session_note()
		sleep(2)
		self.login_page_obj.clk_navigation_btn()
		# Start creating session
		sleep(1)
		self.login_page_obj.clk_mobile_calendar()
		sleep(1)
		self.calendar_page_obj.click_add_session()
		sleep(1)
		# Complete the Session details form

		# Select Client
		sleep(1)
		self.calendar_page_obj.input_clientname(client_name)
		sleep(1)

		# Select Room
		room = XLUtility.readData(self.path, 'session_mobile_data', 2, 6)
		self.calendar_page_obj.sel_room(room)

		# Select Date and Time
		sleep(1)

		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.date_time = str(meeting_date) + " 9:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.date_time = str(meeting_date) + " 9:00am"
		self.calendar_page_obj.txt_date_time(self.date_time)
		sleep(1)

		# Select Service type (CBT, Counselling, etc.)
		service = XLUtility.readData(self.path, 'session_mobile_data', 2, 5)
		self.calendar_page_obj.sel_service(service)

		# Click on Create Session
		sleep(1)
		self.calendar_page_obj.clk_create_session()
		sleep(1)
		self.calendar_page_obj.clk_btn_calendar_view()
		sleep(1)
		self.calendar_page_obj.clk_btn_calendar_week_view()

		if current_weekday < 3 or current_weekday == 6:
			self.calendar_page_obj.clk_mobile_session_info()

		else:
			# self.calendar_page_obj.clk_move_to_next_week()
			self.calendar_page_obj.clk_mobile_session_info()
		sleep(1)
		mobile_session_details = self.calendar_page_obj.mobile_session_details()

		# View the detail of the session created
		sleep(1)
		self.calendar_page_obj.clk_mobile_more_information()
		sleep(1)
		self.calendar_page_obj.clk_delete_session()
		sleep(1)
		self.calendar_page_obj.clk_delete_session_warn()
		exp_date_time = "Thu, " + meeting_date.strftime("%b %-d") + " - 9:00am to 10:00am"

		if exp_date_time in mobile_session_details:
					self.log.info("{} passed!".format(__name__))
					assert True
		else:
					self.driver.save_screenshot(
						self.pathScreenShot + "Test_TC101_101_CreateSession" + self.dateFormat + ".png"
					)
					self.log.info("{} failed!".format(__name__))
					assert False
