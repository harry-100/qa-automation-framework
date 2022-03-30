import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session with 3 clients and no email
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_114_CreateSession3CLientsNoEmail():

	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.logIn()

	def test_create_session_3clients_noemail(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		self.driver.set_window_size(411, 823)

		today_date = date.today()
		current_weekday = today_date.weekday()

		# delete any existing session
		common.mobile_delete_existing_session()

		# delete the sessions from client side
		client_name = XLUtility.readData(self.path, 'session_mobile_data', 28, 2)
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
		sleep(1)
		self.login_page_obj.clk_navigation_btn()
		# Start creating session
		sleep(1)
		self.login_page_obj.clk_mobile_calendar()
		sleep(1)

		# Start creating session
		self.calendar_page_obj.click_add_session()

		# Complete the Session details form
		# Select Event type

		# Select Client
		sleep(1)
		self.calendar_page_obj.input_clientname(client_name)
		sleep(1)

		# Select Date and Time
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
		service = XLUtility.readData(self.path, 'session_mobile_data', 28, 4)
		self.calendar_page_obj.sel_service(service)
		sleep(2)
		# Click on Create Session
		self.calendar_page_obj.clk_create_session()
		sleep(1)
		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		self.client_page_obj.mobile_sel_client_name(client_name)
		sleep(2)
		self.client_page_obj.clk_view_client_mobile()
		sleep(2)
		self.calendar_page_obj.clk_mobile_client_session()
		sleep(2)

		# Details of second client
		self.login_page_obj.clk_navigation_btn()
		sleep(1)
		self.client_page_obj.clk_all_clients_mobile()
		client_name_2 = XLUtility.readData(self.path, 'session_mobile_data', 28, 5)
		self.client_page_obj.mobile_sel_client_name(client_name_2)
		sleep(2)
		self.client_page_obj.clk_view_client_mobile()
		sleep(2)
		# self.calendar_page_obj.clk_mobile_client_session()
		sleep(2)
		self.calendar_page_obj.clk_mobile_client_session()

		# Details of third client
		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		client_name_3 = XLUtility.readData(self.path, 'session_mobile_data', 28, 6)
		self.client_page_obj.mobile_sel_client_name(client_name_3)
		sleep(2)
		self.client_page_obj.clk_view_client_mobile()
		sleep(2)
		# self.calendar_page_obj.clk_mobile_client_session()
		sleep(2)
		mobile_client_session_info = self.calendar_page_obj.clk_mobile_client_session()

		self.calendar_page_obj.clk_mobile_client_view_session()
		sleep(2)
		self.calendar_page_obj.clk_delete_session()
		self.calendar_page_obj.clk_delete_session_warn()
		sleep(1)
		# self.calendar_page_obj.clk_appointment_delete_confirm()
		suffix = common.get_date_suffix(meeting_date)
		exp_date_time = (
			"Thu, " + meeting_date.strftime("%b %-d") + suffix + " " + meeting_date.strftime("%Y") + " at 9:00am"
		)

		if exp_date_time in mobile_client_session_info:
					self.log.info("{} passed!".format(__name__))
					assert True
		else:
					self.driver.save_screenshot(
						self.pathScreenShot + "Test_TC101_114_CreateSession3CLientsNoEmail" +
						self.dateFormat + ".png"
					)
					self.log.info("{} failed!".format(__name__))
					assert False
