import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session note.
@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_013_SetServiceForExistingClients:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_set_service_for_existing_clients(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# get the required data
		client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 26, 2)
		user_name = XLUtility.readData(self.path_1, 'client_portal_data', 26, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 26, 4)
		service_name = XLUtility.readData(self.path_1, 'client_portal_data', 26, 5)
		duration = XLUtility.readData(self.path_1, 'client_portal_data', 26, 6)
		service_type = XLUtility.readData(self.path_1, 'client_portal_data', 26, 7)
		therapist_grade = XLUtility.readData(self.path_1, 'client_portal_data', 26, 8)
		allowed_portal = XLUtility.readData(self.path_1, 'client_portal_data', 26, 9)
		video_bookable = XLUtility.readData(self.path_1, 'client_portal_data', 26, 10)
		service_fee = XLUtility.readData(self.path_1, 'client_portal_data', 26, 11)

		self.login_page_obj.clk_settings_btn()
		self.settings_page_obj.clk_services_and_fee()
		self.finances_page_obj.clk_btn_add_item()

		# create service`
		service_details = {"service_name": service_name, "duration": duration, "service_type": service_type, "therapist_grade": therapist_grade, "service_fee": service_fee, "allowed_portal": allowed_portal, "video_bookable": video_bookable}
		common.create_service(service_details)

		# Log in to client portal
		self.driver.get(client_portal_url)

		# check for new client
		self.client_portal_page_obj.clk_book_now()
		sleep(5)
		list_of_services = self.client_portal_page_obj.get_list_of_services()

		pass_counter = 0
		if service_name not in list_of_services:
			pass_counter = pass_counter + 1

		# log in with existing client credentails
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)
		self.client_portal_page_obj.clk_book_now()
		sleep(6)
		list_of_services = self.client_portal_page_obj.get_list_of_services()
		if service_name in list_of_services:
			pass_counter = pass_counter + 1

		if pass_counter == 2:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False


