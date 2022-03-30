from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class ClientsListPage(BasePage):
    tab_add_custom_list_css = "*[data-testid='containers_clients_navigation-add-custom-list']"
    txt_list_name = "listName"
    dd_tag_name_xpath = "//div[contains(@class, 'TagSelect__TagSelectField')]/div/div[2]"
    txt_tag_name_xpath = "//div[contains(@class, 'TagSelect__TagSelectField')]/div[1]/div[1]/div[2]/div[1]/input[1]"
    btn_add_client_list_xpath = "//button[contains(text(), 'Add Client List')]"
    btn_name_and_tags_xpath = "//button[contains(text(), 'Name and Tags')]"
    btn_table_columns_xpath = "//button[contains(text(), 'Table Columns')]"
    btn_column_order_xpath = "//button[contains(text(), 'Column Order')]"
    btn_sharing_xpath = "//button[contains(text(), 'Sharing')]"
    cb_column_first_name_xpath = "//div[@title='First Name']"
    cb_column_last_name_xpath = "//div[@title='Last Name']"
    cb_column_city_xpath = "//div[@title='City']"
    cb_user_access_owners_xpath = "//div[@title='Owners']"
    cb_user_access_therapists_xpath = "//div[@title='Therapists']"
    cb_user_access_office_admins_xpath = "//div[@title='Office Admins']"
    cb_user_access_private_xpath = "//div[@title='Private (only I get access)']"
    btn_delete_client_list_css = (
        "*[data-testid='containers_clients_lists_desktop_show-delete-confirmation']"
    )
    btn_delete_confirmation_client_list_css = "*[data-testid='containers_clients_lists_desktop_delete-list']"
    btn_export_client_list_css = "*[data-testid='containers_clients_lists_desktop_export-list']"
    btn_confirm_list_export_xpath = "//button[@aria-label='Export Client List']"
    cb_show_client_names_xpath = "//div[@title='Show Client Names']"
    btn_filter_css = "*[data-testid='components_datatable_header_button_toggle-filter-list']"
    private_lists_xpaths = "//ul[@data-testid='containers_clients_navigation_private-lists']/li"
    public_lists_xpaths = "//ul[@data-testid='containers_clients_navigation_shared-lists']/li"
    cb_office_admins_xpath = "//div[@title='Office Admins']"
    btn_mobile_delete_client_lists_css = "*[data-testid='containers_clients_lists_mobile_show-delete-confirmation']"
    btn_mobile_confirm_delete_client_lists_css = "*[data-testid='containers_clients_lists_mobile_delete-list']"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clk_add_custom_list(self):
        self.click("CSS_SELECTOR", self.tab_add_custom_list_css)

    def input_list_name(self, list_name):
        self.enter("NAME", self.txt_list_name, list_name)

    def clk_tag_name(self):
        self.click("XPATH", self.dd_tag_name_xpath)

    def input_tag_name(self, tag_name):
        # self.enter("XPATH", self.dd_tag_name_xpath, tag_name)
        self.click("XPATH", self.dd_tag_name_xpath)
        self.enter("XPATH", self.txt_tag_name_xpath, tag_name)
        self.click("XPATH", "//div[contains(@class,'react-select__menu-list')]//div[text()='OPTION_VALUE']".replace(
            "OPTION_VALUE", tag_name))

    # self.click("XPATH", "//div[contains(@class, 'react-select__option')]//div[text()='OPTION_VALUE']".replace(
    # "OPTION_VALUE", tag_name))

    def clk_add_client_list(self):
        self.click("XPATH", self.btn_add_client_list_xpath)

    def clk_name_and_tags(self):
        self.click("XPATH", self.btn_name_and_tags_xpath)

    def clk_table_columns(self):
        self.click("XPATH", self.btn_table_columns_xpath)

    def clk_column_order(self):
        self.click("XPATH", self.btn_column_order_xpath)

    def clk_sharing(self):
        self.click("XPATH", self.btn_sharing_xpath)

    def clk_column_last_name(self):
        self.click("XPATH", self.cb_column_last_name_xpath)

    def clk_column_first_name(self):
        self.click("XPATH", self.cb_column_first_name_xpath)

    def clk_column_city(self):
        self.click("XPATH", self.cb_column_city_xpath)

    def clk_user_access_owners(self):
        self.click("XPATH", self.cb_user_access_owners_xpath)

    def clk_user_access_therapists(self):
        self.click("XPATH", self.cb_user_access_therapists_xpath)

    def clk_user_access_office_admins(self):
        self.click("XPATH", self.cb_user_access_office_admins_xpath)

    def clk_user_access_private(self):
        self.click("XPATH", self.cb_user_access_private_xpath)

    def clk_delete_client_list(self):
        self.click("CSS_SELECTOR", self.btn_delete_client_list_css)

    def clk_delete_confirm_client_list(self):
        self.click("CSS_SELECTOR", self.btn_delete_confirmation_client_list_css)

    def clk_export_client_list(self):
        self.click("CSS_SELECTOR", self.btn_export_client_list_css)

    def clk_export_confirm_export_client_list(self):
        self.click("XPATH", self.btn_confirm_list_export_xpath)

    def clk_show_client_names(self):
        self.click("XPATH", self.cb_show_client_names_xpath)

    def clk_filter_client_list(self):
        self.click("CSS_SELECTOR", self.btn_filter_css)

    def clk_office_admins(self):
        self.click("XPATH", self.cb_office_admins_xpath)

    def get_clients_private_list(self):

        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_private-lists']")
        no_of_lists = self.get_length(self.private_lists_xpaths)
        clients_lists = []
        for i in range(1, no_of_lists + 1):
            clients_list_x = self.get_text("XPATH",
                                           "//ul[@data-testid='containers_clients_navigation_private-lists']/li[" + str(
                                               i) + "]/a/div")
            clients_lists.append(clients_list_x)
        return clients_lists

    def get_no_of_mobile_client_lists(self):
        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_private-lists']")
        no_of_lists = self.get_length(self.private_lists_xpaths)
        return no_of_lists

    def get_no_of_mobile_shared_client_list(self):
        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_shared-lists']")
        no_of_lists = self.get_length(self.public_lists_xpaths)
        return no_of_lists

    def clk_mobile_client_list(self):
        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_private-lists']")
        self.click("XPATH", "//ul[@data-testid='containers_clients_navigation_private-lists']/li[1]/a/div")

    def clk_mobile_shared_client_list(self):
        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_shared-lists']")
        self.click("XPATH", "//ul[@data-testid='containers_clients_navigation_shared-lists']/li[1]/a/div")

    def clk_mobile_delete_client_list(self):
        self.click("CSS_SELECTOR", self.btn_mobile_delete_client_lists_css)

    def clk_mobile_confirm_delete_client_list(self):
        self.click("CSS_SELECTOR", self.btn_mobile_confirm_delete_client_lists_css)

    def sel_clients_list(self, clients_list):

        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_private-lists']")
        no_of_lists = self.get_length(self.private_lists_xpaths)
        clients_lists = []
        for i in range(1, no_of_lists + 1):
            clients_list_x = self.get_text("XPATH",
                                           "//ul[@data-testid='containers_clients_navigation_private-lists']/li[" + str(
                                               i) + "]/a/div")
            clients_lists.append(clients_list_x)
            if clients_list_x == clients_list:
                select_client_list_xpath = "//ul[@data-testid='containers_clients_navigation_private-lists']/li[" + str(
                    i) + "]/a/div"
                sleep(0.5)
                self.click("XPATH", select_client_list_xpath)
                break
            else:
                continue

    def get_clients_public_list(self):

        self.wait_for_element_visibility("CSS_SELECTOR",
                                         "*[data-testid='containers_clients_navigation_shared-lists']")
        no_of_lists = self.get_length(self.public_lists_xpaths)
        clients_lists = []
        for i in range(1, no_of_lists + 1):
            clients_list_x = self.get_text("XPATH",
                                           "//ul[@data-testid='containers_clients_navigation_shared-lists']/li[" + str(
                                               i) + "]/a/div")
            clients_lists.append(clients_list_x)
        return clients_lists
