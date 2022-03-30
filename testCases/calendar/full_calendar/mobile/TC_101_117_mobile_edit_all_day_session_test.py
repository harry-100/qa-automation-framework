import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of editing an all day session
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_117_EditAllDaySession():

	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.logIn()

	def test_edit_all_day_session(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		self.driver.set_window_size(411, 823)

		today_date = date.today()
		current_weekday = today_date.weekday()

		# delete any existing session
		common.mobile_delete_all_day_session()

		# Start creating session
		sleep(1)
		self.calendar_page_obj.click_add_session()

		# Complete the Session details form
		event_type = XLUtility.readData(self.path, 'session_mobile_data', 34, 2)
		sleep(1)
		self.calendar_page_obj.sel_event_type(event_type)
		sleep(1)
		event_name = XLUtility.readData(self.path, 'session_mobile_data', 34, 3)
		self.calendar_page_obj.input_event_name(event_name)
		sleep(1)

		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.start_date = str(meeting_date) + " 9:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.start_date = str(meeting_date) + " 9:00am"

		self.calendar_page_obj.txt_start_date(self.start_date)

		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.end_date = str(meeting_date) + " 10:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.end_date = str(meeting_date) + " 10:00am"

		self.calendar_page_obj.txt_end_date(self.end_date)
		sleep(1)
		self.calendar_page_obj.check_all_day_session()
		sleep(2)
		self.calendar_page_obj.clk_create_session()
		sleep(1)
		self.calendar_page_obj.clk_btn_calendar_view()
		sleep(0.5)
		self.calendar_page_obj.clk_btn_calendar_week_view()
		sleep(0.5)
		self.calendar_page_obj.clk_all_day_session()
		sleep(0.5)
		self.calendar_page_obj.clk_mobile_personal_session_more_information()
		sleep(1)
		self.calendar_page_obj.check_all_day_session()
		new_meeting_date = meeting_date + timedelta(days=7)
		self.new_start_date = str(new_meeting_date) + " 9:00am"
		self.calendar_page_obj.txt_start_date(self.new_start_date)
		self.new_end_date = str(new_meeting_date) + " 10:00am"
		self.calendar_page_obj.txt_end_date(self.new_end_date)
		sleep(1)
		self.calendar_page_obj.check_all_day_session()
		sleep(1)
		self.calendar_page_obj.clk_update_session()
		sleep(2)
		self.calendar_page_obj.clk_move_to_next_week()
		sleep(0.5)
		self.calendar_page_obj.clk_all_day_session()
		sleep(1)
		mobile_personal_session_info = self.calendar_page_obj.tab_mobile_personal_session_details()
		self.calendar_page_obj.clk_mobile_personal_session_more_information()
		sleep(0.5)
		self.calendar_page_obj.clk_delete_session()
		sleep(0.5)
		self.calendar_page_obj.clk_delete_session_warn()

		exp_session_info = "Research All Office"
		if exp_session_info in mobile_personal_session_info:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			pathScreenShot = "screenshots/"
			self.driver.save_screenshot(
				pathScreenShot + "Test_TC101_117_EditAllDaySession " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
