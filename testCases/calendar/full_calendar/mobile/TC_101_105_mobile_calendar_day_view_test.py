import pytest
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


# This test checks the functionality of day view of calendar
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_105_CalendarDayView():
	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.driver.set_window_size(411, 823)
		self.logIn()

	def test_calendar_day_view(self):
		self.log.info("starting test {}...".format(__name__))

		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.title_is("Calendar"))
		self.calendar_page_obj.clk_btn_calendar_view()
		sleep(1)
		self.calendar_page_obj.clk_mobile_calendar_day_view()
		sleep(0.5)
		self.calendar_page_obj.clk_btn_calendar_view()
		sleep(0.5)
		self.calendar_page_obj.clk_mobile_jump_to_today()
		sleep(1)
		day_text = self.calendar_page_obj.mobile_calendar_day_info()
		print("day text ", day_text)

		currentDT = datetime.now()
		today_date = currentDT.date()
		today_day = today_date.day
		week_day = datetime.today().weekday()
		week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
		day_of_week = week_days[week_day]
		print("driver name ", self.driver.name)
		if self.driver.name == "chrome":
			exp_date = "" + str(day_of_week) + "\n" + str(today_day) + ''
			print("this is Chrome or Firefox")

		elif self.driver.name == "firefox":
			exp_date = "" + str(day_of_week) + "\n" + str(today_day) + ''
			print("exp date ", exp_date)

		elif self.driver.name == "Safari" or "Safari Technology Preview":
			exp_date = "" + str(day_of_week) + "  " + str(today_day) + ''
			print("this is Safari")


		if day_text in exp_date:
			assert True
			self.log.info("{} passed!".format(__name__))
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_105_CalendarDayView " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
