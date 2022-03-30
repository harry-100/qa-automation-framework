import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_003_CreateAccount:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_create_account(self):
		common = CommonMethods(self.driver)

		# get all the required data
		first_name = XLUtility.readData(self.path_1, 'client_portal_data', 6, 3)
		last_name = XLUtility.readData(self.path_1, 'client_portal_data', 6, 4)
		birth_date = XLUtility.readData(self.path_1, 'client_portal_data', 6, 5)
		phone_no = XLUtility.readData(self.path_1, 'client_portal_data', 6, 6)
		email_id = XLUtility.readData(self.path_1, 'client_portal_data', 6, 7)
		passwd = XLUtility.readData(self.path_1, 'client_portal_data', 6, 8)
		client_name = first_name + " " + last_name

		# clear the previous data
		self.logIn()
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.clk_all_clients_prospects()
		try:
			self.client_page_obj.sel_prospect_name_for_delete(client_name)
			self.client_page_obj.clk_delete_user()
			self.client_portal_page_obj.clk_confirm_delete_prospect()
		except Exception:
			pass

		# create the account
		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_create_account()
		common.create_client_portal_user(first_name, last_name, birth_date, phone_no, email_id, passwd)
		sign_in_message = self.client_portal_page_obj.capture_sign_in_message()
		exp_sign_in_message = "Success! You have created your account."
		sleep(1)

		# delete the new account created
		self.driver.get(self.base_url)
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.clk_all_clients_prospects()
		self.client_page_obj.sel_prospect_name_for_delete(client_name)
		self.client_page_obj.clk_delete_user()
		self.client_portal_page_obj.clk_confirm_delete_prospect()

		if sign_in_message == exp_sign_in_message:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
