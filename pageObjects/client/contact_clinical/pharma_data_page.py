from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities.BasePage import BasePage


class PharmaDataPage(BasePage):

    btn_contact_clinical_css = "*[data-testid='containers_client_navigation_contact-clinical']"
    btn_mobile_contact_clinical_css = "*[data-testid='containers_client_navigation_contact-clinical_mobile']"
    # btn_contact_clinical_css = "//span[contains(text(),'Contact & Clinical')]"
    #btn_contact_clinical_css = "//ul[contains(text(),'Navigate')]/li[2]"
    btn_mobile_contact_clinical_xpath = "*[@data-testid='containers_client_navigation_contact-clinical']"
    btn_medications_css = "*[data-testid='containers_client_contact-clinical_menu_medications']"
    btn_add_medications_css = (
        "*[data-testid='containers_client_contact-clinical_medications_add-medication']"
    )
    txt_dose_id = "forms_client_pharmacological-data_concentration"
    txt_frequency_id = "forms_client_pharmacological-data_frequency"
    txt_doctor_id = "forms_client_pharmacological-data_prescribing-doctor"
    dd_category_xpath = "//div[@id='forms_client_pharmacological-data_category']/div/div[2]"
    txt_category_xpath = (
        "//div[@id='forms_client_pharmacological-data_category']/div[1]/div[1]/div[2]/div[1]/input[1]"
    )
    dd_medication_name_xpath = "//div[@id='forms_client_pharmacological-data_name']/div/div[2]"
    txt_medication_name_xpath = (
        "//div[@id='forms_client_pharmacological-data_name']/div[1]/div[1]/div[2]/div[1]/input[1]"
    )

    txt_start_date_css = "*[ data-testid='forms_client_pharmacological-data_start-date']"
    txt_end_date_css = "*[ data-testid='forms_client_pharmacological-data_end-date']"
    btn_save_medication_css = "//button[@data-testid='containers_client_contact-clinical_medications_save-button']"

    tab_historical_medication_xpath = (
        "//div[@data-testid='containers_client_contact-clinical_medications_medication-history-list']"
        "/div[2]/div[1]"
    )

    btn_delete_current_medication_css = (
        "*[data-testid='containers_client_contact-clinical_medications_delete-button']"
    )

    btn_delete_historical_medication_css = (
        "*[data-testid='containers_client_contact-clinical_medications-history_delete-button']"
    )

    btn_delete_entry_medication_css = (
        "*[data-testid='containers_client_contact-clinical_delete-entry']"
    )

    tab_current_medication_xpath = (
        "//div[@data-testid='containers_client_contact-clinical_medications_medications-list']/div[1]"
    )
    btn_edit_historical_medication_css = (
        "*[data-testid='containers_client_contact-clinical_medications-history_edit-button']"
    )
    filter_css = "*[data-testid='components_datatable_header_button_toggle-filter-list']"
    filter_category_css = "*[data-testid='components_client-action-menu_drug-category']"
    filter_category_0_css = "*[data-testid='components_datatable_header_filter_category_0']"
    filter_category_adhd_css = "*[data-testid='components_client-action-menu_adhd']"
    tab_mobile_historical_medication_xpath = (
        "//div[@data-testid='containers_client_contact-clinical_medication_table-wrapper-mobile']/div[1]"
    )
    mobile_filter_xpath = (
        "//div[@data-testid='components_mobile-bottom-menu_icon-counter_wrapper']/button"
    )
    mobile_select_filter_xpath = "//ul[@datatest-id='components_mobile-filter-list_menu']/li[5]"
    mobile_close_filter_xpath = "/html/body/div[*]/div/div[2]/div/button"
    mobile_clear_filter_css = "*[data-testid='components_mobile-filter-list_button_clear-filters']"
    mobile_filtered_medication_xpath = (
        "//div[@data-testid='containers_client_contact-clinical_medication_table-wrapper-mobile']/div"
    )
    mobile_updated_medication_info_xpath = (
        "//div[@data-testid='containers_client_contact-clinical_medication_table-wrapper-mobile']"
        "/div[1]/div[2]/div[1]/div[1]/div[1]"
    )
    current_medications_list_xpaths = (
        "//div[@data-testid='containers_client_contact-clinical_medications_medications-list']/div"
    )
    historical_medications_list_xpaths = (
        "//div[@data-testid='containers_client_contact-clinical_medications_medication-history-list']"
        "/div[2]/div"
    )
    mobile_historical_medications_list_xpaths = (
        "//div[@data-testid='containers_client_contact-clinical_medication_table-wrapper-mobile']/div"
    )
    clear_filter_xpath = "//ul[@data-testid = 'containers_filter_menu']/li[5]"
    open_start_date_picker_xpath = "//button[@aria-label='open date picker']"
    filtered_medications_xpath = (
        "//div[@data-testid='containers_client_contact-clinical_medications_medication-history-list']"
        "/div[2]/div"
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def clk_contact_clinical_btn(self):
        self.click("CSS_SELECTOR", self.btn_contact_clinical_css)

    def clk_medications_btn(self):
        self.click("CSS_SELECTOR", self.btn_medications_css)

    def clk_add_medications_btn(self):
        self.click("CSS_SELECTOR", self.btn_add_medications_css)

    def clk_category_option(self):
        self.click("XPATH", self.dd_category_xpath)

    def input_category_option(self, category_option):
        self.enter("XPATH", self.txt_category_xpath, category_option)
        self.click("XPATH",
                   "//div[contains(@class,'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE",
                                                                                                      category_option))

    def clk_medication_name(self):
        self.click("XPATH", self.dd_medication_name_xpath)

    def input_medication_name(self, medication_name):
        self.enter("XPATH", self.txt_medication_name_xpath, medication_name)
        self.click("XPATH",
                   "//div[contains(@class,'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE",
                                                                                                      medication_name))

    def input_dose(self, dose):
        self.enter("ID", self.txt_dose_id, dose)

    def input_frequency(self, frequency):
        self.enter("ID", self.txt_frequency_id, frequency)

    def input_prescribing_doctor(self, doctor):
        self.enter("ID", self.txt_doctor_id, doctor)

    def input_start_date(self, start_date):
        self.enter("CSS_SELECTOR", self.txt_start_date_css, start_date)

    def input_end_date(self, end_date):
        self.enter("CSS_SELECTOR", self.txt_end_date_css, end_date)

    def clk_save_medication(self):
        self.click("XPATH", self.btn_save_medication_css)

    def clk_historical_medication_tab(self):
        historical_medication_info = self.get_text("XPATH", self.tab_historical_medication_xpath)
        self.click("XPATH", self.tab_historical_medication_xpath)
        return historical_medication_info

    def clk_delete_current_medication_btn(self):
        self.click("CSS_SELECTOR", self.btn_delete_current_medication_css)

    def clk_delete_historical_medication_btn(self):
        self.click("CSS_SELECTOR", self.btn_delete_historical_medication_css)

    def clk_delete_entry_medication_btn(self):
        self.click("CSS_SELECTOR", self.btn_delete_entry_medication_css)

    def clk_current_medication_tab(self):
        self.click("XPATH", self.tab_current_medication_xpath)
        current_medication_info = self.get_text("XPATH", self.tab_current_medication_xpath)
        return current_medication_info

    def set_dose_frequency_null(self):
        self.set_js("ID", self.txt_dose_id, '')
        self.set_js("ID", self.txt_frequency_id, '')

    def input_new_dose(self, new_dose):
        self.clear_field("ID", self.txt_dose_id)
        self.enter("ID", self.txt_dose_id, new_dose)

    def input_new_frequency(self, frequency):
        self.clear_field("ID", self.txt_frequency_id)
        self.enter("ID", self.txt_frequency_id, frequency)

    def clk_filter(self):
        self.click("CSS_SELECTOR", self.filter_css)

    def clk_filter_category(self):
        self.click("CSS_SELECTOR", self.filter_category_css)

    def clk_filter_category_0(self):
        self.click_js("CSS_SELECTOR", self.filter_category_adhd_css)

    def filtered_medications_info(self):
        self.wait_for_element_visibility("XPATH", self.filtered_medications_xpath )
        filtered_medications_list = self.driver.find_elements_by_xpath(self.filtered_medications_xpath)
        return filtered_medications_list

    def clear_filter(self):
        self.click("XPATH", self.clear_filter_xpath)

    def clk_mobile_historical_medication_tab(self):
        mobile_historical_medication_info = self.get_text("XPATH", self.tab_mobile_historical_medication_xpath)
        self.click("XPATH", self.tab_mobile_historical_medication_xpath)
        return mobile_historical_medication_info
    '''
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        tab_mobile_historical_medication_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, self.tab_mobile_historical_medication_xpath))
        )
        hover = ActionChains(self.driver).move_to_element(tab_mobile_historical_medication_element)
        hover.perform()
        mobile_historical_medication_info = tab_mobile_historical_medication_element.text
        tab_mobile_historical_medication_element.click()
        return mobile_historical_medication_info
    '''

    def clk_mobile_contact_clinical_btn(self):
        sleep(1)
        self.click("CSS_SELECTOR", self.btn_mobile_contact_clinical_css)
        '''
        contact_clinical_element = self.driver.find_element_by_css_selector(
            self.btn_contact_clinical_css
        )
        self.driver.execute_script("arguments[0].click();", contact_clinical_element)
        '''

    def clk_mobile_filter(self):
        self.click("XPATH", self.mobile_filter_xpath)

    def clk_mobile_select_filter(self):
        self.click("XPATH", self.mobile_select_filter_xpath)

    def clk_mobile_close_filter(self):
        self.click("XPATH", self.mobile_close_filter_xpath)

    def clk_mobile_clear_filter(self):
        self.click("CSS_SELECTOR", self.mobile_clear_filter_css)

    def mobile_filtered_medication_info(self):
        number_medications = self.get_length(self.mobile_filtered_medication_xpath)
        '''
        mobile_filtered_medications_list = (
            self.driver.find_elements_by_xpath(self.mobile_filtered_medication_xpath)
        )
        number_medications = len(mobile_filtered_medications_list)
        '''
        for i in range(1, number_medications + 1):
            # medicine_name = self.driver.find_element_by_xpath(
            #	"//div[@data-testid='containers_client_contact-clinical_medication_table-wrapper-mobile']"
            #	"/div[" + str(i) + "]/div[1]/div[1]").text
            medicine_name = self.get_text("XPATH",
                                          "//div[@data-testid='containers_client_contact-clinical_medication_table-wrapper-mobile']"
                                          "/div[" + str(i) + "]/div[1]/div[1]")
        return medicine_name

    def clk_edit_historical_medication(self):
        self.click("CSS_SELECTOR", self.btn_edit_historical_medication_css)

    def clk_mobile_updated_historical_medication(self):
        wait = WebDriverWait(self.driver, 10)
        sleep(3)
        tab_mobile_historical_medication_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, self.mobile_updated_medication_info_xpath))
        )
        hover = ActionChains(self.driver).move_to_element(tab_mobile_historical_medication_element)
        hover.perform()
        mobile_updated_historical_medication_info = self.get_text("XPATH", self.tab_mobile_historical_medication_xpath)
        # mobile_updated_historical_medication_info = tab_mobile_historical_medication_element.text
        self.click("XPATH", self.mobile_updated_medication_info_xpath)
        # tab_mobile_historical_medication_element.click()
        return mobile_updated_historical_medication_info

    def no_of_current_medications(self):
        self.wait_for_element_visibility("XPATH", "//div[contains(@class, 'ContactClinical__MedicationMainContainer')]")
        no_of_medications = self.get_length(self.current_medications_list_xpaths)
        return no_of_medications

    def no_of_historical_medications(self):
        self.wait_for_element_visibility("XPATH", "//div[contains(@class, 'ContactClinical__MedicationMainContainer')]")
        no_of_historical_medications = self.get_length(self.historical_medications_list_xpaths)
        return no_of_historical_medications

    def mobile_no_of_historical_medications(self):
        self.wait_for_element_visibility("XPATH", "//div[contains(@class, 'ContactClinical__MedicationMainContainer')]")
        mobile_no_of_historical_medications = self.get_length(self.mobile_historical_medications_list_xpaths)
        return mobile_no_of_historical_medications

    def pick_start_date_medication(self, start_date):
        self.click("XPATH", self.open_start_date_picker_xpath)
