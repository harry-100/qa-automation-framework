import pytest
from datetime import (
	timedelta,
	date
)
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# This test checks the functionality of checking  weekly view of calendar
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_106_CalendarWeekView():

	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.logIn()
		self.driver.set_window_size(411, 823)
		self.wait = WebDriverWait(self.driver, 10)

	def test_calendar_week_view(self):
		self.log.info("starting test {}...".format(__name__))

		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.title_is("Calendar"))
		self.calendar_page_obj.clk_btn_calendar_view()
		sleep(1)
		self.calendar_page_obj.clk_btn_calendar_week_view()

		today_date = date.today()
		current_weekday = today_date.weekday()

		if current_weekday >= 0 and current_weekday <= 5:
			N = current_weekday + 1
			start_week_date = today_date - timedelta(days=N)
		else:
			start_week_date = today_date

		end_week_date = start_week_date + timedelta(days=6)

		act_date_info = self.calendar_page_obj.text_mobile_date_info()

		start_date_format = start_week_date.strftime("%b %-d")
		end_date_format2 = end_week_date.strftime("%b %-d")
		end_date_format1 = end_week_date.strftime("%-d")
		end_year = end_week_date.strftime("%Y")
		start_year = start_week_date.strftime("%Y")
		exp_date_format1 = start_date_format + " - " + end_date_format1 + ", " + end_year
		exp_date_format2 = start_date_format + " - " + end_date_format2 + ", " + end_year
		exp_date_format3 = (
			start_date_format + "," + start_year + " - " + end_date_format1 + ", " + end_year
		)
		if start_week_date.year == end_week_date.year:

			if start_week_date.month == end_week_date.month:
				exp_date_format = exp_date_format1
			else:
				exp_date_format = exp_date_format2

		else:

				exp_date_format = exp_date_format3

		if exp_date_format == act_date_info:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_106_CalendarWeekView" + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
