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
class Test_TC208_110_MobileCreateSessionClinicPortalShowsClientPortal:
	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.set_window_size(411, 823)
		self.logIn()

	def test_mobile_create_session_clinic_portal_shows_client_portal(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))

		# get the required data
		user_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 20, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 20, 4)
		service = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 20, 5)
		session_time = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 18, 6)
		client_name = XLUtility.readData(self.path_1, 'client_portal_mobile_data', 20, 7)

		today_date = date.today()
		meeting_date = today_date + timedelta(days=1)
		date_time = str(meeting_date) + " " + session_time

		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		self.client_page_obj.mobile_sel_client_name(client_name)
		self.client_page_obj.clk_view_client_mobile()
		self.notes_page_obj.clk_session_notes()

		# delete prior session notes
		common.delete_mobile_prior_session_note()

		# Click on Create Session button
		sleep(1)
		self.client_page_obj.clk_client_create_session_mobile()
		sleep(1)
		common.create_client_session(service, date_time)
		sleep(1)
		sessions_details_clinic_portal = self.client_portal_page_obj.get_mobile_session_details()

		# Log in to client portal
		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_mobile_menu()
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)
		self.client_portal_page_obj.clk_mobile_menu()
		self.client_portal_page_obj.clk_my_account()

		# check session booked on client portal
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
		self.driver.get(self.base_url)
		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		self.client_page_obj.mobile_sel_client_name(client_name)
		self.client_page_obj.clk_view_client_mobile()
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		self.notes_page_obj.mobile_clk_first_session_notes()
		sleep(1)
		self.notes_page_obj.clk_delete_session()
		sleep(1)
		self.notes_page_obj.clk_confirm_delete_session()

		if session_time in sessions_details_clinic_portal:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
