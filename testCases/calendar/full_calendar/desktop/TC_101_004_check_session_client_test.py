import pytest
from time import (
	sleep,
)
from datetime import (
	timedelta,
	date
)
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session and checking on a client side
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_004_CheckSessionClient:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_check_session_client(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# clear any exising session
		common.delete_existing_session()

		# Start creating session
		self.calendar_page_obj.click_add_session()

		# Complete the Session details form
		self.client_name = XLUtility.readData(self.path, 'session_data', 8, 3)
		sleep(1)
		self.calendar_page_obj.input_clientname(self.client_name)

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
		self.calendar_page_obj.txt_date_time(self.date_time)
		sleep(1)
		service = XLUtility.readData(self.path, 'session_data', 8, 8)
		self.calendar_page_obj.sel_service(service)
		sleep(1)

		self.calendar_page_obj.clk_create_session()
		sleep(1)
		self.client_page_obj.clk_btn_clients()
		sleep(1)
		self.client_page_obj.sel_client_name(self.client_name)
		sleep(1)
		self.client_page_obj.clk_client_session_details()
		sleep(1)
		session_information = self.calendar_page_obj.clk_session_info()
		sleep(1)
		self.calendar_page_obj.clk_more_information()
		sleep(1)
		self.calendar_page_obj.clk_delete_session()
		sleep(1)
		self.calendar_page_obj.clk_delete_session_warn()
		exp_date_time = "Thu, " + meeting_date.strftime("%b %-d") + " - 9:00am to 10:00am"
		if exp_date_time in session_information:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			pathScreenShot = "screenshots/"
			self.driver.save_screenshot(
				pathScreenShot + "Test_TC101_004_CheckSessionClient " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
