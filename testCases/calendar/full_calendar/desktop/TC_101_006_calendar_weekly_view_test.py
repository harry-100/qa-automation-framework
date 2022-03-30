import pytest
from datetime import (
	datetime,
	timedelta
)
from pytest import fixture
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# This test checks the functionality of weekly view of calendar
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_006_CalendarWeekView:

	@fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_calendar_week_view(self):
		self.log.info("starting test {}...".format(__name__))

		self.wait.until(EC.title_is("Calendar"))
		self.calendar_page_obj.clk_calendar_week_view()
		days = self.calendar_page_obj.desktop_calendar_week_info()

		currentDT = datetime.now()
		today_date = currentDT.date()
		week_day = datetime.today().weekday()

		if week_day >= 0 and week_day <= 5:
			N = week_day + 1
			start_date = today_date - timedelta(days=N)
		else:
			start_date = today_date

		start_day = start_date.day
		start_month = start_date.month
		exp_start_date = "Sun " + str(start_month) + "/" + str(start_day) + ""
		third_date = start_date + timedelta(days=2)
		third_day = third_date.day
		third_month = third_date.month
		exp_third_date = "Tue " + str(third_month) + "/" + str(third_day) + ""
		if (exp_start_date in days[0]) and (exp_third_date in days[2]):
			assert True
			self.log.info("{} passed!".format(__name__))

		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_006_CalendarWeekView " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
