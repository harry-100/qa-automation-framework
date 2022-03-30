import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities import XLUtility


# This test checks the functionality of therapist view of the Calendar

@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_010_CalendarTherapistView:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()
		self.wait = WebDriverWait(self.driver, 10)

	def test_calendar_therapist_view(self):
		self.log.info("starting test {}...".format(__name__))

		self.wait.until(EC.title_is("Calendar"))

		self.calendar_page_obj.clk_therapist_availability_view()
		sleep(1)
		therapist_name_list = self.calendar_page_obj.desktop_therapist_view_info()
		therapist_name = XLUtility.readData(self.path, 'session_data', 20, 4)
		if therapist_name in therapist_name_list:
			assert True
			self.log.info("{} passed!".format(__name__))
		else:
			self.driver.save_screenshot(
				self.pathScreenShot + "Test_TC101_010_CalendarTherapistView " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
