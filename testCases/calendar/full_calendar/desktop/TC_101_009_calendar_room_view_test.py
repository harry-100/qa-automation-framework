import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities import XLUtility


# This test checks the functionality of Room view of the Calendar

@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_009_CalendarRoomView:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_calendar_room_view(self):
		self.log.info("starting test {}...".format(__name__))

		self.wait.until(EC.title_is("Calendar"))
		sleep(2)
		self.calendar_page_obj.clk_calendar_room_view()
		sleep(1)
		rooms = self.calendar_page_obj.desktop_calendar_room_info()
		room_name = XLUtility.readData(self.path, 'session_data', 18, 2)

		if room_name in rooms:
			assert True
			self.log.info("{} passed!".format(__name__))
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_009_CalendarRoomView " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
