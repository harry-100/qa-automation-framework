import pytest
from time import sleep
from datetime import (
	date,
	timedelta
)
from utilities import XLUtility
import imapclient
import pyzmail
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session with 3 clients with email
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_115_CreateSession3CLientsWithEmail():

	@pytest.fixture(autouse=True)
	def classSetup(self, one_time_setup):
		self.logIn()

	def test_create_session_3clients_withemail(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		self.driver.set_window_size(411, 823)

		imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
		email_id = XLUtility.readData(self.path, 'session_mobile_data', 30, 7)
		passwd = XLUtility.readData(self.path, 'session_mobile_data', 30, 8)
		email_subject = XLUtility.readData(self.path, 'session_mobile_data', 30, 9)
		imap_obj.login(email_id, passwd)
		imap_obj.select_folder("INBOX", readonly=False)
		uids = imap_obj.search(['subject', email_subject])

		today_date = date.today()
		current_weekday = today_date.weekday()

		# delete any existing session
		common.mobile_delete_existing_session()

		# delete the sessions from client side
		client_name = XLUtility.readData(self.path, 'session_mobile_data', 30, 2)
		sleep(1)
		self.login_page_obj.clk_navigation_btn()
		sleep(1)
		self.client_page_obj.clk_all_clients_mobile()
		sleep(1)
		self.client_page_obj.mobile_sel_client_name(client_name)
		sleep(1)
		self.client_page_obj.clk_view_client_mobile()
		sleep(1)
		self.notes_page_obj.clk_session_notes()
		sleep(1)
		common.delete_mobile_prior_session_note()
		sleep(1)
		self.login_page_obj.clk_navigation_btn()
		# Start creating session
		sleep(1)
		self.login_page_obj.clk_mobile_calendar()
		sleep(1)

		# Start creating session
		self.calendar_page_obj.click_add_session()

		# Complete the Session details form

		# Select Client
		sleep(1)
		self.calendar_page_obj.input_clientname(client_name)

		# Select Date and Time
		sleep(1)

		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.date_time = str(meeting_date) + " 9:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			self.date_time = str(meeting_date) + " 9:00am"
		self.calendar_page_obj.txt_date_time(self.date_time)
		sleep(1)
		# Select Service type (CBT, Counselling, etc.)
		service = XLUtility.readData(self.path, 'session_mobile_data', 30, 4)
		self.calendar_page_obj.sel_service(service)
		sleep(2)
		# Click on Create Session
		self.calendar_page_obj.clk_create_session()
		sleep(1)
		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		self.client_page_obj.mobile_sel_client_name(client_name)
		sleep(2)
		self.client_page_obj.clk_view_client_mobile()
		sleep(2)
		self.calendar_page_obj.clk_mobile_client_session()
		sleep(2)

		# Details of second client
		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		client_name_2 = XLUtility.readData(self.path, 'session_mobile_data', 30, 5)
		self.client_page_obj.mobile_sel_client_name(client_name_2)
		sleep(2)
		self.client_page_obj.clk_view_client_mobile()
		sleep(2)
		# self.calendar_page_obj.clk_mobile_client_session()
		sleep(2)
		self.calendar_page_obj.clk_mobile_client_session()

		# Details of third client
		self.login_page_obj.clk_navigation_btn()
		self.client_page_obj.clk_all_clients_mobile()
		client_name_3 = XLUtility.readData(self.path, 'session_mobile_data', 30, 6)
		self.client_page_obj.mobile_sel_client_name(client_name_3)
		sleep(2)
		self.client_page_obj.clk_view_client_mobile()
		sleep(2)
		# self.calendar_page_obj.clk_mobile_client_session()
		sleep(2)
		self.calendar_page_obj.clk_mobile_client_session()

		self.calendar_page_obj.clk_mobile_client_view_session()
		sleep(1)
		self.calendar_page_obj.clk_delete_session()
		sleep(0.5)
		self.calendar_page_obj.clk_delete_session_warn()
		sleep(0.5)
		self.calendar_page_obj.clk_appointment_delete_confirm()
		sleep(5)
		year = meeting_date.strftime("%Y")
		month = meeting_date.strftime("%m")
		date1 = meeting_date.strftime("%d")
		exp_email_content = str(year + "-" + month + "-" + date1 + " at 09:00 AM")

		for i in range(15):
			sleep(5)
			imap_obj.select_folder("INBOX", readonly=False)
			uids = imap_obj.search(['subject', email_subject])
			no_of_messages = len(uids)
			if len(uids) ==0:
				continue
			else:
				break

		raw_messages = imap_obj.fetch(uids, ['BODY[]'])
		message = pyzmail.PyzMessage.factory(raw_messages[uids[0]][b'BODY[]'])
		text = message.text_part.get_payload().decode(message.text_part.charset)

		for i in (0, no_of_messages - 1):
			message = pyzmail.PyzMessage.factory(raw_messages[uids[i]][b'BODY[]'])
			text = message.text_part.get_payload().decode(message.text_part.charset)
			if "removed" in text:
				continue
			else:
				if exp_email_content in text:
					act_email_content = text

		imap_obj.delete_messages(uids)

		if exp_email_content in act_email_content:
			self.log.info("{} passed!".format(__name__))
			assert True
		else:
			self.driver.save_screenshot(
				self.pathScreenShot +
				"Test_TC101_115_CreateSession3CLientsWithEmail " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
