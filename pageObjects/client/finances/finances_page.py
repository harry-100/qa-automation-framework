from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities.BasePage import BasePage


class FinancesPage(BasePage):

	tab_receipts_xpath = "//button[normalize-space()='Receipts']"
	tab_invoices_xpath = "//button[normalize-space()='Invoices']"
	tab_refunds_xpath = "//button[normalize-space()='Refunds']"
	tab_non_session_charges_xpath = "//button[normalize-space()='Non-Session Charges']"
	tab_client_navigation_finances_css = "*[data-testid='containers_client_navigation_finances']"
	tab_recipts_css = "*[data-testid='receipts_tab']"
	tab_invoices_css = "*[data-testid='invoices_tab']"
	tab_refunds_css = "*[data-testid='refunds_tab']"
	tab_non_session_charges_css = "*[data-testid='non-session-charges_tab']"
	btn_add_item_css = "*[data-testid='components_datatable_header_button_add-item']"
	tab_record_payment_id = "containers_client_navigation_record-payment"
	dd_payment_type_control_xpath = (
		"//div[@data-testid='components_record-payment_payment-method']/div[2]/div[1]/div[2]"
	)
	dd_payment_type_input_xpath = (
		"//div[@data-testid='components_record-payment_payment-method']/div[2]/div[1]/div[1]/div[2]/"
		"div[1]/input[1]"
	)
	txt_payment_amount_xpath = (
		"//div[@data-testid='components_record-payment_payment-amount']/div[2]/div[2]/div[1]/input[1]"
	)
	txt_confirmation_number_css = "*[data-testid='components_record-payment_confirmation-number']"

	btn_record_payment_xpath = "//button[contains(text(),'Record Payment')]"
	btn_generate_credit_xpath = "//button[contains(text(),'Generate Credit')]"
	btn_close_pdf_preview_xpath = "//button[contains(text(),'Close')]"
	tab_account_details_css = (
		"*[data-testid='containers_client_contact-clinical_menu_account-details']"
	)
	btn_edit_account_details_xpath = "//*[@id='app']/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/button"
	dd_payment_term_control_xpath = (
		"//div[@id='forms_client_account-details_payment-terms-select']/div[1]/div[2]"
	)
	dd_payment_term_input_xpath = (
		"//div[@id='forms_client_account-details_payment-terms-select']/div[1]/div[1]/div[2]/"
		"div[1]/input[1]"
	)
	btn_save_acount_details_xpath = "//button[contains(text(),'Save')]"
	btn_mark_attendance_css = (
		"*[data-testid='containers_client_sessions-notes_sessions_mark-attendance_mobile']"
	)
	btn_session_attended_css = "*[data-testid='components_client-action-menu_attended']"
	first_invoice_xpath = "//div[@data-testid='components_table']/div[2]/div[1]"
	btn_delete_client_invoice_css = "*[data-testid='containers_client_delete-invoice-button']"
	btn_delete_confirm_client_invoice_css = (
		"*[ data-testid='containers_client_confirm-delete-invoice']"
	)
	tab_client_navigation_create_invoice_id = "containers_client_navigation_create-invoice"
	txt_invoice_date_range_start_date_xpath = (
		"//div[@data-testid='components_create-invoice_date-range-wrapper']/div[1]/input[1]"
	)
	btn_create_invoice_find_session_range_css = (
		"*[data-testid='components_create-invoice_find-session-range-button']"
	)
	btn_create_invoice_css = "*[data-testid='components_create-invoice_create-invoice-button']"
	btn_client_invoice_pdf_preview_close_css = (
		"*[data-testid='containers_client-action-controller_pdf-preview-modal']"
	)
	text_message_delete_invoiced_session_xpath = "/html/body/div[*]/div/div/span"
	txt_non_session_chage_billable_name = "billable_name"
	txt_non_session_charge_date_xpath = (
		"//div[@data-testid='components_date-picker_wrapper']/div[2]/input[1]"
	)
	dd_non_session_charge_therapist_xpath = "//div[@id='non_session_charge_therapist']/div/div[2]"

	dd_non_session_charge_therapist_name_xpath = (
		"//div[@id='non_session_charge_therapist']/div[1]/div[1]/div[2]/div[1]/input[1]"
	)
	txt_non_session_charge_amount_css = (
		"*[data-testid='containers_client_finances_non-session-charge_amount-charged']"
	)
	txt_non_session_charge_amount_xpath = "/html/body/div[2]/div/div[2]/div/div[2]/form/div[4]/div[2]/div[2]"

	btn_autoinvoice_yes_xpath = (
		"//input[@data-testid='containers_client_finances_non-session-charge_auto-invoice_yes']/.."
	)
	btn_autoinvoice_no_xpath = (
		"//input[@data-testid='containers_client_finances_non-session-charge_auto-invoice_no']/.."
	)
	btn_non_session_charge_save_xpath = "//button[@aria-label='save charge']"
	btn_client_view_invoice_css = "*[data-testid='containers_client_view-invoice-button']"
	#tab_pdf_preview_add_email_xpath = (
	#	"//ul[@data-testid='components_pdf-preview_email-recipients_list']/li[1]"
	#)
	tab_pdf_preview_add_email_xpath = "//a[@data-testid = 'component_email-recipients_check-recipient-wrapper']"
	btn_pdf_preview_send_email_css = "*[data-testid='components_client-action-menu_email']"
	btn_client_adjust_invoice_css = "*[data-testid='containers_client_adjust-invoice-button']"
	txt_reason_for_adjustment_xpath = "//input[contains(@class,'UnpaidItem__ReasonInput')]"
	txt_new_adjusted_amount_xpath = (
		"//div[@data-testid='components_table']/div[2]/div[2]/div[3]/span[1]/div[1]/div[2]/input[1]"
	)
	btn_client_adjust_invoice_xpath = (
		"//div[@data-testid='components_table']/div[2]/div[2]/div[4]/span[1]/button[1]"
	)
	btn_client_invoice_balance_adjust_close_css = (
		"*[data-testid='containers_client-invoices_close-balance-adjustment-modal']"
	)
	btn_pdf_preview_refund_css = "*[data-testid='components_PdfPreview_button-refund']"
	txt_inovice_refund_confirmation_number_name = "confirmation_number"
	txt_client_invoice_refund_amount_xpath = (
		"//div[@data-testid=‘components_table’]/div[2]/div[1]/div[7]/span/div[1]/div[1]/input[1]"
	)
	btn_client_invoice_refund_payment_xpath = "//button[contains(text(),'Refund Payment')]"
	btn_forms_refund_payment_refund_css = "*[ data-testid='forms_refund-payment_button-refund']"
	txt_client_account_details_global_discount_xpath = (
		"//div[@data-testid='components_table']/div[2]/div[1]/div[5]/span[1]/div[1]/div[2]/input[1]"
	)
	txt_mobile_client_global_discount_xpath = "/html/body/div[*]/div/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div[2]/input"
	tab_client_credit_balance_xpath = "//button[@aria-label='view billing']/div[2]/div[1]/span[1]"
	tab_client_balance_xpath = "//button[@aria-label='view billing']/div[1]/div[1]/span[1]/span "
	cb_record_payment_use_account_credit_xpath = "//div[@title='Use Account Credit']"
	btn_delete_non_session_charge_xpath = "//button[@aria-label='confirm delete charge']"
	btn_delete_charge_non_session_charge_xpath = "//button[@aria-label='delete charge']"
	txt_allocate_manually_payment_1_xpath = (
		"//div[@data-testid='components_table']/div[2]/div[1]/div[6]/span[1]/div[1]/div[1]/input[1]"
	)
	txt_allocate_manually_payment_2_xpath = (
		"//div[@data-testid='components_table']/div[2]/div[2]/div[6]/span[1]/div[1]/div[1]/input[1]"
	)
	tab_mobile_record_payment_id = "containers_client_navigation_record-payment"
	tab_client_contact_clinical_account_details_css = (
		"*[data-testid='containers_client_contact-clinical_menu_account-details']"
	)
	btn_client_account_details_edit_css = (
		"*[data-testid='containers_client_contact-clinical_account_edit-button']"
	)
	dd_payment_terms_xpath = (
		"//div[@id='forms_client_account-details_payment-terms-select']/div/div[2]"
	)
	input_payment_terms_xpath = (
		"//div[@id='forms_client_account-details_payment-terms-select']/div[1]/div[1]/div[2]/div[1]"
		"/input[1]"
	)
	btn_client_account_details_save_css = "*[data-testid='containers_client_account-details_save-button']"
	no_of_invoices_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div"
	first_mobile_invoice_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[1]"
	btn_mobile_invoice_delete_css = "*[data-testid='containers_client_delete-invoice-button']"
	btn_mobile_invoice_delete_confirm_css = (
		"*[data-testid='containers_client_confirm-delete-invoice']"
	)
	btn_mobile_session_mark_attendance_css = (
		"*[data-testid='containers_client_sessions-notes_sessions_mark-attendance_mobile']"
	)
	mobile_session_status_xpath = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div[1]/div[2]/div[1]/div[1]/"
		"div[1]/div[3]"
	)
	receipt_xpaths = "//div[@data-testid='components_table']/div[2]/div"
	sel_session_xpaths = (
		"//div[@data-testid='containers_client_session-notes_table-body']/div"
	)
	invoices_xpaths = "//div[@data-testid='components_table']/div[2]/div"
	sel_invoices_xpaths = "//div[@data-testid='components_table']/div[2]/div"
	selected_invoice_amount_charged_xpath = (
		"//div[@data-testid='components_table']/div[2]/div[1]/div[6]"
	)
	sel_non_session_charges_xpaths = "//div[@data-testid='components_table']/div[2]/div"
	first_invoice_number_xpath = "//div[@data-testid='components_table']/div[2]/div[1]/div[3]"
	sel_refunds_xpaths = "//div[@data-testid='components_table']/div[2]/div"
	sel_session_notes_xpaths = "//div[@data-testid='containers_client_session-notes_table-body']/div"
	sel_non_session_charge_xpaths = "//div[@data-testid='components_table']/div[2]/div"
	sel_first_non_session_charge_xpath = "//div[@data-testid='components_table']/div[2]/div[1]"
	first_receipt_xpath = "//div[@data-testid='components_table']/div[2]/div[1]"
	btn_delete_receipt_confirm_xpath = "//button[@aria-label='delete receipt']"
	btn_delete_receipt_xpath = "//button[@aria-label='confirm delete receipt']"
	cb_record_payment_manually_xpath = "//div[@title='Allocate Payments Manually']"
	tab_mobile_client_navigation_finance_css = (
		"*[data-testid='containers_client_navigation_finances_mobile']"
	)
	btn_mobile_client_actions_record_payment_css = (
		"*[data-testid='components_client-action-menu_record-payment']"
	)
	sel_mobile_client_receipts_xpaths = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div"
	)
	mobile_first_receipt_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[1]"
	mobile_first_non_session_charge_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[1]"
	mobile_non_session_charge_xpaths = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div"
	)
	btn_mobile_delete_non_session_charge_css = (
		"*[data-testid='containers_client_finances_delete-charge-button']"
	)
	btn_mobile_delete_confirm_non_session_charge_css = (
		"*[data-testid='containers_client_finances_confirm-delete-charge-button']"
	)
	btn_mobile_add_item_css = "*[data-testid='components_mobile-bottom-menu_add-item-button']"
	txt_mobile_invoice_adjust_amount_css = (
		"*[ data-testid='containers_client_finances_balance-adjustment_new-amount']"
	)
	btn_mobile_invoice_adjust_css = "*[data-testid='containers_client_finances_adjust-button']"
	new_amount_charged_xpath = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/span[1]/span[1]"
	)
	mobile_amount_charged_xpath = (
		"//*[@data-testid='components_common_table-wrapper-mobile']/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/span[1]/span"
	)
	tab_mobile_client_record_payment_id = "containers_client_navigation_record-payment_mobile"
	tab_mobile_client_balance_xpath = (
		"//ul[@data-testid='containers_client_finances_mobile-drawer-content']/li[1]/a/div/span/span/span"
	)
	sel_mobile_workflow_attendance_session_xpaths = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div"
	)
	btn_mobile_workflow_attedance_xpath = "//button[normalize-space()='Mark Attendance']"
	tab_mobile_client_navigation_create_invoice_id = "containers_client_navigation_create-invoice_mobile"
	tab_mobile_first_invoice_number_xpath = "//*[@data-testid='components_common_table-wrapper-mobile']/div[1]/div[1]/div[1]"

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)

	def clk_tab_receipts(self):
		self.click("XPATH", self.tab_receipts_xpath)

	def clk_tab_client_navigation_finances(self):
		self.click("CSS_SELECTOR", self.tab_client_navigation_finances_css)

	def clk_tab_invoices(self):
		self.click("XPATH", self.tab_invoices_xpath)

	def clk_tab_refunds(self):
		self.click("XPATH", self.tab_refunds_xpath)

	def clk_tab_non_session_charges(self):
		self.click("XPATH", self.tab_non_session_charges_xpath)

	def clk_btn_add_item(self):
		self.click("CSS_SELECTOR", self.btn_add_item_css)

	def clk_tab_record_payment(self):
		self.click("ID", self.tab_record_payment_id)

	def input_payment_amount(self, payment_amount):
		self.enter("XPATH", self.txt_payment_amount_xpath, Keys.CLEAR)
		self.enter("XPATH", self.txt_payment_amount_xpath, payment_amount)

	def sel_payment_type(self, payment_method):
		self.click("XPATH", self.dd_payment_type_control_xpath)
		self.enter("XPATH", self.dd_payment_type_input_xpath, payment_method)
		#sleep(0.5)
		self.click("XPATH", "//div[contains(@class,'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", payment_method))

	def input_confirmation_number(self, confirmation_number):
		self.enter("CSS_SELECTOR", self.txt_confirmation_number_css, confirmation_number)

	def clk_record_payment(self):
		self.click("XPATH", self.btn_record_payment_xpath)

	def clk_generate_credit_btn(self):
		self.click("XPATH", self.btn_generate_credit_xpath)

	def clk_close_pdf_preview(self):
		self.click("XPATH", self.btn_close_pdf_preview_xpath)

	def get_confirmation_number_of_receipt(self):
		self.wait_for_element_visibility("XPATH", self.receipt_xpaths)
		no_of_receipts = self.get_length(self.receipt_xpaths)
		confirmation_number_list = []
		for i in range(1, no_of_receipts + 1):
			confirmation_number_x =self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[7]")
			confirmation_number_list.append(confirmation_number_x)
		return confirmation_number_list

	def number_of_receipts(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_receipts = self.get_length(self.receipt_xpaths)
		return no_of_receipts

	def select_first_receipt(self):
		self.click("XPATH", self.first_receipt_xpath)

	def clk_delete_receipt(self):
		self.click("XPATH", self.btn_delete_receipt_xpath)

	def clk_delete_receipt_confirm(self):
		self.click("XPATH", self.btn_delete_receipt_confirm_xpath)

	def clk_account_details(self):
		self.click("CSS_SELECTOR", self.tab_account_details_css)

	def clk_edit_account_details(self):
		self.click("XPATH", self.btn_edit_account_details_xpath)

	def sel_payment_term(self, payment_term):
		self.click("XPATH", self.dd_payment_term_control_xpath)
		self.enter("XPATH", self.dd_payment_term_input_xpath, payment_term)
		self.click("XPATH", "//div[contains(@class,'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", payment_term))

	def clk_save_account_details(self):
		self.click("XPATH", self.btn_save_acount_details_xpath)

	def clk_mark_attendance_sesison(self):
		sleep(2)
		self.click("CSS_SELECTOR", self.btn_mark_attendance_css)

	def clk_session_attended(self):
		self.click("CSS_SELECTOR", self.btn_session_attended_css)

	def check_session_status(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='containers_client_session-notes_table-body']")
		no_of_sessions = self.get_length(self.sel_session_xpaths)
		sessions_name_list = []
		for i in range(1, no_of_sessions + 1):
			sessions_name_x = self.get_text("XPATH", "//div[@data-testid='containers_client_session-notes_table-body']/div[" + str(i) + "]/div[2]")
			sessions_name_list.append(sessions_name_x)
			if sessions_name_x == date_1:
				select_sessions_xpath = "//div[@data-testid='containers_client_session-notes_table-body']/div[" + str(i) + "]/div[7]"
				sleep(1)
				session_status = self.get_text("XPATH", select_sessions_xpath)
				break
			else:
				continue
		return session_status

	def get_no_of_invoices(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_invoices = self.get_length(self.invoices_xpaths)
		return no_of_invoices

	def select_first_invoice(self):
		self.click("XPATH", self.first_invoice_xpath)

	def clk_delete_client_invoice(self):
		self.click("CSS_SELECTOR", self.btn_delete_client_invoice_css)

	def clk_delete_confirm_client_invoice(self):
		self.click("CSS_SELECTOR", self.btn_delete_confirm_client_invoice_css)

	def clk_client_navigation_create_invoice(self):
		self.click("ID", self.tab_client_navigation_create_invoice_id)

	def input_start_date_search_invoice(self, start_date):
		txt_invoice_date_range_start_date_element = self.wait.until(EC.visibility_of_element_located(
			(By.XPATH, self.txt_invoice_date_range_start_date_xpath))
		)
		txt_invoice_date_range_start_date_element_text = (
			txt_invoice_date_range_start_date_element.get_attribute('value')
		)
		len_date_time = len(txt_invoice_date_range_start_date_element_text)
		for x in range(len_date_time):
			txt_invoice_date_range_start_date_element.send_keys(Keys.BACKSPACE)
			sleep(0.1)
		sleep(0.5)
		self.enter("XPATH", self.txt_invoice_date_range_start_date_xpath, start_date)

	def clk_create_invoice_find_session_range(self):
		self.click("CSS_SELECTOR", self.btn_create_invoice_find_session_range_css)

	def clk_create_invoice_btn(self):
		self.click("CSS_SELECTOR", self.btn_create_invoice_css)

	def clk_client_invoice_pdf_preview_close(self):
		self.click("CSS_SELECTOR", self.btn_client_invoice_pdf_preview_close_css)

	def sel_invoice_number(self, invoice_number):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_invoices = self.get_length(self.sel_invoices_xpaths)
		invoice_number_list = []
		for i in range(1, no_of_invoices + 1):
			invoice_number_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[3]")
			invoice_number_list.append(invoice_number_x)
			if invoice_number_x == invoice_number:
				select_invoice_xpath = "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]"
				sleep(1)
				self.click("XPATH", select_invoice_xpath)
				break
			else:
				continue

	def sel_invoice_date(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_invoices = self.get_length(self.sel_invoices_xpaths)
		invoice_list = []
		for i in range(1, no_of_invoices + 1):
			invoice_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[2]")
			invoice_list.append(invoice_x)
			if invoice_x == date_1:
				select_invoice_xpath = "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]"
				sleep(1)
				self.click("XPATH", select_invoice_xpath)
				break
			else:
				continue

	def list_of_invoices(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_invoices = self.get_length(self.sel_invoices_xpaths)
		invoice_number_list = []
		for i in range(1, no_of_invoices + 1):
			invoice_number_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[6]")
			invoice_number_list.append(invoice_number_x)
		return invoice_number_list

	def get_message_delete_invoiced_session(self):
		error_message = self.get_text("XPATH", self.text_message_delete_invoiced_session_xpath)
		return error_message

	def input_non_session_charge_billable_name(self, service_name):
		self.enter("NAME", self.txt_non_session_chage_billable_name, service_name)

	def input_non_session_charge_date(self, date):
		self.enter("XPATH", self.txt_non_session_charge_date_xpath, date)

	def sel_therapist(self, therapist):
		self.click("XPATH", self.dd_non_session_charge_therapist_xpath)
		self.enter("XPATH", self.dd_non_session_charge_therapist_name_xpath, therapist)
		self.enter("XPATH", self.dd_non_session_charge_therapist_name_xpath, Keys.RETURN)

	def input_non_session_charge_amount(self, amount):
		self.click("CSS_SELECTOR", self.txt_non_session_charge_amount_css)
		self.enter_withoutclear("CSS_SELECTOR", self.txt_non_session_charge_amount_css, amount)

	def clk_autoinvoice_yes(self):
		self.click("XPATH", self.btn_autoinvoice_yes_xpath)

	def clk_autoinvoice_no(self):
		self.click("XPATH", self.btn_autoinvoice_no_xpath)

	def clk_non_session_charge_save(self):
		self.click("XPATH", self.btn_non_session_charge_save_xpath)

	def list_of_non_session_charges(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_non_session_charges = self.get_length(self.sel_non_session_charges_xpaths)
		non_session_charges_list = []
		for i in range(1, no_of_non_session_charges + 1):
			non_session_charges_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[5]")
			non_session_charges_list.append(non_session_charges_x)
		return non_session_charges_list

	def check_status_non_session_charges(self, service_name):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_non_session_charges = self.get_length(self.sel_non_session_charges_xpaths)
		for i in range(1, no_of_non_session_charges + 1):
			non_session_charges_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[5]")
			if non_session_charges_x == service_name:
				nsn_status = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[8]")
			break
		return nsn_status

	def clk_client_invoice_view(self):
		self.click("CSS_SELECTOR", self.btn_client_view_invoice_css)

	def clk_pdf_preview_add_email(self, email_id):
		self.click("XPATH", self.tab_pdf_preview_add_email_xpath)

	def clk_pdf_preview_send_email(self):
		self.click("CSS_SELECTOR", self.btn_pdf_preview_send_email_css)

	def get_first_invoice_number(self):
		invoice_number = self.get_text("XPATH", self.first_invoice_number_xpath)
		return invoice_number

	def clk_client_invoice_adjust(self):
		self.click("CSS_SELECTOR", self.btn_client_adjust_invoice_css)

	def input_reason_for_invoice_adjustment(self, adjustment_reason):
		self.enter("XPATH", self.txt_reason_for_adjustment_xpath, adjustment_reason)

	def input_new_adjusted_amount(self, adjusted_amount):
		self.click("XPATH", self.txt_new_adjusted_amount_xpath)
		self.enter("XPATH", self.txt_new_adjusted_amount_xpath, adjusted_amount)

	def clk_invoice_adjust_button(self):
		self.click("XPATH", self.btn_client_adjust_invoice_xpath)

	def clk_client_invoice_balance_adjust_close(self):
		self.click("CSS_SELECTOR", self.btn_client_invoice_balance_adjust_close_css)

	def get_selected_invoice_amount_charged(self):
		amount_charged = self.get_text("XPATH", self.selected_invoice_amount_charged_xpath)
		return amount_charged

	def clk_pdf_preview_refund(self):
		self.click("CSS_SELECTOR", self.btn_pdf_preview_refund_css)

	def input_client_invoice_refund_confirmation_number(self, confirmation_number):
		self.enter("NAME", self.txt_inovice_refund_confirmation_number_name, confirmation_number)

	def input_client_invoice_refund_amount(self, refund_amount):
		self.enter("XPATH", self.txt_client_invoice_refund_amount_xpath, refund_amount)

	def clk_client_invoice_refund_payment(self):
		self.click("XPATH", self.btn_client_invoice_refund_payment_xpath)

	def clk_client_invoice_confirm_refund(self):
		self.click("CSS_SELECTOR", self.btn_forms_refund_payment_refund_css)

	def list_of_refunds(self, invoice_number):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_refunds = self.get_length(self.sel_refunds_xpaths)
		refunds_number_list = []
		for i in range(1, no_of_refunds + 1):
			refund_number_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[2]/div[" + str(i) + "]/div[7]")
			refunds_number_list.append(refund_number_x)
		return refunds_number_list

	def input_client_account_details_global_discount(self, global_discount):
		self.enter("XPATH", self.txt_client_account_details_global_discount_xpath, Keys.CLEAR)
		self.enter("XPATH", self.txt_client_account_details_global_discount_xpath, global_discount)

	def sel_session_charge(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='containers_client_session-notes_table-body']")
		no_of_notes = self.get_length(self.sel_session_notes_xpaths)
		notes_name_list = []
		for i in range(1, no_of_notes + 1):
			note_name_x = self.get_text("XPATH", "//div[@data-testid='containers_client_session-notes_table-body']/div[" + str(i) + "]/div[2]")
			notes_name_list.append(note_name_x)
			if note_name_x == date_1:
				select_note_xpath = "//div[@data-testid='containers_client_session-notes_table-body']/div[" + str(i) + "]/div[6]"
				sleep(2)
				amount_charged = self.get_text("XPATH", select_note_xpath)
				break
		return amount_charged

	def sel_session_status(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='containers_client_session-notes_table-body']")
		no_of_notes = self.get_length(self.sel_session_notes_xpaths)
		notes_name_list = []
		for i in range(1, no_of_notes + 1):
			note_name_x = self.get_text("XPATH", "//div[@data-testid='containers_client_session-notes_table-body']/div[" + str(i) + "]/div[2]")
			notes_name_list.append(note_name_x)
			if note_name_x == date_1:
				select_note_xpath = "//div[@data-testid='containers_client_session-notes_table-body']/div[" + str(i) + "]/div[7]"
				sleep(1)
				session_status = self.get_text("XPATH", select_note_xpath)
				break
		return session_status

	def get_client_account_credit_balance(self):
		credit_balance = self.get_text("XPATH", self.tab_client_credit_balance_xpath)
		return credit_balance

	def get_client_account_balance(self):
		account_balance = self.get_text("XPATH", self.tab_client_balance_xpath)
		return account_balance
	'''
	def uncheck_use_account_credit(self):
		cb_record_payment_use_account_credit_element = self.wait.until(EC.presence_of_element_located(
			(By.XPATH, self.cb_record_payment_use_account_credit_xpath))
		)
		if cb_record_payment_use_account_credit_element.is_selected() = false:
	'''
	def number_of_non_session_charge(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_table']/div[2]")
		no_of_non_session_charge = self.get_length(self.sel_non_session_charge_xpaths)
		return no_of_non_session_charge

	def sel_first_non_session_charge(self):
		self.click("XPATH", self.sel_first_non_session_charge_xpath)

	def clk_delete_non_session_charge(self):
		self.click("XPATH", self.btn_delete_non_session_charge_xpath)

	def clk_delete_charge_non_session_charge(self):
		self.click("XPATH", self.btn_delete_charge_non_session_charge_xpath)

	def input_allocate_manually_payment_1(self, payment_amount_1):
		self.enter("XPATH", self.txt_allocate_manually_payment_1_xpath, payment_amount_1)

	def input_allocate_manually_payment_2(self, payment_amount_2):
		self.enter("XPATH", self.txt_allocate_manually_payment_2_xpath, payment_amount_2)

	def clk_mobile_record_payment(self):
		#self.scroll("ID", self.tab_mobile_record_payment_id)
		self.hover("ID", self.tab_mobile_record_payment_id)
		self.click_js("ID", self.tab_mobile_record_payment_id)
		# self.driver.execute_script("arguments[0].scrollIntoView();", tab_mobile_record_payment_element)
		# self.driver.execute_script("arguments[0].click();", tab_mobile_record_payment_element)

	def clk_client_contact_clinical_account_details(self):
		self.click("CSS_SELECTOR", self.tab_client_contact_clinical_account_details_css)

	def clk_client_contact_clinical_acount_details_edit(self):
		self.click("CSS_SELECTOR", self.btn_client_account_details_edit_css)

	def input_payment_terms(self, payment_term):
		self.click("XPATH", self.dd_payment_terms_xpath)
		self.enter("XPATH", self.input_payment_terms_xpath, payment_term)
		self.enter("XPATH", self.input_payment_terms_xpath, Keys.RETURN)

	def clk_client_account_details_save(self):
		self.click("CSS_SELECTOR", self.btn_client_account_details_save_css)

	def input_mobile_client_global_discount(self, global_discount):
		self.enter("XPATH", self.txt_mobile_client_global_discount_xpath, global_discount)

	def return_mobile_no_of_invoices(self):
		self.wait_for_element_visibility("XPATH",  "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_invoices = self.get_length(self.no_of_invoices_xpath)
		return no_of_invoices

	def clk_mobile_invoice(self):
		self.click("XPATH", self.first_mobile_invoice_xpath)

	def clk_mobile_invoice_delete(self):
		self.click("CSS_SELECTOR", self.btn_mobile_invoice_delete_css)

	def clk_mobile_invoice_delete_confirm(self):
		self.click("CSS_SELECTOR", self.btn_mobile_invoice_delete_confirm_css)
		# self.driver.execute_script("arguments[0].click();", btn_mobile_invoice_delete_confirm_element)

	def clk_mobile_mark_attendance(self):
		self.click("CSS_SELECTOR", self.btn_mobile_session_mark_attendance_css)

	def mobile_get_status_session(self):
		status_session = self.get_text("XPATH", self.mobile_session_status_xpath)
		return status_session

	def clk_allocate_payment_manually(self):
		self.click("XPATH", self.cb_record_payment_manually_xpath)

	def clk_mobile_client_navigation_finance(self):
		self.click("CSS_SELECTOR", self.tab_mobile_client_navigation_finance_css)

	def clk_mobile_client_action_record_payment(self):
		self.click("CSS_SELECTOR", self.btn_mobile_client_actions_record_payment_css)

	def mobile_no_of_receipts(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_receipts = self.get_length(self.sel_mobile_client_receipts_xpaths)
		return no_of_receipts

	def sel_mobile_first_receipt(self):
		self.click("XPATH", self.mobile_first_receipt_xpath)

	def mobile_client_receipts_list(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_receipts = self.get_length(self.sel_mobile_client_receipts_xpaths)
		receipts_number_list = []
		for i in range(1, no_of_receipts + 1):
			receipt_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
			self.click("XPATH", receipt_xpath)
			receipt_number_xpath = (
				"//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[2]/div[1]/div[1]/div[1]/div[4]")
			receipt_number_x = self.get_text("XPATH", receipt_number_xpath)
			receipts_number_list.append(receipt_number_x)
		return receipts_number_list

	def select_mobile_client_receipt(self, receipt_number):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_receipts = self.get_length(self.sel_mobile_client_receipts_xpaths)
		receipts_number_list = []
		for i in range(1, no_of_receipts + 1):
			receipt_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
			self.click("XPATH", receipt_xpath)
			receipt_number_xpath = (
				"//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[2]/div[1]/div[1]/div[1]/div[4]")
			receipt_number_x = self.get_text("XPATH", receipt_number_xpath)
			receipts_number_list.append(receipt_number_x)
			if receipt_number_x == receipt_number:
				self.click("XPATH", receipt_number_xpath)
				# self.driver.execute_script("arguments[0].click();", select_note_element)
				break
			else:
				continue

	def sel_mobile_first_non_session_charge(self):
		self.click("XPATH", self.mobile_first_non_session_charge_xpath)

	def mobile_no_of_non_session_charges(self):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_non_session_charges = self.get_length(self.mobile_non_session_charge_xpaths)
		return no_of_non_session_charges

	def clk_mobile_delete_non_session_charge(self):
		self.click("CSS_SELECTOR", self.btn_mobile_delete_non_session_charge_css)

	def clk_mobile_delete_confirm_non_session_charge(self):
		self.click("CSS_SELECTOR", self.btn_mobile_delete_confirm_non_session_charge_css)

	def clk_mobile_add_item(self):
		self.click("CSS_SELECTOR", self.btn_mobile_add_item_css)

	def sel_mobile_invoice_date(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_invoices = self.get_length(self.no_of_invoices_xpath)
		invoice_list = []
		for i in range(1, no_of_invoices + 1):
			invoice_x = self.get_text("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[1]/div[2]")
			invoice_list.append(invoice_x)
			if invoice_x == date_1:
				select_invoice_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
				sleep(1)
				self.click("XPATH", select_invoice_xpath)
				break
			else:
				continue

	def input_mobile_invoice_adjust_amount(self, new_amount):
		self.enter("CSS_SELECTOR", self.txt_mobile_invoice_adjust_amount_css, new_amount)

	def clk_mobile_invoice_adjust(self):
		self.click("CSS_SELECTOR", self.btn_mobile_invoice_adjust_css)

	def get_mobile_new_amount_charged(self):
		new_amount_charged = self.get_text("XPATH", self.new_amount_charged_xpath)
		return new_amount_charged

	def sel_mobile_nsn_charge_date(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		mobile_no_of_nsn_charges = self.get_length(self.mobile_non_session_charge_xpaths)
		nsn_charges_list = []
		for i in range(1, mobile_no_of_nsn_charges + 1):
			nsn_charges_x = self.get_text("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[1]/div[2]")
			nsn_charges_list.append(nsn_charges_x)
			if nsn_charges_x == date_1:
				select_nsn_charge_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
				sleep(1)
				self.click("XPATH", select_nsn_charge_xpath)
				nsn_status_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[2]/div[1]/div[1]/div[1]/div[4]/span"
				nsn_status = self.get_text("XPATH", nsn_status_xpath)
				break
			else:
				continue
		return nsn_status

	def get_mobile_amount_charged(self):
		mobile_amount_charged = self.get_text("XPATH", self.mobile_amount_charged_xpath)
		return mobile_amount_charged

	def clk_mobile_client_record_payment(self):
		self.click("ID", self.tab_mobile_client_record_payment_id)

	def get_mobile_client_balance(self):
		act_client_balance = self.get_text("XPATH", self.tab_mobile_client_balance_xpath)
		return act_client_balance

	def select_mobile_non_session_note(self, date_1):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_sessions = self.get_length(self.sel_mobile_workflow_attendance_session_xpaths)
		sessions_name_list = []
		for i in range(1, no_of_sessions + 1):
			session_name_x = self.get_text("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div[1]/div[2]")
			sessions_name_list.append(session_name_x)
			if session_name_x == date_1:
				select_session_xpath = "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]"
				sleep(1)
				self.click("XPATH", select_session_xpath)
				# self.driver.execute_script("arguments[0].click();", select_note_element)
				break
			else:
				continue

	def clk_mobile_workflow_attendance(self):
		self.click("XPATH", self.btn_mobile_workflow_attedance_xpath)

	def clk_mobile_client_navigation_create_invoice(self):
		self.click("ID", self.tab_mobile_client_navigation_create_invoice_id)

	def get_mobile_first_invoice_number(self):
		invoice_number = self.get_text("XPATH", self.tab_mobile_first_invoice_number_xpath)
		return invoice_number
