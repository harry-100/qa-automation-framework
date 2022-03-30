import pytest
from datetime import (
	timedelta,
	date
)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep

# this test checks the functionality of monthly view of Calendar
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_007_CalendarMonthlyView:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_calender_month_view(self):
		self.log.info("starting test {}...".format(__name__))

		self.wait.until(EC.title_is("Calendar"))
		sleep(0.5)
		self.calendar_page_obj.clk_calendar_month_view()
		sleep(1)
		month_view_info = self.calendar_page_obj.desktop_calendar_month_info()
		today_date = date.today()
		today_day = today_date.day
		first_date = today_date - timedelta(days=today_day - 1)
		first_date_weekday = first_date.weekday()
		if first_date_weekday == 6:
			N = 0
		else:
			N = first_date_weekday + 1

		start_date = first_date - timedelta(days=N)
		end_date = start_date + timedelta(days=41)
		start_date_format = start_date.strftime("%b %-d")
		start_year = start_date.strftime("%Y")
		end_date_format = end_date.strftime("%b %-d")
		end_year = end_date.strftime("%Y")
		exp_date_format = (
			start_date_format + ", " + start_year + " - " + end_date_format + ", " + end_year
		)
		if start_year == end_year:
			exp_date_format = start_date_format + " - " + end_date_format + ", " + end_year
		else:
			exp_date_format = (
				start_date_format + ", " + start_year + " - " + end_date_format + ", " + end_year
			)
		if exp_date_format == month_view_info:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_007_CalendarMonthlyView " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
