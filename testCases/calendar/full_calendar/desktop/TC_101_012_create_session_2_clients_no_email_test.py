import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session with two linked clients
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_012CreateSessionTwoClientsNoEmail:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_create_session_2clients_noemail(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# clear any existing session
		common.delete_existing_session()
		# Switch to clients page
		sleep(1)
		client_name_1 = XLUtility.readData(self.path, 'session_data', 24, 3)
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

		service = XLUtility.readData(self.path, 'session_data', 24, 8)
		sleep(1)
		common.create_client_session(service, date_time)
		sleep(1)
		self.client_page_obj.clk_client_session_details()
		sleep(1)

		self.client_page_obj.clk_btn_clients()
		client_name_2 = XLUtility.readData(self.path, 'session_data', 24, 15)
		self.client_page_obj.sel_client_name(client_name_2)

		self.client_page_obj.clk_client_session_details()
		sleep(2)
		session_information_1 = self.calendar_page_obj.clk_session_info()

		self.calendar_page_obj.clk_more_information()
		sleep(1)
		self.calendar_page_obj.clk_delete_session()
		sleep(1)
		self.calendar_page_obj.clk_delete_session_warn()
		sleep(1)
		try:
			self.calendar_page_obj.clk_session_delete_appointment_confirm()
		except Exception:
			self.log.info("No appontment confirmation sent")

		exp_date_time = "Thu, " + meeting_date.strftime("%b %-d") + " - 9:00am to 10:00am"
		if exp_date_time in session_information_1:

			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_012CreateSessionTwoClientsNoEmail " +
				self.dateFormat + ".png"

			)
			self.log.info("{} failed!".format(__name__))
			assert False
