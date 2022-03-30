from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from utilities.BasePage import BasePage


class ClientPortalPage(BasePage):

    # Top Tabs
    tab_home_xpath = "//button[@aria-label='Home']"
    tab_create_account_xpath = "//button[@aria-label='Create Account']"
    tab_book_now_xpath = "//button[@aria-label='Book Now']"
    tab_sign_in_xpath = "//button[@aria-label='Sign In']"
    tab_my_account_xpath = "//button[@aria-label='My Account']"
    tab_sign_out_xpath = "//button[@aria-label='Sign Out']"
    btn_mobile_menu_xpath = "//button[@aria-label='Menu'] "
    tab_messaging_xpath = "//button[@aria-label='Messaging']"

    # Sign In
    txt_username_name = "username"
    txt_password_name = "password"
    btn_account_sign_in_css = "*[data-testid='containers_app_sign-in-modal_sign-in']"
    sign_in_message_xpath = "//p[contains(@class, 'NotificationController')]"

    # Forgot Password
    btn_forgot_password_xpath = "//button[contains(text(), 'Forgot Password')]"
    txt_forgot_email_name = "forgotEmail"
    btn_send_email_xpath = "//button[@aria-label='Send email to reset password']"

    # Create Account Form
    txt_first_name = "first_name"
    txt_last_name = "last_name"
    txt_date_of_birth_xpath = "//input[contains(@class, 'DatePicker__DateInput')]"
    txt_phone_number_name = "mobile_phone"
    txt_email_id_name = "username"
    txt_password_name = "password"
    txt_reneter_password_name = "password2"
    btn_create_account_form_css = (
        "*[data-testid='containers_app_create-account-modal_create-account']"
    )

    btn_my_account_xpath = "//button[@aria-label='My Account']"
    btn_messaging_xpath = "//button[@aria-label='Messaging']"
    btn_session_booked_notification_xpath = "//p[contains(@class, 'NotificationController')]"
    tab_reset_password_css = "*[data-testid='containers_account_open_reset-password-modal']"
    txt_new_password_xpath = "//input[@label='New Password']"
    txt_retype_new_password_xpath = "//input[@label='Re-type Password']"
    btn_reset_password_css = "*[data-testid='containers_account_reset-password-modal_reset-password']"

    # Add Payment Method
    btn_add_payment_method_xpath = "//button[@aria-label='Add Payment Method']"
    txt_cardholder_name = "name"
    txt_street_name = "adress_line1"
    dd_country_xpath = "//div[@id='forms_payment-method_country']/div/div[2]"
    txt_country_xpath = (
        "//div[@id='forms_payment-method_country']/div[1]/div[1]/div[2]/div[1]/input[1]"
    )
    txt_city_name = "address_city"
    txt_state_name = "address_state"
    txt_postal_code_name = "address_zip"
    txt_card_number_name = "cardnumber"
    txt_card_expiration_date_name = "exp-date"
    txt_card_cvv_no_name = "cvc"
    btn_add_card_xpath = "//button[@aria-label='Add Card']"
    service_xpaths = (
        "//div[@data-testid='components_radio-button-group_for_which_service']/fieldset/div"
    )
    btn_jump_to_available_slot_xpath = "//button[contains(@aria-label,'Jump to')]"
    btn_book_meeting_xpath = "//button[@aria-label='Book']"
    btn_confirm_booking_xpath = "//button[@aria-label='Confirm Booking']"
    sessions_xpaths = "//div[@class='sessionHistory']/ul/li"
    # btn_cancel_session_xpath = (
    #    "//div[@class='sessionHistory']/ul/li[1]/div[2]//button[contains(text(), 'Cancel')]"
    # )
    btn_cancel_booking_xpath = "//button[@aria-label='Cancel Booking']"
    message_session_cancel_xpath = "//div[contains(@class,'common__ModalContent')]"
    mobile_message_session_cancel_xpath = "//div[contains(@class,'common__ModalContent')]"
    text_mobile_session_details_xpath = (
        "//div[@data-testid='components_common_table-wrapper-mobile']/div[1]/div[1]/div[2]"
    )
    btn_session_join_xpath = "//div[@class='sessionHistory']//button[contains(text(),'Join')]"
    message_join_session_xpath = "//div[contains(@class, 'Tooltip__Content')]"
    tab_secured_conversation_xpath = "//div[contains(@class, 'ChatList__ConversationList')]/div[1]"
    txt_message_textbox_id = "chat-input-box-textarea"
    btn_send_message_css = "*[data-testid='components_chat-input-box_send-message']"
    btn_attach_file_css = "*[data-testid='components_chat-actions-bar_attach_file']"
    tab_chat_message_xpaths = "//div[contains(@class, 'ChatView__Content')]/div"
    btn_delete_confirm_prospect_css = "*[data-testid='containers_clients_prospects_delete-prospect']"
    btn_mobile_prospects_css = "*[data-testid='components_mobile-side-menu_clients-prospects_mobile']"
    btn_mobile_delete_user_css = (
        "*[data-testid='containers_clients_prospects_open-delete-prospect-modal']"
    )
    # Secure messaging
    dd_therapists_list_xpaths = "//div[contains(@class,'react-select__menu-list')]/div"
    btn_add_new_conversation_css = "*[data-testid='components_chat-list_new-conversation']"
    dd_therapist_select_indicator_xpath = "//div[@id='forms_add-secure-conversation_therapist-id']/div[1]/div[2]/div[1]"

    # Client Portal
    list_of_pages_xpaths = "//nav[@aria-label='Main Navigation']/button"
    btn_cancel_session_xpath = "//button[@aria-label='Cancel Session']"
    btn_cancel_booking_xpath = "//button[@aria-label='Cancel Booking']"
    get_text_cancel_notificaiton_xpath = "//div[contains(text(),'This will remove your booking with this therapist.')]"
    btn_adjust_session_xpath = "//button[text()='Adjust Session']"
    session_tab_xpath = "//nav[@aria-label='Tab Navigation']"
    tab_financial_documents_xpath = "//h2[contains(text(),'Financial Documents')]"
    btn_service_price_xpath = "//input[@id='name-1']/..//div[2]/span/span[2]"
    tab_services_list_css = "*[data-testid='components_radio-button-group_for_which_service']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clk_sign_in_tab(self):
        self.click("XPATH", self.tab_sign_in_xpath)

    def input_username(self, user_name):
        self.enter("NAME", self.txt_username_name, user_name)

    def input_password(self, password):
        self.enter("NAME", self.txt_password_name, password)

    def clk_account_sign_in(self):
        self.click("CSS_SELECTOR", self.btn_account_sign_in_css)

    def capture_sign_in_message(self):
        sign_in_message = self.get_text("XPATH", self.sign_in_message_xpath)
        return sign_in_message

    def clk_create_account(self):
        self.click("XPATH", self.tab_create_account_xpath)

    # Create Account Form
    def input_client_first_name(self, first_name):
        self.enter("NAME", self.txt_first_name, first_name)

    def input_client_last_name(self, last_name):
        self.enter("NAME", self.txt_last_name, last_name)

    def input_client_birth_date(self, date_of_birth):
        self.enter("XPATH", self.txt_date_of_birth_xpath, date_of_birth)

    def input_phone_number(self, mobile_phone):
        self.enter("NAME", self.txt_phone_number_name, mobile_phone)

    def input_email_id(self, email_id):
        self.enter("NAME", self.txt_email_id_name, email_id)

    def input_client_password(self, password):
        self.enter("NAME", self.txt_password_name, password)

    def input_again_password(self, password):
        self.enter("NAME", self.txt_reneter_password_name, password)

    def clk_create_new_account(self):
        self.click("CSS_SELECTOR", self.btn_create_account_form_css)

    def clk_reset_password(self):
        self.click("CSS_SELECTOR", self.tab_reset_password_css)

    def clk_my_account(self):
        self.click("XPATH", self.tab_my_account_xpath)

    def input_new_password(self, new_password):
        self.enter("XPATH", self.txt_new_password_xpath, new_password)

    def input_new_password_again(self, new_password):
        self.enter("XPATH", self.txt_retype_new_password_xpath, new_password)

    def submit_new_password(self):
        self.click("CSS_SELECTOR", self.btn_reset_password_css)

    def clk_sign_out(self):
        self.click("XPATH", self.tab_sign_out_xpath)

    def clk_forgot_password(self):
        self.click("XPATH", self.btn_forgot_password_xpath)

    def input_email_forgotten_password(self, email_id):
        self.enter("NAME", self.txt_forgot_email_name, email_id)

    def clk_send_email(self):
        self.click("XPATH", self.btn_send_email_xpath)

    # Add Payment Card

    def clk_add_payment_card(self):
        self.click("XPATH", self.btn_add_payment_method_xpath)

    def input_cardholder_name(self, cardholder_name):
        self.enter("NAME", self.txt_cardholder_name, cardholder_name)

    def input_street_name(self, street_name):
        self.enter("NAME", self.txt_state_name, street_name)

    def input_country(self, country):
        self.click("XPATH", self.dd_country_xpath)
        self.enter("XPATH", self.txt_country_xpath, country)
        self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", country))

    def input_cty(self, city):
        self.enter("NAME", self.txt_city_name, city)

    def input_state(self, state):
        self.enter("NAME", self.txt_state_name, state)

    def input_postal_code(self, postal_code):
        self.enter("NAME", self.txt_postal_code_name, postal_code)

    def input_card_number(self, card_number):
        self.enter("NAME", self.txt_card_number_name, card_number)

    def input_card_expiration_date(self, expiration_date):
        self.enter("NAME", self.txt_card_expiration_date_name, expiration_date)

    def input_cvv_number(self, cvv_number):
        self.enter("NAME", self.txt_card_cvv_no_name, cvv_number)

    def clk_add_card(self):
        self.click("XPATH", self.btn_add_card_xpath)

    def clk_book_now(self):
        self.click("XPATH", self.tab_book_now_xpath)

    def clk_service(self, service):
        sel_service_xpath = "//div[@data-testid='components_radio-button-group_what_kind_of_service']/fieldset/div[2]/label/div[1]"
        self.click_js("XPATH", sel_service_xpath)

    def select_service(self, service):
        # self.wait_for_element_visibility("CSS_SELECTOR", "*[data-testid='containers_client_non-session-notes_table-body']")
        no_of_services = self.get_length(self.service_xpaths) - 1
        service_list = []
        for i in range(2, no_of_services + 2):
            service_name_x = self.get_text(
                "XPATH", "//div[@data-testid='components_radio-button-group_for_which_service']/fieldset/div[" + str(i) + "]/label/div[2]/span[1]/span[1]")
            #print("service name X ", service_name_x)
            service_list.append(service_name_x)
            print("service name x=", service_name_x)
            if service in service_name_x:
                select_service_xpath = "//div[@data-testid='components_radio-button-group_for_which_service']/fieldset/div[" + str(i) + "]/label/div[1]"
                self.click_js("XPATH", select_service_xpath)
                break
            else:
                continue
        return service_list

    def check_availability_of_slots(self):
        try:
            self.wait_for_element_presence("XPATH", self.btn_jump_to_available_slot_xpath)
        except:
            pass

        #	return False
        return True

    def clk_jump_to_next_slot(self):
        self.click("XPATH", self.btn_jump_to_available_slot_xpath)

    '''
	def clk_time_slot(self, meeting_time):
		time_slot_xpath = "//ul[@data-testid='forms_your-booking_time-slot-wrapper']//button[@aria-label='OPTION_VALUE']".replace("OPTION_VALUE", meeting_time)
		self.click("XPATH", time_slot_xpath)
	'''

    def clk_time_slot(self, meeting_time):
        time_slot_xpath = "//ul[@data-testid='forms_your-booking_time-slot-wrapper']/li[1]/button"
        self.click("XPATH", time_slot_xpath)

    def clk_book_meeting(self):
        self.click("XPATH", self.btn_book_meeting_xpath)

    def clk_confirm_booking(self):
        self.click("XPATH", self.btn_confirm_booking_xpath)

    def return_list_of_sessions(self):

        no_of_services = self.get_length(self.sessions_xpaths)
        sessions_list = []
        for i in range(1, no_of_services + 1):
            session_name_x = self.get_text(
                "XPATH", "//div[@class='sessionHistory']/ul/li[" + str(i) + "]/div[1]/div/span/span[2]")
            print("service name X", session_name_x)
            sessions_list.append(session_name_x)
        return sessions_list

    def get_session_booked_details(self):
        session_details = self.get_text(
            "XPATH", "//div[@class='sessionHistory']/ul/li[1]/div[1]/div")
        return session_details

    def get_list_of_services(self):
        # self.wait_for_element_visibility("CSS_SELECTOR", "*[data-testid='containers_client_non-session-notes_table-body']")
        no_of_services = self.get_length(self.service_xpaths) - 1
        service_list = []
        for i in range(2, no_of_services + 2):
            service_name_x = self.get_text(
                "XPATH", "//div[@data-testid='components_radio-button-group_for_which_service']/fieldset/div[" + str(i) + "]/label/div[2]/span/span[1]")
            service_list.append(service_name_x)
        return service_list

    def clk_cancel_session(self):
        self.click("XPATH", self.btn_cancel_session_xpath)

    def clk_cancel_booking(self):
        self.click("XPATH", self.btn_cancel_booking_xpath)

    def get_message_session_cancel(self):
        btn_session_cancel_element = (
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.btn_cancel_session_xpath)))
        )
        hover = ActionChains(self.driver).move_to_element(btn_session_cancel_element)
        hover.perform()
        message_cancel_session = self.get_text("XPATH", self.message_session_cancel_xpath)
        return message_cancel_session

    def get_mobile_message_session_cancel(self):
        btn_session_cancel_element = (
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.btn_cancel_session_xpath)))
        )
        hover = ActionChains(self.driver).move_to_element(btn_session_cancel_element)
        hover.perform()
        message_cancel_session = self.get_text("XPATH", self.mobile_message_session_cancel_xpath)
        return message_cancel_session

    def clk_mobile_menu(self):
        self.click("XPATH", self.btn_mobile_menu_xpath)

    def get_mobile_session_details(self):
        get_mobile_session_details = self.get_text("XPATH", self.text_mobile_session_details_xpath)
        return get_mobile_session_details

    def clk_join_session(self):
        self.click("XPATH", self.btn_session_join_xpath)

    def get_warning_message(self):
        btn_session_join_element = (
            self.wait.until(EC.presence_of_element_located((By.XPATH, self.btn_session_join_xpath)))
        )
        hover = ActionChains(self.driver).move_to_element(btn_session_join_element)
        hover.perform()
        message = self.get_text("XPATH", self.message_join_session_xpath)
        return message

    def clk_secured_conversation(self):
        self.click("XPATH", self.tab_secured_conversation_xpath)

    def input_message_textbox(self, message):
        self.enter("ID", self.txt_message_textbox_id, message)

    def clk_send_message(self):
        self.click("CSS_SELECTOR", self.btn_send_message_css)

    def clk_attach_file(self):
        self.click("CSS_SELECTOR", self.btn_attach_file_css)

    def get_messages(self):
        self.wait_for_element_visibility("XPATH", "//div[contains(@class, 'ChatView__Content')]")
        no_of_messages = self.get_length(self.tab_chat_message_xpaths)
        print("no of messages=", no_of_messages)
        message_list = []
        for i in range(1, no_of_messages + 1):
            sleep(0.5)
            print("the values of i is", i)
            try:
                message_x = self.get_text("XPATH", "//div[contains(@class, 'ChatView__Content')]/div[" + str(i) + "]/span[1]/span[1]/div[1]")
                print("message_x=", message_x)
            except:
                pass

            message_list.append(message_x)
        return message_list

    def clk_client_portal_messaging(self):
        self.click("XPATH", self.tab_messaging_xpath)

    def clk_confirm_delete_prospect(self):
        self.click("CSS_SELECTOR", self.btn_delete_confirm_prospect_css)

    def clk_mobile_prospects(self):
        self.click("CSS_SELECTOR", self.btn_mobile_prospects_css)

    def mobile_sel_prospect_name(self, client_name):
        sleep(2)
        #client_name_break = client_name.split()
        #client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        self.wait_for_element_visibility("XPATH", self.cb_select_mobile_client_xpaths)
        no_of_clients = self.get_length(self.cb_select_mobile_client_xpaths)
        for i in range(1, no_of_clients + 1):
            client_name_list_xpath = (
                "//*[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
            )
            self.wait_for_element_visibility("XPATH", client_name_list_xpath)
            client_name_list = self.driver.find_element_by_xpath(client_name_list_xpath).text
            if client_name in client_name_list:
                self.click("XPATH", client_name_list_xpath)
                break

    def clk_mobile_delete_user(self):
        self.click("CSS_SELECTOR", self.btn_mobile_delete_user_css)

    def get_list_of_therapists(self):
        no_of_therapists = self.get_length(self.dd_therapists_list_xpath)
        therapists_names_list = []
        for i in range(1, no_of_therapists + 1):
            therapists_name_x = self.get_text("XPATH", "//div[contains(@class,'react-select__menu-list')]/div[" + str(i) + "]")
            therapists_names_list.append(therapists_name_x)
        return therapists_names_list

    def clk_add_new_conversation(self):
        self.click("CSS_SELECTOR", self.btn_add_new_conversation_css)

    def clk_select_therapist_dropdown(self):
        self.click("XPATH", self.dd_therapist_select_indicator_xpath)

    def get_pages_list_client_portal(self):
        no_of_pages = self.get_length(self.list_of_pages_xpaths)
        pages_list = []
        for i in range(1, no_of_pages + 1):
            page_name_x = self.get_text("XPATH", "//nav[@aria-label='Main Navigation']/button[" + str(i) + "]  ")
            pages_list.append(page_name_x)
        return pages_list

    def clk_my_account(self):
    	self.click("XPATH", self.btn_my_account_xpath)

    def clk_cancel_session(self):
    	self.click("XPATH", self.btn_cancel_session_xpath)

    def clk_cancel_booking(self):
    	self.click("XPATH", self.btn_cancel_booking_xpath)

    def get_text_cancel_notificaiton(self):
    	cancel_text = self.get_text("XPATH", self.get_text_cancel_notificaiton_xpath)
    	return cancel_text

    def check_presence_adjust_button(self):
    	self.wait_for_element_visibility("XPATH", self.session_tab_xpath)
    	len = self.get_length(self.btn_adjust_session_xpath)
    	return len

    def check_presence_cancel_button(self):
    	self.wait_for_element_visibility("XPATH", self.session_tab_xpath)
    	len = self.get_length(self.btn_cancel_session_xpath)
    	return len
    	
    def check_presence_financial_documents_tab(self):
    	self.wait_for_element_visibility("XPATH", self.session_tab_xpath)
    	len = self.get_length(self.tab_financial_documents_xpath)
    	return len

    def check_presence_service_price_tab(self):
    	self.wait_for_element_visibility("CSS_SELECTOR", self.tab_services_list_css)
    	len = self.get_length(self.btn_service_price_xpath)
    	return len

