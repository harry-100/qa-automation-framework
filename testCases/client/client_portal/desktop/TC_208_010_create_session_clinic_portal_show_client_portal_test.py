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
class Test_TC208_010_CreateSessionClinicPortalShowsClientPortal:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_create_session_clinic_portal_shows_client_portal(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# get the required data
		#client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 20, 2)
		user_name = XLUtility.readData(self.path_1, 'client_portal_data', 20, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 20, 4)
		service = XLUtility.readData(self.path_1, 'client_portal_data', 20, 5)
		session_time = XLUtility.readData(self.path_1, 'client_portal_data', 18, 6)
		client_name = XLUtility.readData(self.path_1, 'client_portal_data', 20, 7)

		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		# delete any previous session notes
		common.delete_session_notes()
		self.notes_page_obj.clk_client_add_session()
		today_date = date.today()
		meeting_date = today_date + timedelta(days=1)
		date_time = str(meeting_date) + " " + session_time

		# Complete the Session details form
		common.create_client_session(service, date_time)
		sleep(1)
		sessions_details_client_portal = self.notes_page_obj.get_first_session_details()
		print("\nsession_details=", sessions_details_client_portal)

		# Log in to client portal
		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)

		# check session booked on client portal
		self.client_portal_page_obj.clk_my_account()
		sleep(1)
		sessions_details = self.client_portal_page_obj.get_session_booked_details()
		sessions_details = sessions_details.split("\n")
		service = service.split("(")
		str_2 = sessions_details[1].replace(service[0], "")
		str_2 = str_2.split("for")
		str_2 = str_2[0].strip()
		str_3 = str_2.split()
		suffix = common.get_date_number_suffix(int(str_3[2]))
		session_time = str_3[0] + " " + str_3[1] + " " + str_3[2] + suffix + " " + str_3[3] + " " + str_3[4] + " " + str_3[5]

		# delete the session created
		#self.logIn()
		self.driver.get(self.base_url)
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		common.delete_session_notes()

		if session_time in sessions_details_client_portal:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
