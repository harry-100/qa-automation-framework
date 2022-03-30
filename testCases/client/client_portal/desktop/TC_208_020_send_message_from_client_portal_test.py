import pytest
from time import sleep
from utilities import XLUtility


@pytest.mark.usefixtures("one_time_setup")
class Test_TC208_020_SendMessageFromClientPortal:
    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.driver.maximize_window()

    def test_send_message_from_client_portal(self):
        self.log.info("starting test {}...".format(__name__))

        # get the required data
        user_name = XLUtility.readData(self.path_1, 'client_portal_data', 40, 3)
        password = XLUtility.readData(self.path_1, 'client_portal_data', 40, 4)
        message_1 = XLUtility.readData(self.path_1, 'client_portal_data', 40, 5)
        '''
        # Log in to client portal
        self.driver.get(self.client_portal_url)
        self.client_portal_page_obj.clk_sign_in_tab()
        self.client_portal_page_obj.input_username(user_name)
        self.client_portal_page_obj.input_password(password)
        self.client_portal_page_obj.clk_account_sign_in()
        sleep(1)
        self.client_portal_page_obj.clk_client_portal_messaging()
        self.client_portal_page_obj.clk_secured_conversation()
        sleep(2)
        self.client_portal_page_obj.input_message_textbox(message_1)
        self.client_portal_page_obj.clk_send_message()
        '''
        # log in to clinic portal
        self.logIn()
        self.login_page_obj.clk_messaging_btn()
        sleep(1)
        self.client_portal_page_obj.clk_secured_conversation()
        sleep(1)
        message_list = self.client_portal_page_obj.get_messages()
        print("message_list=", message_list)
        last_message = message_list[-1]
        print("last message=", last_message)

        if last_message == message_1:
            self.log.info("{} passed!".format(__name__))
            assert True
        else:
            self.log.info("{} failed!".format(__name__))
            assert False
