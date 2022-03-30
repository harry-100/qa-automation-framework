import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_009_CreateSessionClientPortalShowsClinicPortal:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_create_session_client_portal_shows_clinic_portal(self):
		common = CommonMethods(self.driver)

		# get the required data
		#client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 18, 2)
		user_name = XLUtility.readData(self.path_1, 'client_portal_data', 18, 3)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 18, 4)
		service = XLUtility.readData(self.path_1, 'client_portal_data', 18, 5)
		meeting_time = XLUtility.readData(self.path_1, 'client_portal_data', 18, 6)
		client_name = XLUtility.readData(self.path_1, 'client_portal_data', 18, 7)

		# Log in to client portal
		self.driver.get(self.client_portal_url)
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.input_username(user_name)
		self.client_portal_page_obj.input_password(password)
		self.client_portal_page_obj.clk_account_sign_in()
		sleep(1)

		# book a session on client portal
		self.client_portal_page_obj.clk_book_now()
		sleep(2)
		self.client_portal_page_obj.select_service(service)
		sleep(2)

		try:
			self.client_portal_page_obj.clk_jump_to_next_slot()
		except:
			pass
		sleep(1)
		self.client_portal_page_obj.clk_time_slot(meeting_time)
		sleep(1)
		self.client_portal_page_obj.clk_book_meeting()
		self.client_portal_page_obj.clk_confirm_booking()

		# check session booked on client portal

		self.client_portal_page_obj.clk_my_account()
		sleep(1)
		exp_meeting_time = meeting_time.replace(" ", "")
		exp_meeting_time = exp_meeting_time.replace(".", "")
		print("exp_meeting_time=", exp_meeting_time)
		sessions_details = self.client_portal_page_obj.get_session_booked_details()
		sessions_details = sessions_details.split("\n")
		service = service.split("(")
		str_2 = sessions_details[1].replace(service[0], "")
		str_2 = str_2.split("for")
		str_2 = str_2[0].strip()
		str_3 = str_2.split()
		suffix = common.get_date_number_suffix(int(str_3[2]))
		session_time = str_3[0] + " " + str_3[1] + " " + str_3[2] + suffix + " " + str_3[3] + " " + str_3[4] + " " + str_3[5]

		# Check on clinic portal

		self.logIn()
		self.login_page_obj.clk_clients_btn()
		self.client_page_obj.sel_client_name(client_name)
		self.client_page_obj.clk_navigate_sessions_notes()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		sessions_details_session_portal = self.notes_page_obj.get_first_session_details()
		print("sessions list", sessions_details_session_portal)

		# delete any previous session notes
		common.delete_session_notes()

		if session_time in sessions_details_session_portal:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.log.info("{} failed!".format(__name__))
			assert False
