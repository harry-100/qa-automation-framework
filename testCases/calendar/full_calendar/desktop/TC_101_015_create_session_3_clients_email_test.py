import pytest
from time import (
	sleep,
)
from datetime import date

from datetime import timedelta

from utilities import XLUtility
import imapclient
import pyzmail
from pageObjects.common_functions.common_methods import CommonMethods


# This test checks the functionality of creating a session for 3 linked clients with email
@pytest.mark.usefixtures("one_time_setup")
class Test_TC101_015CreateSessionThreeClientsEmail:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()
		self.logIn()

	def test_create_session_3clients_email(self):
		common = CommonMethods(self.driver)
		self.log.info("starting test {}...".format(__name__))
		imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
		email_id = XLUtility.readData(self.path, 'session_data', 30, 7)
		passwd = XLUtility.readData(self.path, 'session_data', 30, 8)
		imap_obj.login(email_id, passwd)
		imap_obj.select_folder("INBOX", readonly=False)
		email_subject = XLUtility.readData(self.path, 'session_data', 30, 9)
		uids = imap_obj.search(['subject', email_subject])

		# clear any existing session
		common.delete_existing_session()
		client_name_1 = XLUtility.readData(self.path, 'session_data', 30, 2)

		# Complete the Session details form
		self.client_page_obj.clk_btn_clients()
		sleep(1)
		self.client_page_obj.sel_client_name(client_name_1)
		# Start creating session
		sleep(2)
		self.client_page_obj.clk_book_session()
		sleep(1)

		today_date = date.today()
		current_weekday = today_date.weekday()

		if current_weekday < 3:
			N = 3 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			date_time = str(meeting_date) + " 9:00am"

		if current_weekday >= 3:
			N = 10 - current_weekday
			meeting_date = today_date + timedelta(days=N)
			date_time = str(meeting_date) + " 9:00am"

		sleep(1)
		service = XLUtility.readData(self.path, 'session_data', 30, 4)
		common.create_client_session(service, date_time)
		sleep(1)
		self.client_page_obj.clk_client_session_details()
		sleep(2)

		self.client_page_obj.clk_btn_clients()
		client_name_2 = XLUtility.readData(self.path, 'session_data', 30, 5)
		self.client_page_obj.sel_client_name(client_name_2)
		sleep(2)
		self.client_page_obj.clk_client_session_details()
		sleep(2)

		self.client_page_obj.clk_btn_clients()
		client_name_3 = XLUtility.readData(self.path, 'session_data', 30, 6)
		self.client_page_obj.sel_client_name(client_name_3)

		self.client_page_obj.clk_client_session_details()
		self.calendar_page_obj.clk_session_info()
		self.calendar_page_obj.clk_more_information()
		sleep(2)
		self.calendar_page_obj.clk_delete_session()
		sleep(1)
		self.calendar_page_obj.clk_delete_session_warn()
		sleep(1)
		self.calendar_page_obj.clk_appointment_delete_confirm()

		year = meeting_date.strftime("%Y")
		month = meeting_date.strftime("%m")
		date1 = meeting_date.strftime("%d")
		exp_email_content = str(year + "-" + month + "-" + date1 + " at 09:00 AM")

		for i in range(15):
			sleep(5)
			imap_obj.select_folder("INBOX", readonly=False)
			uids = imap_obj.search(['subject', email_subject])
			no_of_messages = len(uids)
			if len(uids) == 0:
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
				"Test_TC101_015CreateSessionThreeClientsEmail " + self.dateFormat + ".png"
			)
			self.log.info("{} failed!".format(__name__))
			assert False
