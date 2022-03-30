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
class Test_TC101_001_CreateSession:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_create_session(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# clear any existing session
		sleep(2)
		common.delete_existing_session()

		# clear any session from client side
		client_name = XLUtility.readData(self.path, 'session_data', 2, 3)
		self.client_page_obj.clk_btn_clients()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()

		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		# delete any previous session notes
		common.delete_session_notes()

		# Start creating session
		sleep(1)
		self.login_page_obj.clk_calendar_btn()
		sleep(1)
		self.calendar_page_obj.click_add_session()

		# Complete the Session details form
		sleep(1)
		self.calendar_page_obj.input_clientname(client_name)
		sleep(1)
		today_date = date.today()
		current_weekday = today_date.weekday()
		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.date_time = str(meeting_date) + " 9:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.date_time = str(meeting_date) + " 9:00am"
		sleep(1)
		self.calendar_page_obj.txt_date_time(self.date_time)
		sleep(1)
		service = XLUtility.readData(self.path, 'session_data', 2, 8)
		self.calendar_page_obj.sel_service(service)
		sleep(2)

		room = XLUtility.readData(self.path, 'session_data', 2, 9)
		self.calendar_page_obj.sel_room(room)
		sleep(1)
		self.calendar_page_obj.clk_create_session()
		sleep(1)
		self.client_page_obj.clk_btn_clients()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		day = meeting_date.strftime("%-d")
		day = int(day)
		if 4 <= day <= 20 or 24 <= day <= 30:
			suffix = "th"
		else:
			suffix = ["st", "nd", "rd"][day % 10 - 1]
		date_1 = (meeting_date.strftime("%a, %b %-d") + suffix + today_date.strftime(" %Y") + " at " + "9:00am")

		self.notes_page_obj.sel_session_notes_by_date(date_1)

		session_information = self.calendar_page_obj.clk_session_info()
		self.calendar_page_obj.clk_more_information()
		self.calendar_page_obj.clk_delete_session()
		self.calendar_page_obj.clk_delete_session_warn()
		exp_date_time = "Thu, " + meeting_date.strftime("%b %-d") + " - 9:00am to 10:00am"

		if exp_date_time in session_information:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			pathScreenShot = "screenshots/"
			self.driver.save_screenshot(
				pathScreenShot + "Test_TC101_001_CreateSession " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
