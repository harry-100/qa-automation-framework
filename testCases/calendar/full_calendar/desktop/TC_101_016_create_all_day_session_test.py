import pytest
from time import sleep
from datetime import date
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a all day session
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_016_CreateAllDaySession:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_create_all_day_session(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		today_date = date.today()
		current_weekday = today_date.weekday()

		# delete any existing session
		self.calendar_page_obj.clk_calendar_day_view()
		sleep(1)
		self.calendar_page_obj.tab_calendar_today()
		sleep(1)
		no_of_personal_sessions = self.calendar_page_obj.get_no_personal_sessions()
		try:
			for i in range(no_of_personal_sessions):
				common.delete_all_day_session()
		except Exception:
			self.log.info("No prior personal sessions found")

		self.calendar_page_obj.clk_all_day_session_slot()
		sleep(1)
		# Complete the Session details form
		try:
			self.calendar_page_obj.clk_create_all_day_session()
		except Exception:
			self.log.info("Create session button not found")

		event_name = XLUtility.readData(self.path, 'session_data', 32, 3)
		self.calendar_page_obj.input_event_name(event_name)

		self.calendar_page_obj.clk_create_session()

		self.calendar_page_obj.clk_all_day_session_info()
		personal_session_info = self.calendar_page_obj.tab_personal_session_info()

		self.calendar_page_obj.clk_personal_session_more_information()
		self.calendar_page_obj.clk_delete_session()
		self.calendar_page_obj.clk_delete_session_warn()

		exp_session_info = "Research — All Office"
		if exp_session_info in personal_session_info:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
