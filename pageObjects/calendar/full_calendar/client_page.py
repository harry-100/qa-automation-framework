from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities.BasePage import BasePage


class ClientPage(BasePage):
    btn_clients_css = "*[data-testid='components_side-menu_navigation_clients']"
    btn_add_client_css = "*[data-testid='containers_top-menu_actions_add-client']"
    txt_first_name = "first_name"
    txt_last_name = "last_name"
    btn_add_client_xpath = "//button[contains(text(), 'Add Client')]"
    txt_preferred_name_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[1]/div[5]/div[2]/div[1]/input"
    )
    txt_date_of_birth_xpath = "*[data-testid='forms_add-client_date-of-birth']"
    sel_sex_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[1]/div[9]/div[2]/div[1]/div/div/div[2]/div"
    )
    txt_sex_id = "react-select-4-input"
    txt_email_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[1]/div[11]/div[2]/div[1]/input"
    )
    txt_phone_number_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[3]/div[2]/div[2]/div/input"
    )
    txt_street_name_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/div[2]/div[2]/div[1]/input"
    )
    txt_city_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/div[3]/div[2]/div[1]/input"
    )
    sel_region_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/div[4]/div[2]/div[1]/div/div/div[2]/div"
    )
    txt_region_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/div[4]/div[2]/div[1]/div/div/div[2]/div"
    )
    txt_postal_code_xpath = (
        "/html/body/div[2]/div/div[2]/div/div[2]/form/div[2]/div[6]/div[2]/div[1]/input"
    )
    dd_therapist_xpath = "//div[@id='forms_add-client_primary-therapist-id']/div[1]/div[2]"
    txt_therapist_xpath = "//div[@id='forms_add-client_primary-therapist-id']/div[1]/div[1]/div[2]/div[1]/input[1]"
    btn_add_and_view_xpath = "//button[contains(text(), 'Add and View')]"

    dd_client_status_xpath = "//div[@id='forms_add-client_status']/div/div[2]"
    txt_add_client_status_xpath = (
        "//div[@id='forms_add-client_status']/div[1]/div[1]/div[2]/div[1]/input[1]"
    )

    client_name_css = "span.ClientCodeBlock__ClientName-sc-1kkf2cz-1.bgCCLm"

    cb_select_client_xpath = (
        "//*[@id='app']/span/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]/div/div[2]/"
        "div[1]"
    )
    btn_view_client_xpath = "//button[@data-testid='containers_clients_all-clients_view']"

    client_session_details_xpath = (
        "//div[@data-testid='containers_client_session-notes_table-body']/div[1]/div[2]"
    )

    btn_book_session_css = "*[data-testid='components_client-top-panel_book-session']"

    # mobile elements

    btn_all_clients_mobile_css = (
        "*[data-testid='components_mobile-side-menu_clients-all-clients_mobile']"
    )
    btn_client_name_mobile_xpath = (
        "//div[@data-testid='components_common_table-wrapper-mobile']/div[1]"
    )
    btn_view_client_mobile_css = (
        "*[data-testid='containers_clients_all-clients_mobile_client-actions_view']"
    )

    client_session_details_mobile_xpath = (
        "//*[@id='app']/span/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/"
        "div[1]"
    )
    btn_client_session_mobile_css = "*[data-testid='components_client-top-panel_book-session']"
    sel_client_xpath = (
        "//*[@id='app']/span/div[2]/div[2]/div[2]/div/div/div/div[2]/div/div/div/div[2]"
        "/div/div[2]/div[1]"


    )
    btn_view_client_css = "*[data-testid='containers_clients_all-clients_view']"

    btn_mobile_open_client_menu_css = (
        "*[data-testid='components_mobile-bottom-menu_open-button_mobile']"
    )
    tab_client_sessions_send_forms_xpath = (
        "//*[@id='app']/div/div[2]/div[2]/div/div/div[1]/div/ul[2]/li[5]"
    )

    tab_client_sessions_documents_css = "*[data-testid='containers_client_navigation_documents']"
    tab_mobile_client_sessions_documents_css = "*[data-testid='containers_client_navigation_documents_mobile']"

    btn_client_documents_list_options_css = (
        "*[data-testid='containers_client_documents_list-item-options-button']"
    )

    btn_client_documents_delete_css = "*[data-testid='components_client-action-menu_delete']"

    btn_client_documents_delete_warning_css = (
        "*[data-testid='containers_client_documents_mobile_delete-document']"
    )
    tab_session_notes_css = "*[data-testid='containers_client_navigation_sessions-notes']"
    tab_client_session_xpath = (
        "//div[@data-testid='containers_client_session-notes_table-body']/div[1]"
    )
    btn_delete_client_session_css = (
        "*[data-testid='containers_client_sessions-notes_sessions_delete-session_mobile']"
    )
    cb_select_client_xpaths = "//div[@data-testid='components_table']/div[2]/div/div[3]"
    cb_select_mobile_client_xpaths = "//*[@data-testid='components_common_table-wrapper-mobile']/div"
    tab_client_documents_list_xpaths = "//div[@data-testid='containers_client_documents_list']/div"
    sel_session_xpaths = "//div[@data-testid='containers_client_session-notes_table-body']/div"
    select_first_session_xpath = (
        "//div[@data-testid='containers_client_session-notes_table-body']/div[1]/div[1]"
    )
    tab_mobile_client_add_session_xpath = "//div[normalize-space()='Add New Session']"
    btn_delete_client_css = "*[data-testid='containers_clients_all-clients_delete']"
    btn_delete_confirm_client_css = "*[data-testid='clients_all-clients_confirm-warn-delete-client']"
    btn_delete_confirm_again_client_xpath = "//button[contains(text(), 'Confirm Delete Client')]"

    # client filter elements

    all_client_filter_css = "*[data-testid='components_datatable_header_button_toggle-filter-list']"
    all_client_filter_tags_css = "*[data-testid='components_client-action-menu_tags']"
    all_client_filter_tags_item_css = "*[data-testid='components_client-action-menu_OPTION_VALUE']"
    all_client_filter_client_status_waitlist_css = (
        "*[data-testid='components_client-action-menu_waitlist']"
    )
    all_client_filter_client_status_css = (
        "*[data-testid='components_client-action-menu_client-status']"
    )
    txt_client_since_xpath = "//div[@data-testid='forms_add-client_client-since']/input"
    sel_client_status_xpath = "//div[@id='forms_add-client_status']/div/div[2]"
    tab_all_clients_waitlist_css = "*[data-testid='containers_clients_navigation_waitlist']"
    btn_edit_client_contact_clinical_xpath = "//button[contains(text(), 'Edit')]"

    # Edit clinical details form
    dd_client_status_xpath = "//div[@id='forms_client_clinical-details_status']/div/div[2]"
    sel_client_status_xpath = "//div[@id='forms_client_clinical-details_status']/div[1]/div[1]/div[2]/div[1]/input[1]"
    dd_waitlist_service_xpath = "//div[@id='forms_client_clinical-waitlisted-for-service']/div/div[2]"
    sel_waitlist_service_xpath = "//div[@id='forms_client_clinical-waitlisted-for-service']/div[1]/div[1]/div[2]/div[1]/input[1]"
    txt_waitlist_comments_name = "waitlist_comments"
    btn_clinical_details_save_css = (
        "*[data-testid='containers_client_contact-clinical-details_button-save']"
    )
    txt_client_status_since_xpath = (
        "//div[@data-testid='forms_client_clinical-details_status_since']/input"
    )
    tab_client_clinical_details_css = (
        "*[data-testid='containers_client_contact-clinical_menu_clinical-details']"
    )
    btn_client_edit_clinical_details_xpath = "//button[contains(text(), 'Edit')]"
    dd_client_status_xpath = "//div[@id='forms_client_clinical-details_status']/div[1]/div[2]"
    txt_client_status_xpath = "//div[@id='forms_client_clinical-details_status']/div[1]/div[1]/div[2]/div[1]/input[1]"
    btn_contact_clinical_save_css = "*[data-testid='containers_client_contact-clinical-details_button-save']"
    tab_waitlist_clients_css = "*[data-testid='containers_clients_navigation_waitlist']"
    btn_change_client_status_xpath = "//button[text()='Change Status']"
    btn_client_make_active_css = "*[data-testid='components_client-action-menu_active']"
    tab_all_clients_css = "*[data-testid='containers_clients_navigation_all-clients']"
    txt_waitlist_comments_name = "waitlist_comments"
    txt_waitlist_service_xpath = (
        "//div[@id='forms_client_clinical-waitlisted-for-service']/div[1]/div[1]/div[2]/div[1]/input[1]"
    )
    txt_new_client_waitlist_service_xpath = (
        "//div[@id='fforms_add-client_waitlisted-for-service']/div[1]/div[1]/div[2]/div[1]/input[1]"
    )
    btn_mobile_client_change_status_css = (
        "*[data-testid='containers_clients_waitlist_mobile_client-actions_change-status_button']"
    )
    btn_mobile_client_delete_css = (
        "*[data-testid='containers_clients_all-clients_mobile_client-actions_delete']"
    )
    txt_client_status_css = "*[data-testid='containers_client_contact-clinical_status']"
    btn_mobile_change_client_status_css = (
        "*[data-testid='containers_clients_all-clients_mobile_client-actions_change-status']"
    )
    tab_all_clients_prospects_css = "*[data-testid='containers_clients_navigation_prospects']"
    btn_delete_user_xpath = "//button[contains(text(), 'Delete User')]"

    # Secure Messaging
    tab_secure_messaging_css = "*[data-testid='containers_client_navigation_secure-messaging']"
    tab_client_chatlist_xpath = "//span[@class='Card__ClientName-xi2w08-3 lbrbRa']"
    txt_chatbox_area_id = "chat-input-box-textarea"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clk_btn_clients(self):
        self.click("CSS_SELECTOR", self.btn_clients_css)

    def sel_client_medication(self):
        self.click("XPATH", self.sel_client_xpath)

    def view_client(self):
        self.click("CSS_SELECTOR", self.btn_view_client_css)
        '''
		wait = WebDriverWait(self.driver, 10)
		view_client_element = wait.until(EC.presence_of_element_located(
			(By.CSS_SELECTOR, self.btn_view_client_css))
		)
		hover = ActionChains(self.driver).move_to_element(view_client_element)
		hover.perform()
		view_client_element.click()
		'''

    def clk_mobile_open_client_menu(self):
        sleep(2)
        # self.hover("CSS_SELECTOR", self.btn_mobile_open_client_menu_css)
        # self.click("CSS_SELECTOR", self.btn_mobile_open_client_menu_css)

        wait = WebDriverWait(self.driver, 10)
        btn_mobile_open_client_menu = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, self.btn_mobile_open_client_menu_css))
        )
        hover = ActionChains(self.driver).move_to_element(btn_mobile_open_client_menu)
        hover.perform()
        self.click("CSS_SELECTOR", self.btn_mobile_open_client_menu_css)
        # btn_mobile_open_client_menu.click()

    def clk_add_new_client(self):
        self.click("CSS_SELECTOR", self.btn_add_client_css)

    def input_first_name(self, first_name):
        self.enter("NAME", self.txt_first_name, first_name)

    def input_last_name(self, last_name):
        self.enter("NAME", self.txt_last_name, last_name)

    def clk_add_client(self):
        self.click("XPATH", self.btn_add_client_xpath)

    def clk_delete_client(self):
        self.click("CSS_SELECTOR", self.btn_delete_client_css)

    def clk_confirm_delete_client(self):
        self.click("CSS_SELECTOR", self.btn_delete_confirm_client_css)

    def clk_confirm_again_delete_client(self):
        self.click("XPATH", self.btn_delete_confirm_again_client_xpath)

    def input_preferred_name(self, preferredName):
        preferred_name_element = self.driver.find_element_by_xpath(self.txt_preferred_name_xpath)
        preferred_name_element.send_keys(preferredName)

    def input_date_of_birth(self, date_of_birth):
        date_of_birthcreate_client_element = self.driver.find_element_by_xpath(self.txt_date_of_birth_xpath)
        date_of_birth_element.send_keys(date_of_birth)

    def input_sex(self, sex):
        sel_sex_element = self.driver.find_element_by_xpath(self.sel_sex_xpath)
        txt_sex_element = self.driver.find_element_by_id(self.txt_sex_id)
        sel_sex_element.click()
        sleep(1)
        txt_sex_element.send_keys(sex)
        txt_sex_element.send_keys(Keys.RETURN)

    def input_email(self, email):
        txt_email_element = self.driver.find_element_by_xpath(self.txt_email_xpath)
        txt_email_element.send_keys(email)

    def input_phone_number(self, phone_number):
        txt_phone_number_element = self.driver.find_element_by_xpath(self.txt_phone_number_xpath)
        txt_phone_number_element.send_keys(phone_number)

    def input_street_name(self, street_name):
        txt_street_name_element = self.driver.find_element_by_xpath(self.txt_street_name_xpath)
        txt_street_name_element.send_keys(street_name)

    def input_city_name(self, city_name):
        txt_city_name_element = self.driver.find_element_by_xpath(self.txt_city_xpath)
        txt_city_name_element.send_keys(city_name)

    def input_region_name(self, region_name):
        sel_region_name_element = self.driver.find_element_by_xpath(self.sel_region_xpath)
        sel_region_name_element.click()
        sleep(1)
        txt_region_name_element = self.driver.find_element_by_xpath(self.txt_region_xpath)
        txt_region_name_element.send_keys(region_name)

    def input_postal_code(self, postal_code):
        txt_postal_code_element = self.driver.find_element_by_xpath(self.txt_postal_code_xpath)
        txt_postal_code_element.send_keys(postal_code)

    def clk_add_and_view(self):
        clk_add_and_view_element = self.driver.find_element_by_xpath(self.btn_add_and_view_xpath)
        clk_add_and_view_element.click()

    def sel_client(self):
        self.click("XPATH", self.cb_select_client_xpath)
        '''
		wait = WebDriverWait(self.driver, 10)
		cb_select_client_element = wait.until(EC.presence_of_element_located(
			(By.XPATH, self.cb_select_client_xpath))
		)
		ActionChains(self.driver).move_to_element(cb_select_client_element)
		sleep(2)
		cb_select_client_element.click()
		'''

    def sel_client_name(self, client_name):
        sleep(2)
        client_name_break = client_name.split()
        client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]/div")
        no_of_clients = self.get_length(self.cb_select_client_xpaths)

        for i in range(1, no_of_clients + 1):
            client_name_list_xpath = (
                "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[3]"
            )
            client_name_list = self.get_text("XPATH", client_name_list_xpath)
            if client_name_modified in client_name_list:
                self.click("XPATH", client_name_list_xpath)
                break
        sleep(1)
        try:
            self.click("CSS_SELECTOR", self.btn_view_client_css)
        except:
            pass

    def sel_client_name_for_delete(self, client_name):
        sleep(2)
        client_name_break = client_name.split()
        client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        no_of_clients = self.get_length(self.cb_select_client_xpaths)

        for i in range(1, no_of_clients + 1):
            client_name_list = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[3]")
            if client_name_modified in client_name_list:
                self.click("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[1]")
                break

    def check_client_name(self, client_name):
        sleep(2)
        client_name_break = client_name.split()
        client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        self.wait_for_element_visibility("XPATH", self.cb_select_client_xpaths)
        no_of_clients = self.get_length(self.cb_select_client_xpaths)
        for i in range(1, no_of_clients + 1):
            client_name_list = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[3]")
            if client_name_modified in client_name_list:
                client_present = "yes"
                break
            else:
                client_present = "no"
        return client_present

    def mobile_sel_client_name(self, client_name):
        sleep(2)
        client_name_break = client_name.split()
        client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        self.wait_for_element_visibility("XPATH", self.cb_select_mobile_client_xpaths)
        no_of_clients = self.get_length(self.cb_select_mobile_client_xpaths)
        for i in range(1, no_of_clients + 1):
            client_name_list_xpath = (
                "//*[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
            )
            self.wait_for_element_visibility("XPATH", client_name_list_xpath)
            client_name_list = self.driver.find_element_by_xpath(client_name_list_xpath).text
            if client_name_modified in client_name_list:
                self.click("XPATH", client_name_list_xpath)
                break

    def mobile_sel_inactive_client_name(self, client_name):
        sleep(2)
        client_name_break = client_name.split()
        client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        self.wait_for_element_visibility("XPATH", self.cb_select_mobile_client_xpaths)
        no_of_clients = self.get_length(self.cb_select_mobile_client_xpaths)
        for i in range(1, no_of_clients + 1):
            client_name_list_xpath = (
                "//*[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[1]/div[1]/div[1]/a"
            )
            self.wait_for_element_visibility("XPATH", client_name_list_xpath)
            client_name_list = self.driver.find_element_by_xpath(client_name_list_xpath).text
            if client_name_modified in client_name_list:
                self.click("XPATH", client_name_list_xpath)
                break

    def clk_view_client(self):
        self.click("XPATH", self.btn_view_client_xpath)
        '''
		wait = WebDriverWait(self.driver, 10)
		btn_view_client_element = wait.until(EC.presence_of_element_located(
			(By.XPATH, self.btn_view_client_xpath))
		)
		ActionChains(self.driver).move_to_element(btn_view_client_element)
		btn_view_client_element.click()
		'''

    def clk_client_session_details(self):
        self.click("XPATH", self.client_session_details_xpath)

    def clk_client_session(self):
        self.click("XPATH", self.tab_client_session_xpath)

    def clk_book_session(self):
        sleep(2)
        self.click("CSS_SELECTOR", self.btn_book_session_css)

    def clk_all_clients_mobile(self):
        self.click("CSS_SELECTOR", self.btn_all_clients_mobile_css)

    def clk_client_name_mobile(self):
        self.click("XPATH", self.btn_client_name_mobile_xpath)
        '''
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.presence_of_element_located((By.XPATH, self.btn_client_name_mobile_xpath)))
		ActionChains(self.driver).move_to_element(
			self.driver.find_element_by_xpath(self.btn_client_name_mobile_xpath)
		)
		self.driver.find_element_by_xpath(self.btn_client_name_mobile_xpath).click()
		'''

    def clk_view_client_mobile(self):
        self.click("CSS_SELECTOR", self.btn_view_client_mobile_css)
        '''
		wait = WebDriverWait(self.driver, 10)
		view_client_mobile_element = wait.until(EC.presence_of_element_located(
			(By.CSS_SELECTOR, self.btn_view_client_mobile_css))
		)
		self.driver.execute_script("arguments[0].click();", view_client_mobile_element)
		# view_client_mobile_element.click()
		'''

    def clk_client_create_session_mobile(self):
        self.click("CSS_SELECTOR", self.btn_client_session_mobile_css)

    def clk_client_sessions_send_forms(self):
        self.click("XPATH", self.tab_client_sessions_send_forms_xpath)

    def clk_client_sessions_documents(self):
        self.click("CSS_SELECTOR", self.tab_client_sessions_documents_css)

    '''
		sleep(1)
		tab_client_sessions_documents_element = (
			self.driver.find_element_by_css_selector(self.tab_client_sessions_documents_css)
		)
		self.driver.execute_script(
			"arguments[0].scrollIntoView();", tab_client_sessions_documents_element
		)
		self.driver.execute_script("arguments[0].click();", tab_client_sessions_documents_element)
	'''

    def clk_desktop_client_sessions_documents(self):
        self.click("CSS_SELECTOR", self.tab_client_sessions_documents_css)

    def clk_client_document_list_options(self):
        self.click("CSS_SELECTOR", self.btn_client_documents_list_options_css)

    def clk_client_documents_delete(self):
        self.click("CSS_SELECTOR", self.btn_client_documents_delete_css)

    def clk_client_documents_warn_delete(self):
        self.click("CSS_SELECTOR", self.btn_client_documents_delete_warning_css)

    def sel_client_documents_form(self):
        self.wait_for_element_visibility("XPATH", self.tab_client_documents_list_xpaths)
        no_of_forms = self.get_length(self.tab_client_documents_list_xpaths)
        form_name_list = []
        for i in range(1, no_of_forms + 1):
            form_name_x = (
                self.driver.find_element_by_xpath(
                    "//div[@data-testid='containers_client_documents_list']/div[" + str(i) + "]/div/"
                    "div/div/div[1]/span[1]").text
            )
            form_name_list.append(form_name_x)
        return form_name_list

    def clk_navigate_sessions_notes(self):
        self.click("CSS_SELECTOR", self.tab_session_notes_css)

    def no_of_client_sessions(self):
        no_of_sessions = self.get_length(self.sel_session_xpaths)
        return no_of_sessions

    def select_first_client_session(self):
        self.click("XPATH", self.select_first_session_xpath)

    def clk_delete_client_session(self):
        self.click("CSS_SELECTOR", self.btn_delete_client_session_css)

    def clk_tab_mobile_client_add_session(self):
        self.click("XPATH", self.tab_mobile_client_add_session_xpath)

    def clk_mobile_client_navigation_document(self):
        self.click("CSS_SELECTOR", self.tab_mobile_client_sessions_documents_css)

    def clk_all_client_filter(self):
        self.click("CSS_SELECTOR", self.all_client_filter_css)

    def clk_all_client_filter_tags(self):
        self.click("CSS_SELECTOR", self.all_client_filter_tags_css)

    def clk_all_client_filter_item(self, tag_name):
        self.click_js("CSS_SELECTOR", "*[data-testid='components_client-action-menu_" + tag_name + "']")

    def get_clients_list(self):
        sleep(2)
        self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]/div")
        no_of_clients = self.get_length(self.cb_select_client_xpaths)
        client_list = []
        for i in range(1, no_of_clients + 1):
            client_name_xpath = (
                "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[3]/span[1]/div[1]/a"
            )
            client_name_x = self.get_text("XPATH", client_name_xpath)
            client_list.append(client_name_x)
        return client_list

    def clk_client_clinical_details(self):
        self.click("CSS_SELECTOR", self.tab_client_clinical_details_css)

    def clk_client_edit_clinical_details(self):
        self.click("XPATH", self.btn_client_edit_clinical_details_xpath)

    def clk_edit_client_status(self, client_status):
        self.click("XPATH", self.dd_client_status_xpath)

    def input_edit_client_status(self, client_status):
        self.enter("XPATH", self.txt_client_status_xpath, client_status)
        self.click("XPATH", "//div[contains(@class,'react-select__menu')]"
                   "//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", client_status))

    def clk_contact_clinical_save(self):
        self.click("CSS_SELECTOR", self.btn_contact_clinical_save_css)

    def clk_all_clients_waitlist(self):
        self.click("CSS_SELECTOR", self.tab_waitlist_clients_css)

    def sel_therapist(self, therapist):
        self.click("XPATH", self.dd_therapist_xpath)
        self.enter("XPATH", self.txt_therapist_xpath, therapist)
        self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", therapist))

    def clk_client_change_status(self):
        self.click("XPATH", self.btn_change_client_status_xpath)

    def clk_make_client_active(self):
        self.click("CSS_SELECTOR", self.btn_client_make_active_css)

    def clk_all_clients(self):
        self.click("CSS_SELECTOR", self.tab_all_clients_css)

    def clk_add_client_status(self):
        self.click("XPATH", self.dd_client_status_xpath)

    def input_add_client_status(self, client_status):
        self.enter("XPATH", self.txt_add_client_status_xpath, client_status)
        self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", client_status))

    def add_referral(self):
        referral_name = "referral"
        self.enter("NAME", referral_name, "This is a referral")

    def input_waitlist_comments(self, waitlist_comments):
        self.enter("NAME", self.txt_waitlist_comments_name, waitlist_comments)

    def input_waitlist_service(self, waitlist_service):
        self.enter("XPATH", self.txt_waitlist_service_xpath, waitlist_service)
        self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", waitlist_service))

    def input_new_client_waitlist_service(self, waitlist_service):
        self.enter("XPATH", self.txt_new_client_waitlist_service_xpath, waitlist_service)
        self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", waitlist_service))

    def clk_filter_client_status(self):
        self.click("CSS_SELECTOR", self.all_client_filter_client_status_css)

    def clk_filter_client_status_waitlist(self):
        self.click("CSS_SELECTOR", self.all_client_filter_client_status_waitlist_css)

    def clk_mobile_client_change_status(self):
        self.click("CSS_SELECTOR", self.btn_mobile_client_change_status_css)

    def clk_mobile_delete_client(self):
        self.click("CSS_SELECTOR", self.btn_mobile_client_delete_css)

    def mobile_get_client_list(self):
        sleep(2)
        self.wait_for_element_visibility("XPATH", self.cb_select_mobile_client_xpaths)
        no_of_clients = self.get_length(self.cb_select_mobile_client_xpaths)
        client_list = []
        for i in range(1, no_of_clients + 1):
            client_name_list_xpath = (
                "//*[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[1]/div[1]/div[1]/a"
            )
            client_name_x = self.get_text("XPATH", client_name_list_xpath)
            client_list.append(client_name_x)
            # self.wait_for_element_visibility("XPATH", client_name_list_xpath)
            # client_name_list = self.driver.find_element_by_xpath(client_name_list_xpath).text
        return client_list

    def get_client_status(self):
        client_status = self.get_text("CSS_SELECTOR", self.txt_client_status_css)
        return client_status

    def clk_mobile_change_client_status(self):
        self.click("CSS_SELECTOR", self.btn_mobile_change_client_status_css)

    def sel_all_clients_name(self, client_name):
        sleep(2)
        client_name_break = client_name.split()
        client_name_modified = client_name_break[1] + ", " + client_name_break[0]
        self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]/div")
        no_of_clients = self.get_length(self.cb_select_client_xpaths)
        client_list_name = []
        for i in range(1, no_of_clients + 1):
            client_name_list_xpath = (
                "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[3]/span[1]/div[1]/a"
            )
            client_name_x = self.get_text("XPATH", client_name_list_xpath)
            if client_name_x == client_name_modified:
                client_list_name.append(client_name_x)
        no_of_clients_name = len(client_list_name)
        return no_of_clients_name

    def clk_all_clients_prospects(self):
        self.click("CSS_SELECTOR", self.tab_all_clients_prospects_css)

    def clk_delete_user(self):
        self.click("XPATH", self.btn_delete_user_xpath)

    def sel_prospect_name_for_delete(self, client_name):
        sleep(2)
        no_of_clients = self.get_length(self.cb_select_client_xpaths)

        for i in range(1, no_of_clients + 1):
            client_name_list = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[2]")
            if client_name in client_name_list:
                self.click("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[1]")
                break

    def mobile_sel_prospect_name(self, client_name):
        sleep(2)
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

    # Secure Messaging

    def clk_secure_messaging(self):
        self.click("CSS_SELECTOR", self.tab_secure_messaging_css)

    def clk_client_chat_list(self):
        self.click("XPATH", self.tab_client_chatlist_xpath)

    def enter_message(self, message):
        self.enter("ID", self.txt_chatbox_area_id, message)
