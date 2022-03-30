import pytest
from time import sleep
from utilities import XLUtility
import imapclient
import pyzmail


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_004_UserForgotPassword:

	@pytest.fixture(autouse=True)
	def class_setup(self, one_time_setup):
		self.driver.maximize_window()

	def test_user_forgot_password(self):

		# get all the required data
		client_portal_url = XLUtility.readData(self.path_1, 'client_portal_data', 10, 2)
		first_name = XLUtility.readData(self.path_1, 'client_portal_data', 10, 3)
		last_name = XLUtility.readData(self.path_1, 'client_portal_data', 10, 4)
		birth_date = XLUtility.readData(self.path_1, 'client_portal_data', 10, 5)
		phone_number = XLUtility.readData(self.path_1, 'client_portal_data', 10, 6)
		email_id = XLUtility.readData(self.path_1, 'client_portal_data', 10, 7)
		password = XLUtility.readData(self.path_1, 'client_portal_data', 10, 8)
		new_password = XLUtility.readData(self.path_1, 'client_portal_data', 10, 9)
		client_name = first_name + " " + last_name

		imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
		email_id = XLUtility.readData(self.path_1, 'client_portal_data', 10, 10)
		passwd = XLUtility.readData(self.path_1, 'client_portal_data', 10, 11)
		imap_obj.login(email_id, passwd)
		imap_obj.select_folder("INBOX", readonly=False)
		email_subject = XLUtility.readData(self.path, 'client_portal_data', 10, 12)
		uids = imap_obj.search(['subject', email_subject])

		self.driver.get(client_portal_url)
		self.client_portal_page_obj.clk_create_account()
		self.client_portal_page_obj.input_client_first_name(first_name)
		self.client_portal_page_obj.input_client_last_name(last_name)
		self.client_portal_page_obj.input_client_birth_date(birth_date)
		self.client_portal_page_obj.input_phone_number(phone_number)
		self.client_portal_page_obj.input_email_id(email_id)
		self.client_portal_page_obj.input_client_password(password)
		self.client_portal_page_obj.input_again_password(password)
		self.client_portal_page_obj.clk_create_new_account()
		sleep(1)
		self.client_portal_page_obj.clk_sign_out()
		sleep(1)
		self.client_portal_page_obj.clk_sign_in_tab()
		self.client_portal_page_obj.clk_forgot_password()
		self.client_portal_page_obj.input_email_forgotten_password(email_id)
		self.client_portal_page_obj.clk_send_email()

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


		# back to client portal
		self.client_portal_page_obj.input_new_password(new_password)
		self.client_portal_page_obj.input_new_password_again(new_password)
		self.client_portal_page_obj.submit_new_password()
		sleep(1)
		exp_sign_in_message = "Success! Your Password has been reset "
		password_reset_message = self.client_portal_page_obj.capture_sign_in_message()
		print("the message is this again 999 =  ", password_reset_message)
		