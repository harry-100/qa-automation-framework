# Locators of Login Page
from selenium.webdriver.support.ui import WebDriverWait
from utilities.BasePage import BasePage


class LoginPage(BasePage):
	txt_username_name = "username"
	txt_password_name = "password"
	btn_sign_in_css = "*[data-testid='containers_login_sign-in']"

	btn_top_menu_more_action_css = "*[data-testid='containers_top-menu_actions_more-options']"
	btn_sign_out_css = "*[data-testid='components_client-action-menu_sign-out']"
	btn_back_to_signin_xpath = "//button[@type='button' and contains(.,'Back to Sign In')]"

	btn_navigation_css = "*[data-testid='containers_top-menu_side-menu_toogle_mobile']"
	btn_calendar_css = "*[data-testid='components_side-menu_navigation_calendar']"
	btn_clients_css = "*[data-testid='components_side-menu_navigation_clients']"
	btn_workflow_css = "*[data-testid='components_side-menu_navigation_workflow']"
	btn_messaging_css = "*[data-testid='components_side-menu_navigation_messaging']"
	btn_dashboard_css = "*[data-testid='components_side-menu_navigation_dashboard']"
	btn_manage_css = "*[data-testid='components_side-menu_navigation_manage']"
	btn_settings_css = "*[data-testid='components_side-menu_navigation_settings']"
	btn_help_css = "*[data-testid='components_side-menu_navigation_help']"
	btn_mobile_calendar_css = "*[data-testid='components_mobile-side-menu_calendar_mobile']"
	btn_mobile_forms_css = "*[data-testid='components_mobile-side-menu_manage-forms_mobile']"
	#btn_mobile_notes_css = "*[data-testid='containers_workflow_navigation_notes']"
	btn_mobile_workflow_notes_css = (
		"*[data-testid='components_mobile-side-menu_workflow-notes_mobile']"
	)
	btn_mobile_manage_hadnwritten_notes_css = (
		"*[data-testid='components_mobile-side-menu_manage-handwritten-notes_mobile']"
	)
	btn_mobile_workflow_attendance_css = (
		"*[data-testid='components_mobile-side-menu_workflow-attendance_mobile']"
	)
	btn_mobile_settings_practice_details_css = (
		"*[data-testid='components_mobile-side-menu_settings-practice-details_mobile']"
	)
	btn_mobile_waitlist_clients_css = (
		"*[data-testid='components_mobile-side-menu_clients-undefined_mobile']"
	)
	btn_mobile_client_prospects_css = (
		"*[data-testid='components_mobile-side-menu_clients-prospects_mobile']"
	)

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)

	def set_username(self, username):
		self.enter("NAME", self.txt_username_name, username)

	def set_password(self, password):
		self.enter("NAME", self.txt_password_name, password)

	def click_sign_in(self):
		self.click("CSS_SELECTOR", self.btn_sign_in_css)

	def clk_top_menu_more_action(self):
		self.click("CSS_SELECTOR", self.btn_top_menu_more_action_css)

	def clk_sign_out(self):
		self.click("CSS_SELECTOR", self.btn_sign_out_css)

	def clk_back_to_signin(self):
		self.click("XPATH", self.btn_back_to_signin_xpath)

	def clk_navigation_btn(self):
		self.click("CSS_SELECTOR", self.btn_navigation_css)

	def clk_calendar_btn(self):
		self.click("CSS_SELECTOR", self.btn_calendar_css)

	def clk_clients_btn(self):
		self.click("CSS_SELECTOR", self.btn_clients_css)

	def clk_workflow_btn(self):
		self.click("CSS_SELECTOR", self.btn_workflow_css)

	def clk_messaging_btn(self):
		self.click("CSS_SELECTOR", self.btn_messaging_css)

	def clk_dashboard_btn(self):
		self.click("CSS_SELECTOR", self.btn_dashboard_css)

	def clk_manage_btn(self):
		self.click("CSS_SELECTOR", self.btn_manage_css)

	def clk_settings_btn(self):
		self.click("CSS_SELECTOR", self.btn_settings_css)

	def clk_help_btn(self):
		self.click("CSS_SELECTOR", self.btn_help_css)

	def clk_mobile_forms_btn(self):
		self.click("CSS_SELECTOR", self.btn_mobile_forms_css)

	def clk_mobile_workflow_notes_btn(self):
		self.click("CSS_SELECTOR", self.btn_mobile_workflow_notes_css)

	def clk_manage_handwritten_notes_btn(self):
		self.click("CSS_SELECTOR", self.btn_mobile_manage_hadnwritten_notes_css)

	def clk_mobile_calendar(self):
		self.click("CSS_SELECTOR", self.btn_mobile_calendar_css)

	def clk_mobile_workflow_attendance(self):
		self.click("CSS_SELECTOR", self.btn_mobile_workflow_attendance_css)

	def clk_mobile_settings_practice_details(self):
		self.click("CSS_SELECTOR", self.btn_mobile_settings_practice_details_css)

	def clk_mobile_waitlist_clients(self):
		self.click("CSS_SELECTOR", self.btn_mobile_waitlist_clients_css)

	def clk_mobile_client_prospects(self):
		self.click("CSS_SELECTOR", self.btn_mobile_client_prospects_css)

	