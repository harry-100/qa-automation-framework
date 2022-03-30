import pytest
from time import sleep
from utilities import XLUtility


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_002_LoginWithWrongCredentials:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_login_with_wrong_credentials(self):

		# get the required data
		user_name = XLUtility.readData(self.path_1, 'client_portal_data', 4, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 4, 4)

		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sign_in_message = self.client_portal_page_obj.capture_sign_in_message()
		print("\nsign_in_message ", sign_in_message)
		exp_sign_in_message = (
			"Failed to fetch SignIn - The username or password was incorrect, please try again."
		)
		if sign_in_message == exp_sign_in_message:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
