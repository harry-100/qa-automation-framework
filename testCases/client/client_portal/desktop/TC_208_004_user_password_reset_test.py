import pytest
from time import sleep
from utilities import XLUtility


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_004_UserPasswordReset:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_user_password_reset(self):

		# get all the required data
		first_name = XLUtility.readData(self.path_1, 'client_portal_data', 8, 3)
		last_name = XLUtility.readData(self.path_1, 'client_portal_data', 8, 4)
		birth_date = XLUtility.readData(self.path_1, 'client_portal_data', 8, 5)
		phone_number = XLUtility.readData(self.path_1, 'client_portal_data', 8, 6)
		email_id = XLUtility.readData(self.path_1, 'client_portal_data', 8, 7)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 8, 8)
		new_password = XLUtility.readData(self.path_1, 'client_portal_data', 8, 9)
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

		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_create_account()
		self.client_portal_page_obj.input_client_first_name(first_name)
		self.client_portal_page_obj.input_client_last_name(last_name)
		self.client_portal_page_obj.input_client_birth_date(birth_date)
		self.client_portal_page_obj.input_phone_number(phone_number)
		self.client_portal_page_obj.input_email_id(email_id)
		self.client_portal_page_obj.input_client_password(password)
		self.client_portal_page_obj.input_again_password(password)
		self.client_portal_page_obj.clk_create_new_account()
		sleep(1)
		self.driver.refresh()
		self.client_portal_page_obj.clk_my_account()
		self.client_portal_page_obj.clk_reset_password()
		self.client_portal_page_obj.input_new_password(new_password)
		self.client_portal_page_obj.input_new_password_again(new_password)
		self.client_portal_page_obj.submit_new_password()
		sleep(1)
		exp_reset_message = "Success! Your Password has been reset"
		message = self.client_portal_page_obj.capture_sign_in_message()
		password_reset_message = message.strip()
		print("\nthe message is this again 999 =", password_reset_message)

		# delete the new account created
		self.driver.get(self.base_url)
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.clk_all_clients_prospects()
		self.client_page_obj.sel_prospect_name_for_delete(client_name)
		self.client_page_obj.clk_delete_user()
		self.client_portal_page_obj.clk_confirm_delete_prospect()

		if password_reset_message == exp_reset_message:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
