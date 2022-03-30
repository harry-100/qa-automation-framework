import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_008_BookSessionClientPortal:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_book_session_client_portal(self):
		common = CommonMethods(self.driver)

		# get the required data
		#client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 16, 2)
		user_name = XLUtility.readData(self.path_1, 'client_portal_data', 16, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 16, 4)
		service = XLUtility.readData(self.path_1, 'client_portal_data', 16, 5)
		meeting_time = XLUtility.readData(self.path_1, 'client_portal_data', 16, 6)
		client_name = XLUtility.readData(self.path_1, 'client_portal_data', 16, 7)

		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)
		'''
		self.client_portal_page_obj.clk_book_now()
		sleep(1)
		self.client_portal_page_obj.select_service(service)
		sleep(1)

		no_slots_available = self.client_portal_page_obj.check_availability_of_slots()
		if no_slots_available is True:
			self.client_portal_page_obj.clk_jump_to_next_slot()
		sleep(1)
		self.client_portal_page_obj.clk_time_slot(meeting_time)
		sleep(1)

		self.client_portal_page_obj.clk_book_meeting()
		self.client_portal_page_obj.clk_confirm_booking()
		'''
		self.client_portal_page_obj.clk_my_account()
		sleep(1)
		exp_meeting_time = meeting_time.replace(" ", "")
		exp_meeting_time = exp_meeting_time.replace(".", "")
		#print("exp_meeting_time=", exp_meeting_time)
		sessions_list = self.client_portal_page_obj.return_list_of_sessions()
		'''
		# delete the session created
		self.logIn()
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		# delete any previous session notes
		common.delete_session_notes()

		if exp_meeting_time in sessions_list:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
		'''