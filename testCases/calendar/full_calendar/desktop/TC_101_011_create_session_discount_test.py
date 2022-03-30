import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of checking discount on fee

@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_011CreateSessionDiscount:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_create_session_discount(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# clear any existing session
		common.delete_existing_session()

		# clear any session from client side
		client_name = XLUtility.readData(self.path, 'session_data', 22, 3)
		sleep(1)
		self.client_page_obj.clk_btn_clients()
		sleep(1)
		self.client_page_obj.sel_client_name(client_name)
		sleep(1)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		# delete any previous session notes
		common.delete_session_notes()
		sleep(1)
		# Start creating session
		self.notes_page_obj.clk_client_add_session()

		# Complete the Session details form
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
		service = XLUtility.readData(self.path, 'session_data', 22, 8)
		sleep(1)
		self.calendar_page_obj.sel_service(service)
		sleep(2)
		service_fee = self.calendar_page_obj.get_service_fee()

		amount = XLUtility.readData(self.path, 'session_data', 22, 10)
		exp_discount = (1 - int(amount) / int(service_fee))
		exp_discount_percent = "{:.1%}".format(exp_discount)

		self.calendar_page_obj.input_amount(amount)

		self.calendar_page_obj.clk_create_session()
		sleep(1)
		day = meeting_date.strftime("%-d")
		day = int(day)
		if 4 <= day <= 20 or 24 <= day <= 30:
			suffix = "th"
		else:
			suffix = ["st", "nd", "rd"][day % 10 - 1]
		date_1 = (meeting_date.strftime("%a, %b %-d") + suffix + today_date.strftime(" %Y") + " at " + "9:00am")

		self.notes_page_obj.sel_session_notes(date_1)
		sleep(1)
		self.notes_page_obj.clk_view_client_session()

		sleep(2)
		act_discount_percent = self.calendar_page_obj.get_discount_value()
		sleep(1)
		self.calendar_page_obj.clk_delete_session()
		self.calendar_page_obj.clk_delete_session_warn()

		if act_discount_percent == str(exp_discount_percent):
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_011CreateSessionDiscount" + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
