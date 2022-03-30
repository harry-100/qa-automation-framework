import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_103_MobileCreateAccount:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.set_window_size(411, 823)

	def test_mobile_create_account(self):
		common = CommonMethods(self.driver)

		# get all the required data
		client_portal_url = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 2)
		first_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 3)
		last_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 4)
		birth_date = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 5)
		phone_no = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 6)
		email_id = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 7)
		passwd = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 6, 8)
		client_name = first_name + " " + last_name

		self.driver.get(client_portal_url)
		self.client_portal_page_obj.clk_mobile_menu()
		self.client_portal_page_obj.clk_create_account()
		common.create_client_portal_user(first_name, last_name, birth_date, phone_no, email_id, passwd)
		sign_in_message = self.client_portal_page_obj.capture_sign_in_message()

		exp_sign_in_message = "Success! You have created your account."
		sleep(1)

		# delete the new account created
		self.logIn()
		self.login_page_obj.clk_navigation_btn()
		self.login_page_obj.clk_mobile_client_prospects()

		self.client_page_obj.mobile_sel_prospect_name(client_name)
		self.client_page_obj.clk_delete_user()

		if sign_in_message == exp_sign_in_message:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
