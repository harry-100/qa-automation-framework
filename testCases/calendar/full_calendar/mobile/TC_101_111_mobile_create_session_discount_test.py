import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session with fee discount
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_111_CreateSessionDiscount():

	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.logIn()

	def test_create_session_discount(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		self.driver.set_window_size(411, 823)

		today_date = date.today()
		current_weekday = today_date.weekday()

		# delete any existing session
		common.mobile_delete_existing_session()

		# delete any session from client side
		client_name = XLUtility.readData(self.path, 'session_mobile_data', 22, 3)
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
		sleep(4)

		# Click on Create Session button
		self.client_page_obj.clk_client_create_session_mobile()

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
		service = XLUtility.readData(self.path, 'session_mobile_data', 22, 5)
		self.calendar_page_obj.sel_service(service)
		sleep(1)
		service_fee = self.calendar_page_obj.get_service_fee()
		sleep(0.5)
		amount = XLUtility.readData(self.path, 'session_mobile_data', 22, 7)
		self.calendar_page_obj.input_amount(amount)
		sleep(1)

		self.calendar_page_obj.clk_create_session()
		today_date = date.today()
		day = meeting_date.strftime("%-d")
		day = int(day)
		if 4 <= day <= 20 or 24 <= day <= 30:
			suffix = "th"
		else:
			suffix = ["st", "nd", "rd"][day % 10 - 1]
		date_1 = meeting_date.strftime("%a, %b %-d") + suffix + meeting_date.strftime(" %Y") + " at " + "9:00am"
		sleep(2)
		self.calendar_page_obj.sel_mobile_session(date_1)
		sleep(2)
		self.calendar_page_obj.clk_mobile_client_view_session()

		sleep(1)
		discount_percent = self.calendar_page_obj.get_discount_value()
		exp_discount = (1 - int(amount) / int(service_fee))
		exp_discount_percent = "{:.1%}".format(exp_discount)

		self.calendar_page_obj.clk_delete_session()
		sleep(0.5)
		self.calendar_page_obj.clk_delete_session_warn()
		# exp_discount_percent = XLUtility.readData(self.path, 'session_mobile_data', 22, 8)
		if discount_percent == exp_discount_percent:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_111_CreateSessionDiscount" + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
