import pytest
from time import sleep
from utilities import XLUtility
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC209_001_CreatePrivateClientList:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_create_private_client_list(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		client_name = []
		# data required
		list_name = XLUtility.readData(self.path_1, 'clients_list_data', 2, 2)
		tag_name = XLUtility.readData(self.path_1, 'clients_list_data', 2, 3)
		client_name.append(XLUtility.readData(self.path_1, 'clients_list_data', 2, 4))
		client_name.append(XLUtility.readData(self.path_1, 'clients_list_data', 2, 5))

		# Add tag
		self.login_page_obj.clk_settings_btn()
		self.settings_page_obj.clk_practice_details()
		self.waitlist_tags_page_obj.clk_settings_tags()
		self.waitlist_tags_page_obj.input_settings_tag_title(tag_name)
		self.waitlist_tags_page_obj.clk_settings_add_tag()
		for i in range(2):
			self.login_page_obj.clk_clients_btn()
			self.client_page_obj.clk_btn_clients()
			self.client_page_obj.sel_client_name(client_name[i])
			self.waitlist_tags_page_obj.clk_client_add_tags()
			self.waitlist_tags_page_obj.sel_client_tag(tag_name)
			sleep(1)
			self.waitlist_tags_page_obj.clk_client_add_tags()
			sleep(1)
		self.login_page_obj.clk_clients_btn()

		# Create a Client List
		self.clients_list_page_obj.clk_add_custom_list()
		self.clients_list_page_obj.input_list_name(list_name)
		self.clients_list_page_obj.input_tag_name(tag_name)
		self.clients_list_page_obj.clk_table_columns()
		self.clients_list_page_obj.clk_column_first_name()
		self.clients_list_page_obj.clk_column_last_name()
		self.clients_list_page_obj.clk_column_city()
		self.clients_list_page_obj.clk_add_client_list()
		sleep(2)
		clients_list = self.clients_list_page_obj.get_clients_private_list()

		# delete the list created
		sleep(3)
		self.clients_list_page_obj.clk_delete_client_list()
		self.clients_list_page_obj.clk_delete_confirm_client_list()

		# delete the tag created
		self.login_page_obj.clk_settings_btn()
		self.settings_page_obj.clk_practice_details()
		self.waitlist_tags_page_obj.clk_settings_tags()
		# delete any existing tags in settings
		common.delete_settings_tags()

		if list_name in clients_list:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
