import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC209_102_MobileCreatePublicList:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.set_window_size(411, 823)
		self.logIn()

	def test_mobile_create_public_client_list(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		client_name = []
		# get the required data
		list_name = XLUtility.readData(self.path_1, 'clients_list_mobile_data', 4, 2)
		tag_name = XLUtility.readData(self.path_1, 'clients_list_mobile_data', 4, 3)
		client_name.append(XLUtility.readData(self.path_1, 'clients_list_mobile_data', 4, 4))
		client_name.append(XLUtility.readData(self.path_1, 'clients_list_mobile_data', 4, 5))

		# Add tags
		self.login_page_obj.clk_navigation_btn()
		self.login_page_obj.clk_mobile_settings_practice_details()
		self.waitlist_tags_page_obj.clk_settings_tags()
		self.waitlist_tags_page_obj.input_settings_tag_title(tag_name)
		self.waitlist_tags_page_obj.clk_settings_add_tag()

		for i in range(2):
			self.login_page_obj.clk_navigation_btn()
			self.client_page_obj.clk_all_clients_mobile()
			self.client_page_obj. mobile_sel_client_name(client_name[i])
			self.client_page_obj.clk_view_client_mobile()
			sleep(2)
			self.client_page_obj.clk_mobile_open_client_menu()
			sleep(1)
			#self.driver.refresh()

			#self.waitlist_tags_page_obj.clk_client_add_tags()
			self.waitlist_tags_page_obj.sel_mobile_client_tag(tag_name)
			sleep(2)
			self.waitlist_tags_page_obj.clk_mobile_client_profile_close()
			#self.driver.refresh()

		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		self.client_page_obj.clk_mobile_open_client_menu()

		# Create a Client List
		self.clients_list_page_obj.clk_add_custom_list()
		self.clients_list_page_obj.input_list_name(list_name)
		self.clients_list_page_obj.input_tag_name(tag_name)
		self.clients_list_page_obj.clk_table_columns()
		self.clients_list_page_obj.clk_column_first_name()
		self.clients_list_page_obj.clk_column_last_name()
		self.clients_list_page_obj.clk_column_city()
		self.clients_list_page_obj.clk_sharing()
		self.clients_list_page_obj.clk_office_admins()
		self.clients_list_page_obj.clk_add_client_list()
		sleep(2)
		clients_list = self.clients_list_page_obj.get_clients_public_list()
		print("client lists ", clients_list)

		# delete the list created
		no_of_lists = self.clients_list_page_obj.get_no_of_mobile_shared_client_list()
		for i in range(no_of_lists):
			self.clients_list_page_obj.clk_mobile_shared_client_list()
			sleep(1)
			self.clients_list_page_obj.clk_mobile_delete_client_list()
			self.clients_list_page_obj.clk_mobile_confirm_delete_client_list()

		# delete the tag created
		self.login_page_obj.clk_navigation_btn()
		self.login_page_obj.clk_mobile_settings_practice_details()
		self.waitlist_tags_page_obj.clk_settings_tags()

		# delete any existing tags in settings
		common.delete_settings_tags()

		if list_name in clients_list:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
