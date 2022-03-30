from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.client.contact_clinical.pharma_data_page import PharmaDataPage
from utilities.BasePage import BasePage
from pageObjects.calendar.full_calendar.calender_page import CalendarPage
from pageObjects.calendar.full_calendar.client_page import ClientPage
from pageObjects.calendar.full_calendar.login_page import LoginPage
from pageObjects.manage.forms.forms_page import FormsPage
from pageObjects.manage.forms.forms_add_form_page import AddFormsPage
from pageObjects.workflow.workflow_page import WorkFlowPage
from pageObjects.notes.notes_page import NotesPage
from pageObjects.manage.handwritten_notes_page import HandWrittenNotesPage
from pageObjects.client.finances.finances_page import FinancesPage
from pageObjects.client.waitlist_tags.waitlist_tags_page import WaitlistTagsPage
from pageObjects.client.client_portal.client_portal_page import ClientPortalPage
from pageObjects.settings.settings_page import SettingsPage

from datetime import date


class CommonMethods(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        super().__init__(driver)
        self.finances_page_obj = FinancesPage(self.driver)
        self.notes_page_obj = NotesPage(self.driver)
        self.pharma_data_page_obj = PharmaDataPage(self.driver)
        self.login_page_obj = LoginPage(self.driver)
        self.client_page_obj = ClientPage(self.driver)
        self.manage_forms_page_obj = FormsPage(self.driver)
        self.manage_forms_add_form_page_obj = AddFormsPage(self.driver)
        self.calendar_page_obj = CalendarPage(self.driver)
        self.waitlist_tags_page_obj = WaitlistTagsPage(self.driver)
        self.client_portal_page_obj = ClientPortalPage(self.driver)
        self.settings_page_obj = SettingsPage(self.driver)

    def delete_current_medication(self):
        try:
            no_of_medications = self.pharma_data_page_obj.no_of_current_medications()
            sleep(1)
            for i in range(1, no_of_medications + 1):
                self.pharma_data_page_obj.clk_current_medication_tab()
                sleep(1)
                self.pharma_data_page_obj.clk_delete_current_medication_btn()
                sleep(1)
                self.pharma_data_page_obj.clk_delete_entry_medication_btn()
        except Exception:
            self.log.info("No prior medication found")

    def delete_historical_medication(self):
        sleep(2)
        try:
            no_of_historical_medications = self.pharma_data_page_obj.no_of_historical_medications()
            for i in range(1, no_of_historical_medications + 1):
                self.pharma_data_page_obj.clk_historical_medication_tab()
                sleep(1)
                self.pharma_data_page_obj.clk_delete_historical_medication_btn()
                sleep(1)
                self.pharma_data_page_obj.clk_delete_entry_medication_btn()
                sleep(1)
        except Exception:
            self.log.info("No prior medications found")

    def delete_prior_receipts(self):
        sleep(2)
        no_of_receipts = self.finances_page_obj.number_of_receipts()

        try:
            for i in range(no_of_receipts):
                self.finances_page_obj.select_first_receipt()
                self.finances_page_obj.clk_delete_receipt()
                self.finances_page_obj.clk_delete_receipt_confirm()
        except Exception:
            self.log.info("Prior receipts not found")

    def delete_client_invoices(self):
        sleep(2)
        try:
            no_of_invoices = self.finances_page_obj.get_no_of_invoices()
            sleep(0.5)
            for i in range(no_of_invoices):
                self.finances_page_obj.select_first_invoice()
                sleep(0.5)
                self.finances_page_obj.clk_delete_client_invoice()
                sleep(0.5)
                self.finances_page_obj.clk_delete_confirm_client_invoice()
                sleep(1)
        except Exception:
            self.log.info("No prior invoices found")

    def delete_client_non_session_charges(self):
        sleep(2)
        try:
            no_of_non_session_charges = self.finances_page_obj.number_of_non_session_charge()
            print(" no of no session charges ", no_of_non_session_charges)
            sleep(0.5)
            for i in range(no_of_non_session_charges):
                self.finances_page_obj.sel_first_non_session_charge()
                sleep(0.5)
                self.finances_page_obj.clk_delete_non_session_charge()
                sleep(0.5)
                self.finances_page_obj.clk_delete_charge_non_session_charge()
                sleep(1)
        except Exception:
            self.log.info("No prior non_session_charge found")

    def delete_mobile_client_receipts(self):
        sleep(2)
        no_of_receipts = self.finances_page_obj.mobile_no_of_receipts()
        for i in range(no_of_receipts):
            sleep(0.5)
            self.finances_page_obj.sel_mobile_first_receipt()
            sleep(0.2)
            self.finances_page_obj.clk_delete_receipt()
            sleep(0.2)
            self.finances_page_obj.clk_delete_receipt_confirm()

    def delete_mobile_client_invoices(self):
        sleep(2)
        no_of_invoices = self.finances_page_obj.return_mobile_no_of_invoices()
        try:
            for i in range(no_of_invoices):
                sleep(0.5)
                self.finances_page_obj.clk_mobile_invoice()
                sleep(0.2)
                self.finances_page_obj.clk_mobile_invoice_delete()
                sleep(0.2)
                self.finances_page_obj.clk_mobile_invoice_delete_confirm()
        except Exception:
            self.log.info("no prior invocies found")

    def delete_mobile_session_notes(self):
        sleep(2)
        no_of_sessions = self.notes_page_obj.mobile_number_of_session_notes()
        try:
            for i in range(no_of_sessions):
                sleep(0.5)
                self.notes_page_obj.mobile_clk_first_session_notes()
                sleep(0.5)
                self.notes_page_obj.clk_mobile_delete_session_note()
                sleep(0.5)
                self.notes_page_obj.clk_mobile_confirm_delete_session_note()
        except Exception:
            self.log.info("No prior sessions found")

    def delete_mobile_non_session_charge(self):
        sleep(2)
        no_of_non_session_charges = self.finances_page_obj.mobile_no_of_non_session_charges()
        for i in range(no_of_non_session_charges):
            sleep(1)
            self.finances_page_obj.sel_mobile_first_non_session_charge()
            sleep(1)
            self.finances_page_obj.clk_mobile_delete_non_session_charge()
            sleep(1)
            self.finances_page_obj.clk_mobile_delete_confirm_non_session_charge()

    def delete_session_notes(self):
        sleep(2)
        no_of_notes = self.notes_page_obj.number_of_session_notes()
        for i in range(1, no_of_notes + 1):
            try:
                self.notes_page_obj.select_first_session_note()
                sleep(1)
                self.notes_page_obj.clk_delete_session()
                sleep(1)
                self.notes_page_obj.clk_confirm_delete_session()
                sleep(1)
                try:
                    self.notes_page_obj.clk_delete_and_notify()
                except Exception:
                    self.log.info("Delete and Notify button not found")
            except Exception:
                continue

    def delete_non_session_notes(self):
        sleep(2)
        no_of_non_session_notes = self.notes_page_obj.number_of_non_session_notes()
        try:
            for i in range(1, no_of_non_session_notes + 1):
                self.notes_page_obj.sel_non_session_note()
                sleep(0.5)
                self.notes_page_obj.clk_delete_non_session_note()
                sleep(0.5)
                self.notes_page_obj.clk_confirm_delete_non_session_note()
                sleep(0.5)
        except Exception:
            self.log.info("No prior notes found")

    def delete_mobile_prior_session_note(self):
        sleep(2)
        no_of_notes = self.notes_page_obj.mobile_number_of_session_notes()
        try:
            for i in range(1, no_of_notes + 1):
                sleep(1)
                self.notes_page_obj.mobile_clk_first_session_notes()
                sleep(1)
                self.notes_page_obj.clk_delete_session()
                sleep(1)
                self.notes_page_obj.clk_mobile_confirm_delete_session_note()

        except Exception:
            self.log.info("No prior sessions found")

    def delete_mobile_non_session_notes(self):
        sleep(2)
        no_of_notes = self.notes_page_obj.mobile_no_of_non_session_notes()

        try:
            for i in range(1, no_of_notes + 1):
                self.notes_page_obj.sel_mobile_first_non_session_note()
                sleep(0.5)
                self.notes_page_obj.clk_delete_non_session_note()
                sleep(0.5)
                self.notes_page_obj.clk_mobile_confirm_delete_non_session_note()
                sleep(0.5)
        except Exception:
            self.log.info("No prior non-session notes found")

    def delete_prior_forms_client_side(self, client_name):
        self.login_page_obj.clk_clients_btn()
        sleep(2)
        self.client_page_obj.sel_client_name(client_name)
        sleep(2)
        self.client_page_obj.clk_client_sessions_documents()
        sleep(1)
        no_of_forms = self.manage_forms_page_obj.return_client_no_of_forms()
        try:
            for i in range(1, no_of_forms + 1):
                sleep(1)
                self.client_page_obj.clk_client_document_list_options()
                sleep(1)
                self.client_page_obj.clk_client_documents_delete()
                sleep(1)
                self.client_page_obj.clk_client_documents_warn_delete()

        except Exception:
            self.log.info("No prior forms found")

    '''
    def delete_prior_manage_forms(self):
        self.login_page_obj.clk_manage_btn()
        self.manage_forms_page_obj.clk_manage_forms()
        sleep(1)
        no_of_manage_forms = self.manage_forms_page_obj.return_manage_no_of_forms()

        try:
            for i in range(1, no_of_manage_forms + 1):
                self.manage_forms_page_obj.select_manage_first_form()
                sleep(1)
                self.manage_forms_page_obj.clk_manage_forms_delete_form()
                sleep(1)
                self.manage_forms_page_obj.clk_manage_forms_confirm_delete_form()
                sleep(0.5)
                self.driver.refresh()
                sleep(1)
                self.manage_forms_page_obj.clk_manage_forms()
                sleep(0.5)
        except Exception:
            self.log.info("No prior forms found")
    '''

    def delete_prior_manage_forms(self):
        self.login_page_obj.clk_manage_btn()
        self.manage_forms_page_obj.clk_manage_forms()
        sleep(1)
        list_of_forms = self.manage_forms_page_obj.return_list_of_forms()
        print("list of forms=", list_of_forms)
        for form_name in list_of_forms:
            self.manage_forms_page_obj.sel_manage_forms_form_name(form_name)
            sleep(2)
            self.manage_forms_page_obj.clk_manage_forms_delete_form()
            sleep(2)
            self.manage_forms_page_obj.clk_manage_forms_confirm_delete_form()
            sleep(0.5)
            #self.driver.refresh()
            sleep(1)
            self.manage_forms_page_obj.clk_manage_forms()
            sleep(0.5)

    def delete_form_client_side(self, client_name):

        self.login_page_obj.clk_clients_btn()
        self.client_page_obj.sel_client_name(client_name)
        sleep(2)
        self.client_page_obj.clk_client_sessions_documents()
        sleep(1)
        self.client_page_obj.clk_client_document_list_options()
        sleep(1)
        self.client_page_obj.clk_client_documents_delete()
        sleep(1)
        self.client_page_obj.clk_client_documents_warn_delete()

    def delete_form_manage_side(self, new_form_name):
        self.manage_forms_page_obj.sel_manage_forms_form_name(new_form_name)
        sleep(2)
        self.manage_forms_page_obj.clk_manage_forms_delete_form()
        sleep(2)
        self.manage_forms_page_obj.clk_manage_forms_confirm_delete_form()

    def manage_add_form(self, new_form_name, text_question):
        self.login_page_obj.clk_manage_btn()
        self.manage_forms_page_obj.clk_manage_forms()
        self.manage_forms_page_obj.clk_manage_forms_add_form()
        sleep(2)
        self.manage_forms_add_form_page_obj.input_new_form_name(new_form_name)
        self.manage_forms_add_form_page_obj.clk_text_question()
        self.manage_forms_add_form_page_obj.input_text_question(text_question)
        sleep(1)
        self.manage_forms_add_form_page_obj.clk_save_new_form()
        sleep(2)
        self.manage_forms_add_form_page_obj.clk_new_form_text_editor()
        sleep(2)

    def mobile_delete_form_client_side(self, client_name):
        self.login_page_obj.clk_navigation_btn()
        self.client_page_obj.clk_all_clients_mobile()
        self.client_page_obj.mobile_sel_client_name(client_name)
        self.client_page_obj.clk_view_client_mobile()
        sleep(1)
        self.client_page_obj.clk_mobile_open_client_menu()
        sleep(2)
        self.client_page_obj.clk_client_sessions_documents()
        sleep(1)
        self.client_page_obj.clk_client_document_list_options()
        sleep(1)
        self.client_page_obj.clk_client_documents_delete()
        sleep(1)
        self.client_page_obj.clk_client_documents_warn_delete()
        sleep(1)

    def mobile_delete_form_manage_side(self, new_form_name):
        self.login_page_obj.clk_navigation_btn()
        self.login_page_obj.clk_mobile_forms_btn()
        sleep(1)
        self.manage_forms_page_obj.sel_mobile_manage_forms_form_name(new_form_name)
        sleep(1)
        self.manage_forms_page_obj.clk_manage_forms_delete_form()
        sleep(1)
        self.manage_forms_page_obj.clk_manage_forms_confirm_delete_form()

    def delete_existing_session(self):
        today_date = date.today()
        current_weekday = today_date.weekday()

        try:
            if current_weekday in range(3, 6):
                sleep(2)
                self.calendar_page_obj.clk_move_to_next_week()

            sleep(2)
            no_of_sessions = self.calendar_page_obj.get_no_of_sessions_for_delete()
            for i in range(no_of_sessions):
                sleep(1)
                self.calendar_page_obj.clk_session_for_delete()
                sleep(0.5)
                self.calendar_page_obj.clk_more_information()
                sleep(0.5)
                self.calendar_page_obj.clk_delete_session()
                sleep(0.5)
                self.calendar_page_obj.clk_delete_session_warn()
                sleep(0.5)
                try:
                    self.calendar_page_obj.clk_appointment_delete_confirm()
                except:
                    pass

        except Exception:
                self.log.info("No prior sessions found")

    def mobile_delete_existing_session(self):
        today_date = date.today()
        current_weekday = today_date.weekday()
        try:
            if current_weekday < 3 or current_weekday == 6:
                self.calendar_page_obj.clk_btn_calendar_view()
                self.calendar_page_obj.clk_btn_calendar_week_view()
                self.calendar_page_obj.clk_mobile_session_info()
                self.calendar_page_obj.clk_mobile_more_information()
                self.calendar_page_obj.clk_delete_session()
                self.calendar_page_obj.clk_delete_session_warn()
                self.calendar_page_obj.clk_appointment_delete_confirm()

            else:
                self.calendar_page_obj.clk_btn_calendar_view()
                self.calendar_page_obj.clk_btn_calendar_week_view()
                self.calendar_page_obj.clk_move_to_next_week()
                self.calendar_page_obj.clk_mobile_session_info()
                self.calendar_page_obj.clk_mobile_more_information()
                self.calendar_page_obj.clk_delete_session()
                self.calendar_page_obj.clk_delete_session_warn()
                self.calendar_page_obj.clk_appointment_delete_confirm()

        except Exception:
            self.log.info("No prior sessions found")

    def delete_all_day_session(self):
        try:
            self.calendar_page_obj.clk_all_day_session_info()
            self.calendar_page_obj.clk_personal_session_more_information()
            self.calendar_page_obj.clk_delete_session()
            self.calendar_page_obj.clk_delete_session_warn()
        except Exception:
            self.log.info("Prior Personal session not found")

    def mobile_delete_all_day_session(self):
        today_date = date.today()
        current_weekday = today_date.weekday()
        try:
            if current_weekday < 3 or current_weekday == 6:
                self.calendar_page_obj.clk_btn_calendar_view()
                self.calendar_page_obj.clk_btn_calendar_week_view()

            else:
                self.calendar_page_obj.clk_btn_calendar_view()
                self.calendar_page_obj.clk_btn_calendar_week_view()
                sleep(0.5)
                self.calendar_page_obj.clk_move_to_next_week()
            sleep(0.5)
            self.calendar_page_obj.clk_all_day_session()
            sleep(1)
            self.calendar_page_obj.clk_mobile_personal_session_more_information()
            sleep(2)
            self.calendar_page_obj.clk_delete_session()
            sleep(0.5)
            self.calendar_page_obj.clk_delete_session_warn()
        except Exception:
            self.log.info("No prior session found")

    def delete_sessions_client_side(self):
        try:
            no_of_client_sessions = self.client_page_obj.no_of_client_sessions()
            for i in range(1, no_of_client_sessions + 1):
                sleep(0.5)
                self.client_page_obj.select_first_client_session()
                sleep(0.5)
                self.client_page_obj.clk_delete_client_session()
                sleep(0.5)
                self.notes_page_obj.clk_mobile_confirm_delete_session_note()
                sleep(1)
        except Exception:
            self.log.info("No prior sessions found")

    def delete_mobile_historical_medication(self):
        try:
            no_of_historical_medications = self.pharma_data_page_obj.mobile_no_of_historical_medications()
            for i in range(1, no_of_historical_medications + 1):
                self.pharma_data_page_obj.clk_mobile_historical_medication_tab()
                sleep(1)
                self.pharma_data_page_obj.clk_delete_historical_medication_btn()
                sleep(1)
                self.pharma_data_page_obj.clk_delete_entry_medication_btn()
                sleep(1)
        except Exception:
            self.log.info("No prior medications found")

    def get_date_suffix(self, meeting_date):
        day = meeting_date.strftime("%-d")
        day = int(day)
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return suffix

    def client_form_url_title(self, browser_name):
        if browser_name == "chrome":
            exp_title = "Online Portal - Form"
        elif browser_name == "firefox":
            exp_title = "Online Portal - Form"
        elif browser_name == "Safari" or "Safari Technology Preview":
            exp_title = "Online Booking"
        return exp_title

    def create_client_session(self, service, date_time):
        sleep(1)
        self.calendar_page_obj.txt_date_time(date_time)
        sleep(2)
        self.calendar_page_obj.sel_service(service)
        sleep(2)
        self.calendar_page_obj.clk_create_session()
        sleep(2)

    def delete_settings_tags(self):
        sleep(1)
        settings_tags_list = self.waitlist_tags_page_obj.get_settings_tags_list()
        for tag_name in settings_tags_list:
            sleep(1)
            self.waitlist_tags_page_obj.delete_settings_tag(tag_name)
            sleep(1)
            self.waitlist_tags_page_obj.clk_confirm_delete_settings_tag()

    def create_client(self, first_name, last_name, therapist_name):
        sleep(1)
        self.client_page_obj.clk_add_new_client()
        sleep(1)
        self.client_page_obj.input_first_name(first_name)
        self.client_page_obj.input_last_name(last_name)
        sleep(1)
        self.client_page_obj.sel_therapist(therapist_name)
        sleep(1)
        self.client_page_obj.clk_add_client()

    def delete_client_by_name(self, client_name):
        no_of_clients_name = self.client_page_obj.sel_all_clients_name(client_name)
        try:
            for i in range(no_of_clients_name):
                self.client_page_obj.sel_client_name_for_delete(client_name)
                self.client_page_obj.clk_delete_client()
                self.client_page_obj.clk_confirm_delete_client()
                sleep(16)
                self.client_page_obj.clk_confirm_again_delete_client()
        except:
            pass

    def create_client_portal_user(self, first_name, last_name, birth_date, phone_number, email_id, password):
        sleep(1)
        self.client_portal_page_obj.input_client_first_name(first_name)
        self.client_portal_page_obj.input_client_last_name(last_name)
        self.client_portal_page_obj.input_client_birth_date(birth_date)
        self.client_portal_page_obj.input_phone_number(phone_number)
        self.client_portal_page_obj.input_email_id(email_id)
        self.client_portal_page_obj.input_client_password(password)
        self.client_portal_page_obj.input_again_password(password)
        sleep(0.5)
        self.client_portal_page_obj.clk_create_new_account()
        sleep(1)

    def get_date_number_suffix(self, day):
        day = int(day)
        if 4 <= day <= 20 or 24 <= day <= 30:
            suffix = "th"
        else:
            suffix = ["st", "nd", "rd"][day % 10 - 1]
        return suffix

    def create_service(self, service_details):
        service_name = service_details['service_name']
        duration = service_details['duration']
        service_type = service_details['service_type']
        therapist_grade = service_details['therapist_grade']
        service_fee = service_details['service_fee']
        allowed_portal = service_details['allowed_portal']
        video_bookable = service_details['video_bookable']

        # create service
        self.settings_page_obj.input_service_name(service_name)
        self.settings_page_obj.input_service_duration(duration)
        self.settings_page_obj.sel_service_type(service_type)
        self.settings_page_obj.sel_therapist_grade(therapist_grade)
        self.settings_page_obj.input_service_fee(service_fee)
        self.settings_page_obj.sel_allowed_on_portal(allowed_portal)
        self.settings_page_obj.bookable_as_video(video_bookable)
        self.settings_page_obj.clk_create_service()

    def mobile_delete_prsopects(self, prospect_name):
        self.login_page_obj.clk_navigation_btn()
        self.login_page_obj.clk_mobile_client_prospects()

        self.client_page_obj.mobile_sel_prospect_name(prospect_name)
        self.client_page_obj.clk_delete_user()
        self.client_portal_page_obj.clk_confirm_delete_prospect()
