import pytest
from time import sleep
from utilities import XLUtility
from pageObjects.common_functions.common_methods import CommonMethods
import imapclient
import email
import base64
import imaplib


@pytest.mark.skip(reason="Not Now")
@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_007_UserEmailVerification:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_user_email_verification(self):
		common = CommonMethods(self.driver)

		# get all the required data
		client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 14, 2)
		first_name = XLUtility.readData(self.path_1, 'client_portal_data', 14, 3)
		last_name = XLUtility.readData(self.path_1, 'client_portal_data', 14, 4)
		birth_date = XLUtility.readData(self.path_1, 'client_portal_data', 14, 5)
		phone_no = XLUtility.readData(self.path_1, 'client_portal_data', 14, 6)
		email_id = XLUtility.readData(self.path_1, 'client_portal_data', 14, 7)
		passwd = XLUtility.readData(self.path_1, 'client_portal_data', 14, 8)
		email_subject = XLUtility.readData(self.path_1, 'client_portal_data', 14, 9)
		client_name = first_name + " " + last_name

		imap_server = imaplib.IMAP4_SSL(host='mail.gmail.com')
		imap_server.login(email_id, passwd)
		imap_server.select(mailbox='INBOX', readonly=False)
		message_numbers_raw = imap_server.search(None, 'ALL')


		imap_obj.select_folder("INBOX", readonly=False)
		uids = imap_obj.search(['subject', email_subject])

		#self.driver.get(client_portal_url)
		#self.client_portal_page_obj.clk_create_account()
		# common.create_client_portal_user(first_name, last_name, birth_date, phone_no, email_id, passwd)

		for i in range(15):
			sleep(5)
			imap_obj.select_folder("INBOX", readonly=False)
			uids = imap_obj.search(['subject', email_subject])
			no_of_messages = len(uids)
			if len(uids) == 0:
				continue
			else:
				break
		print("no of messages ", no_of_messages)
		raw_messages = imap_obj.fetch(uids, ['BODY[]'])
		message = pyzmail.PyzMessage.factory(raw_messages[uids[0]][b'BODY[]'])

		for i in (0, no_of_messages - 1):
				message = pyzmail.PyzMessage.factory(raw_messages[uids[i]][b'BODY[]'])
				print("the message is ", message)
				text = message.text_part.get_payload().decode(message.text_part.charset)

		act_subject = message.get_subject()
		print("subject ", act_subject)
		#print("the message is ", message)
		sender = message.get_addresses('from')
		print("from = ", sender)
		#text = message.text_part.get_payload().decode(message.text_part.charset)
		print("text of the message is  ", text)
