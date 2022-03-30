import pytest
from time import sleep
from utilities import XLUtility
from datetime import (
	date,
	timedelta
)
from pageObjects.common_functions.common_methods import CommonMethods

# This test checks the functionality of creating a session note.
@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_112_MobileSetServiceForAllClients:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.set_window_size(411, 823)
		self.logIn()

	def test_mobile_set_service_for_all_clients(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# get the required data
		client_portal_url = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 2)
		user_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 4)
		service_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 5)
		duration = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 6)
		service_type = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 7)
		therapist_grade = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 8)
		allowed_portal = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 9)
		video_bookable = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 10)
		service_fee = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 24, 11)

		self.login_page_obj.clk_navigation_btn()
		self.settings_page_obj.clk_mobile_service_fees()
		self.notes_page_obj.clk_mobile_add_non_session_note()

		# create service`
		service_details = {"service_name": service_name, "duration": duration,
		"service_type": service_type, "therapist_grade": therapist_grade, "service_fee": service_fee,
		"allowed_portal": allowed_portal, "video_bookable": video_bookable}
		#common.create_service(service_details)

		# Log in to client portal
		self.driver.get(client_portal_url)

		# check for new client
		self.client_portal_page_obj.clk_mobile_menu()
		self.client_portal_page_obj.clk_book_now()
		sleep(2)
		list_of_services = self.client_portal_page_obj.get_list_of_services()
		pass_counter = 0
		if service_name in list_of_services:
			pass_counter = pass_counter + 1

		self.client_portal_page_obj.clk_mobile_menu()
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)
		self.client_portal_page_obj.clk_mobile_menu()
		self.client_portal_page_obj.clk_book_now()
		list_of_services = self.client_portal_page_obj.get_list_of_services()
		if service_name in list_of_services:
			pass_counter = pass_counter + 1
		print("\npass_counter=", pass_counter)
		if pass_counter == 2:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
