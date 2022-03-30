import pytest
from time import sleep
from datetime import (
	timedelta,
	date
)
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session on client side
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_003_CreateClientSession:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_create_client_session(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# delete any existing session
		common.delete_existing_session()

		# Switch to clients page
		self.client_page_obj.clk_btn_clients()

		# Select client
		client_name = XLUtility.readData(self.path, 'session_data', 6, 3)
		sleep(1)
		self.client_page_obj.sel_client_name(client_name)

		# Click on create session
		sleep(2)
		self.client_page_obj.clk_book_session()

		# Complete the Session details form
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
		service = XLUtility.readData(self.path, 'session_data', 6, 8)
		common.create_client_session(service, date_time)
		sleep(1)
		self.login_page_obj.clk_calendar_btn()
		if current_weekday < 3 or current_weekday == 6:
			session_information = self.calendar_page_obj.clk_session_info()

		else:
			#self.calendar_page_obj.clk_move_to_next_week()
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
				pathScreenShot + "Test_TC101_003_CreateClientSession " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
