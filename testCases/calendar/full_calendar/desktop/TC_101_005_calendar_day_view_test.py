import pytest
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# This test checks the functionality of day view of calendar
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_005_CalendarDayView:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_calendar_day_view(self):
		self.log.info("starting test {}...".format(__name__))
		self.wait = WebDriverWait(self.driver, 10)
		self.wait.until(EC.title_is("Calendar"))

		#self.client_page_obj.clk_navigate_sessions_notes()

		self.calendar_page_obj.clk_calendar_day_view()
		sleep(1)
		self.calendar_page_obj.tab_calendar_today()
		sleep(1)
		calendar_day_info = self.calendar_page_obj.desktop_calendar_day_info()

		currentDT = datetime.now()
		today_date = currentDT.date()
		today_day = today_date.day
		today_month = today_date.month
		week_day = datetime.today().weekday()
		week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		day_of_week = week_days[week_day]
		exp_date = "" + str(day_of_week) + " " + str(today_month) + "/" + str(today_day) + ''

		if calendar_day_info == exp_date:
			assert True
			self.log.info("{} passed!".format(__name__))
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_005_CalendarDayView " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
