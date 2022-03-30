import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.skip(reason="Not Now")
@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_006_AddCreditCardInformation:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_login_add_credit_card_information(self):
		common = CommonMethods(self.driver)

		# get all the required data
		#client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 12, 2)
		first_name = XLUtility.readData(self.path_1, 'client_portal_data', 12, 3)
		last_name = XLUtility.readData(self.path_1, 'client_portal_data', 12, 4)
		birth_date = XLUtility.readData(self.path_1, 'client_portal_data', 12, 5)
		phone_no = XLUtility.readData(self.path_1, 'client_portal_data', 12, 6)
		email_id = XLUtility.readData(self.path_1, 'client_portal_data', 12, 7)
		passwd = XLUtility.readData(self.path_1, 'client_portal_data', 12, 8)
		street_name = XLUtility.readData(self.path_1, 'client_portal_data', 12, 9)
		country = XLUtility.readData(self.path_1, 'client_portal_data', 12, 10)
		city = XLUtility.readData(self.path_1, 'client_portal_data', 12, 11)
		state = XLUtility.readData(self.path_1, 'client_portal_data', 12, 12)
		postal_code = XLUtility.readData(self.path_1, 'client_portal_data', 12, 13)
		card_number = XLUtility.readData(self.path_1, 'client_portal_data', 12, 14)
		expiration_date = XLUtility.readData(self.path_1, 'client_portal_data', 12, 15)
		cvv_number = XLUtility.readData(self.path_1, 'client_portal_data', 12, 16)

		client_name = first_name + " " + last_name

		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_create_account()
		common.create_client_portal_user(first_name, last_name, birth_date, phone_no, email_id, passwd)

		# Add Payment Method
		sleep(5)
		self.client_portal_page_obj.clk_my_account()
		self.client_portal_page_obj.clk_add_payment_card()
		self.client_portal_page_obj.input_cardholder_name(client_name)
		self.client_portal_page_obj.input_address(street_name)
		self.client_portal_page_obj.input_country(country)
		self.client_portal_page_obj.input_cty(city)
		self.client_portal_page_obj.input_state(state)
		self.client_portal_page_obj.input_postal_code(postal_code)
		self.client_portal_page_obj.input_card_number(card_number)
		self.client_portal_page_obj.input_card_expiration_date(expiration_date)
		self.client_portal_page_obj.input_cvv_number(cvv_number)
		self.client_portal_page_obj.clk_add_card()


		'''
		sleep(1)
		# delete the new account created
		self.logIn()
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.clk_all_clients_prospects()
		self.client_page_obj.sel_prospect_name_for_delete(client_name)
		self.client_page_obj.clk_delete_user()

		if sign_in_message == exp_sign_in_message:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
		'''