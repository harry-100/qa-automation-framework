from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities.BasePage import BasePage


class CalendarPage(BasePage):

	btn_add_session_css = "*[data-testid='containers_calendar_new-session']"

	# elements on form for creating sessions
	dd_event_type_xpath = "//div[@id='forms_session_client_event-type']/div/div[2]"

	dd_event_option_xpath = (
		"//div[@id='forms_session_client_event-type']/div[1]/div[1]/div[2]/div[1]/input[1]"
	)
	txt_event_name_css = "*[data-testid='forms_session_personal_event-name']"
	txt_client_name_css = "*[data-testid='forms_session_client_client-name']"
	dd_therapist_xpath = "//div[@id='forms_session_client_therapist']/div/div[2]"

	dd_therapist_name_xpath = (
		"//div[@id='forms_session_client_therapist']/div[1]/div[1]/div[2]/div[1]/input[1]"
	)
	txt_date_time_css = "*[data-testid='forms_session_client_date-picker_start']"

	dd_service_xpath = "//*[@id='forms_session_client_service']/div/div[2]"
	dd_service_type_id = "forms_session_client_service"
	dd_service_type_xpath = (
		"//*[@id='forms_session_client_service']/div[1]/div[1]/div[2]/div[1]/input[1]"
	)

	txt_start_date_css = "*[data-testid='forms_session_personal_date-picker_start']"
	txt_end_date_css = "*[data-testid='forms_session_personal_date-picker_end']"

	dd_room_xpath = "//*[@id='forms_session_client_room']/div/div[2]"
	dd_room_type_xpath = "//*[@id='forms_session_client_room']//div[1]/div[1]/div[2]/div[1]/input[1]"
	txt_amount_id = "forms_session_client_amount-charged"
	btn_create_session_css = "*[data-testid='containers_session-controller_create-session_create']"
	tbl_sessioninfo_xpath = (
		"//*[@id='fullcalendar']/div[2]/div/table/tbody/tr/td/div[2]/div/div[3]/table/tbody/tr/td[*]/"
		"div/div[2]/a/div"
	)
	session_details_css = "*[data-testid='components_session-overview_client_session-details']"
	btn_more_information_css = (
		"*[data-testid='components_session-overview_client_information']"
	)
	btn_mobile_more_information_css = (
		"*[data-testid='components_session-overview_mobile_client_information']"
	)
	btn_personal_more_information_css = (
		"*[data-testid='components_session-overview_personal_information']"
	)
	btn_mobile_personal_more_information_css = (
		"*[data-testid='components_session-overview_mobile_personal_information']"
	)

	btn_update_session_css = (
		"*[data-testid='containers_session-controller_update-session_update']"
	)

	btn_delete_session_css = "*[data-testid='containers_session-controller_update-session_delete']"
	btn_delete_session_warn_css = (
		"*[data-testid='containers_session-controller_warning-delete-session_delete']"
	)

	tbl_calendar_week_xpaths = (
		"//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th"
	)
	btn_day_view_css = "*[data-testid='containers_calendar_toolbar_menu_day']"
	btn_week_view_css = "*[data-testid='containers_calendar_toolbar_menu_week']"
	btn_room_view_css = "*[ data-testid='containers_calendar_toolbar_menu_rooms']"
	btn_move_to_next_week_css = "*[data-testid='containers_calendar_toolbar_menu_nav_right']"
	btn_move_to_previous_week_css = "*[data-testid='containers_calendar_toolbar_menu_nav-left']"
	btn_calendar_option_xpath = "//*[@id='app']/span/div[2]/div[1]/a[1]/div"
	tbl_calendar_day_xpath = (
		"//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th[2]"
	)
	tbl_calendar_week_xpaths = (
		"//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th/a"
	)
	tbl_room_view_xpaths = (
		"//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th"
	)

	btn_hidden_days_css = (
		"*[data-testid='containers_calendar_toolbar_menu_mobile_open-calendar-settings']"
	)

	btn_apply_settings_xpath = "//button[contains(text(),'Apply Settings')]"
	btn_therapist_availability_css = "*[data-testid='containers_calendar_toolbar_menu_availability']"
	tbl_therapist_view_xpaths = (
		"//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th"
	)
	btn_calendar_month_view_css = "*[data-testid='containers_calendar_toolbar_menu_month']"
	txt_month_view_info_css = "*[data-testid='containers_calendar_toolbar_menu_nav-date']"

	# Mobile Elements
	sdd_event_type_id = "forms_session_client_event-type"
	sdd_therapist_id = "forms_session_client_therapist"
	sdd_service_id = "forms_session_client_service"
	sdd_room_id = "forms_session_client_room"
	sdd_recurrence_id = "forms_session_client_recurrence"

	btn_calendar_view_xpath = (
		"//*[@id='app']/span/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/div[3]/span[1]/span/button"
	)
	btn_calendar_view_css = "*[data-testid='containers_calendar_toolbar_menu_mobile_menu-open']"
	btn_calendar_week_view_css = "*[data-testid='components_client-action-menu_week']"
	btn_calendar_day_view_css = "*[data-testid='containers_calendar_toolbar_menu_mobile_day']"

	btn_more_info_mobile_css = (
		"[data-testid = 'components_session-overview_mobile_client_information']"
	)
	tbl_mobile_calendar_day_xpath = (
		"//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr"
	)
	tab_mobile_calendar_xpath = "//span[contains(text(),'Calendar')]"
	btn_mobile_client_session_details_xpath = (
		"//*[@id='app']/span/div[2]/div[2]/div[2]/div/div/div[2]/div[2]"
		"/div/div/div[2]/div[2]/div/div[1]"
	)
	btn_mobile_client_delete_session_xpath = (
		"//*[@id='app']/span/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div[2]/"
		"div[2]/div/div[2]/div/div/div[2]/button[3]"
	)
	btn_mobile_client_confirm_delete_session_xpath = "//button[contains(text(),'Delete Session')]"

	btn_mobile_calendar_month_view_css = (
		"*[data-testid='components_client-action-menu_month']"
	)

	btn_mobile_calendar_room_view_css = (
		"*[data-testid='containers_calendar_toolbar_menu_mobile_rooms']")

	btn_mobile_calendar_therapist_view_css = (
		"*[data-testid='components_client-action-menu_availability']")

	btn_mobile_calendar_day_view_css = (
		"*[data-testid='components_client-action-menu_day']")

	tab_all_day_session_xpath = (
		"//*[@id='fullcalendar']/div[2]/div/table/tbody/tr/td/div[1]/div/div[2]/table/tbody/tr/td[6]"
	)
	tab_personal_session_details_css = (
		"*[data-testid='components_session-overview_personal_session-details']"
	)
	tab_mobile_client_session_xpath = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div[1]"
	)
	btn_mobile_client_view_session_css = (
		"*[data-testid='containers_client_sessions-notes_sessions_view-session_mobile']"
	)
	tab_mobile_personal_session_details_xpath = (
		"/html/body/div[*]/div/div[2]/div/div[1]/div[2]/span[1]"
	)
	discount_value_css = "*[data-testid='forms_session_client_fee-discount']"

	btn_appointment_delete_confirm_css = (
		"*[data-testid='containers_session-controller_warning_appointment_delete_confirm']"
	)
	mobile_session_details_css = (
		"*[data-testid='components_session-overview_client_session-details']"
	)
	tab_calendar_today_css = "*[data-testid='containers_calendar_toolbar_menu_today']"
	btn_session_delete_appointment_confirm_css = (
		"*[data-testid='containers_session-controller_warning_appointment_delete_confirm']"
	)
	all_day_session_css = "*[data-testid='forms_session_personal_checkbox-all-day']"
	all_day_session_xpath = "//div[@data-testid='forms_session_personal_checkbox-all-day']/div[1]/div[1]"
	tab_mobile_jump_to_today_css = "*[data-testid='components_client-action-menu_jump-to-today']"
	tab_date_info_css = "*[data-testid='containers_calendar_toolbar_menu_nav-date']"
	tab_client_session_list_xpaths = (
		"//div[@data-testid='components_common_table-wrapper-mobile']/div"
	)
	#all_day_session_slot_xpath = (
	#	"//*[@id='fullcalendar']/div[2]/div/table/tbody/tr/td/div[1]/div/div[1]/table/tbody/tr/td[2]"
	#)
	all_day_session_slot_xpath = (
		"//*[@id='fullcalendar']/div[2]/div/table/tbody/tr/td/div[1]/div/div[2]"
	)
	all_day_session_info_xpath = "//div[contains(text(), 'Research')]"
	btn_create_all_day_session_xpath = "//button[@type='button' and contains(.,'Create Session')]"
	btn_read_only_delete_session_css = (
		"*[data-testid='containers_session-controller_read-only-view_delete']"
	)
	tab_session_for_delete_xpath = (
		"//div[contains(@class,'EventContent__Title')]//span[text()='9:00am']"
	)
	check_video_session_xpath = "//div[@title='Video session']"

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)

	def click_add_session(self):
		self.click("CSS_SELECTOR", self.btn_add_session_css)
	'''
	def input_clientname(self, client_name):
		self.click("CSS_SELECTOR", self.txt_client_name_css)
		sleep(0.5)
		self.enter_character("CSS_SELECTOR", self.txt_client_name_css, client_name)
		self.enter("CSS_SELECTOR", self.txt_client_name_css, Keys.RETURN)
	'''
	def input_clientname(self, client_name):
		self.click("CSS_SELECTOR", self.txt_client_name_css)
		sleep(0.5)
		self.enter("CSS_SELECTOR", self.txt_client_name_css, client_name)
		self.click("XPATH", "//span[contains(@class, 'ClientCodeBlock__ClientName') and text()='OPTION_VALUE']".replace("OPTION_VALUE", client_name))
	#	self.enter("CSS_SELECTOR", self.txt_client_name_css, Keys.RETURN)

	def sel_event_type(self, event_type):
		self.click("XPATH", self.dd_event_type_xpath)
		self.enter("XPATH", self.dd_event_option_xpath, event_type)
		self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", event_type))

	def input_event_name(self, event_name):
		self.click("CSS_SELECTOR", self.txt_event_name_css)
		self.enter("CSS_SELECTOR", self.txt_event_name_css, event_name)

	def sel_therapist(self, therapist):
		self.click("XPATH", self.dd_therapist_xpath)
		self.enter("XPATH", self.dd_therapist_name_xpath, therapist)
		self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", therapist))

	def txt_start_date(self, start_date):
		self.clear_field("CSS_SELECTOR", self.txt_start_date_css)
		self.enter("CSS_SELECTOR", self.txt_start_date_css, start_date)

	def txt_end_date(self, end_date):
		self.clear_field("CSS_SELECTOR", self.txt_end_date_css)
		self.enter("CSS_SELECTOR", self.txt_end_date_css, end_date)
	'''
	def txt_date_time(self, date_time):
		self.clear_field("CSS_SELECTOR", self.txt_date_time_css)
		self.click("CSS_SELECTOR", self.txt_date_time_css)
		self.enter("CSS_SELECTOR", self.txt_date_time_css, date_time)
	'''
	def txt_date_time(self, date_time):
		self.click("CSS_SELECTOR", self.txt_date_time_css)
		sleep(0.5)
		date_element = self.wait_for_element_visibility("CSS_SELECTOR", self.txt_date_time_css)
		#self.driver.execute_script("arguments[0].value= '';", date_element)
		#self.driver.execute_script("arguments[0].value= '" + date_time + "';", date_element)
		self.clear_field("CSS_SELECTOR", self.txt_date_time_css)
		self.click("CSS_SELECTOR", self.txt_date_time_css)
		self.enter("CSS_SELECTOR", self.txt_date_time_css, date_time)
		
	def sel_service(self, service):
		self.click("XPATH", self.dd_service_xpath)
		self.click("XPATH", "//div[contains(@class,'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", service))

	def sel_room(self, room):
		self.click("XPATH", self.dd_room_xpath)
		self.click("XPATH", "//div[contains(@class,'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", room))

	def get_service_fee(self):
		service_fee_element = self.driver.find_element_by_id("forms_session_client_amount-charged")
		self.wait_for_element_visibility("ID", "forms_session_client_amount-charged")
		service_fee = service_fee_element.get_attribute('value')
		return service_fee

	def input_amount(self, amount):
		self.clear_field("ID", self.txt_amount_id)
		self.enter_character("ID", self.txt_amount_id, amount)

	def get_discount_value(self):
		discount_value = self.get_text("CSS_SELECTOR", self.discount_value_css)
		return discount_value

	def clk_create_session(self):
		self.click_js("CSS_SELECTOR", self.btn_create_session_css)

	def clk_session_info(self):
		# self.click("XPATH", self.tbl_sessioninfo_xpath)
		self.click("XPATH", self.tab_session_for_delete_xpath)
		session_info = self.get_text("CSS_SELECTOR", self.session_details_css)
		return session_info

	def tab_personal_session_info(self):
		personal_session_info = self.get_text("CSS_SELECTOR", self.tab_personal_session_details_css)
		return personal_session_info

	def clk_mobile_session_info(self):
		self.click("XPATH", self.tbl_sessioninfo_xpath)

	def mobile_session_details(self):
		mobile_session_details = self.get_text("CSS_SELECTOR", self.mobile_session_details_css)
		return mobile_session_details

	def clk_personal_session_more_information(self):
		self.click("CSS_SELECTOR", self.btn_personal_more_information_css)

	def clk_mobile_personal_session_more_information(self):
		self.click("CSS_SELECTOR", self.btn_mobile_personal_more_information_css)

	def clk_calendar_view(self):
		self.click("XPATH", self.btn_calendar_option_xpath)

	def clk_more_information(self):
		self.click("CSS_SELECTOR", self.btn_more_information_css)

	def clk_mobile_more_information(self):
		self.click("CSS_SELECTOR", self.btn_mobile_more_information_css)

	def clk_update_session(self):
		self.click_js("CSS_SELECTOR", self.btn_update_session_css)

	def clk_delete_session(self):
		try:
			self.click("CSS_SELECTOR", self.btn_delete_session_css)
		except:
			pass
		try:
			self.click("CSS_SELECTOR", self.btn_read_only_delete_session_css)
		except:
			pass

	def clk_delete_session_warn(self):
		self.click("CSS_SELECTOR", self.btn_delete_session_warn_css)
		'''
		wait = WebDriverWait(self.driver, 10)
		btn_delete_session_warn_element = wait.until(
			EC.presence_of_element_located((By.CSS_SELECTOR, self.btn_delete_session_warn_css))
		)
		ActionChains(self.driver).move_to_element(btn_delete_session_warn_element)
		sleep(2)
		btn_delete_session_warn_element.click()
		sleep(2)
		'''
	'''
	def view_calendar_week_view(self):
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.title_is("Calendar"))
		self.driver.find_elements_by_xpath(self.tbl_calendar_week_xpaths)
	'''
	def clk_calendar_day_view(self):
		self.click("CSS_SELECTOR", self.btn_day_view_css)

	def clk_calendar_week_view(self):
		self.click("CSS_SELECTOR", self.btn_week_view_css)

	def clk_calendar_room_view(self):
		self.click("CSS_SELECTOR", self.btn_room_view_css)

	def clk_hidden_days_view(self):
		self.click("CSS_SELECTOR", self.btn_hidden_days_css)

	def clk_hidden_day(self, hidden_day):
		cb_hidden_day_xpath = "//label[contains(text(),'" + hidden_day + "')]"
		self.click("XPATH", cb_hidden_day_xpath)

	def clk_apply_settings_btn(self):
		self.click("XPATH", self.btn_apply_settings_xpath)

	# Action on mobile elements
	def sel_therapist_name(self, therapist):
		self.enter("ID", self.sdd_therapist_id, therapist)
	'''
	def sel_service_type(self):
		sleep(5)
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.presence_of_element_located((By.ID, self.sdd_service_id)))
		self.driver.find_element_by_id(self.sdd_service_id).send_keys("CBT (Individual)")

	def sel_room_info(self):
		sleep(4)
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.presence_of_element_located((By.ID, self.sdd_room_id)))
		self.driver.find_element_by_id(self.sdd_room_id).send_keys("Room 2")
	'''
	def clk_btn_calendar_view(self):
		self.click("CSS_SELECTOR", self.btn_calendar_view_css)

	def desktop_calendar_week_info(self):
		self.wait_for_element_visibility("XPATH", self.tbl_calendar_week_xpaths)
		no_of_days = self.get_length(self.tbl_calendar_week_xpaths)
		days = []
		for x in range(2, no_of_days + 2):
			day = self.get_text("XPATH", "//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th[" + str(x) + "]/a")
			days.append(day)
		return days

	def desktop_calendar_room_info(self):
		self.wait_for_element_visibility("XPATH", self.tbl_room_view_xpaths)
		number_of_rooms = self.get_length(self.tbl_room_view_xpaths)
		rooms = []
		for x in range(2, number_of_rooms + 1):
			room = self.get_text("XPATH", "//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th[" + str(x) + "]")
			rooms.append(room)
		return rooms

	def desktop_calendar_day_info(self):
		calendar_day_info = self.get_text("XPATH", self.tbl_calendar_day_xpath)
		return calendar_day_info

	def clk_btn_calendar_week_view(self):
		self.click("CSS_SELECTOR", self.btn_calendar_week_view_css)

	def clk_therapist_availability_view(self):
		self.click("CSS_SELECTOR", self.btn_therapist_availability_css)

	def desktop_therapist_view_info(self):
		self.wait_for_element_visibility("XPATH", self.tbl_therapist_view_xpaths)
		no_of_therapists = self.get_length(self.tbl_therapist_view_xpaths)
		therapist_name_list = []
		for i in range(1, no_of_therapists + 1):
			therapist_name_x = self.get_text("XPATH", "//*[@id='fullcalendar']/div[2]/div/table/thead/tr/td/div/table/thead/tr/th[" + str(i) + "]")
			therapist_name_list.append(therapist_name_x)
		return therapist_name_list

	def clk_calendar_month_view(self):
		self.click("CSS_SELECTOR", self.btn_calendar_month_view_css)

	def clk_all_day_session(self):
		self.click("XPATH", self.tab_all_day_session_xpath)

	def desktop_calendar_month_info(self):
		month_view_info = self.get_text("CSS_SELECTOR", self.txt_month_view_info_css)
		return month_view_info

# Mobile view methods

	def mobile_calendar_day_info(self):
		day_text = self.get_text("XPATH", self.tbl_mobile_calendar_day_xpath)
		return day_text

	def clk_move_to_next_week(self):
		self.click("CSS_SELECTOR", self.btn_move_to_next_week_css)

	def clk_move_to_previous_week(self):
		self.click("CSS_SELECTOR", self.btn_move_to_previous_week_css)

	def clk_more_info_mobile(self):
		self.click("CSS_SELECTOR", self.btn_more_info_mobile_css)

	def clk_mobile_tab_calendar(self):
		self.click("XPATH", self.tab_mobile_calendar_xpath)

	def clk_mobile_client_session_details(self):
		self.click("XPATH", self.btn_mobile_client_session_details_xpath)

	def clk_btn_mobile_delete_session(self):
		self.click("XPATH", self.btn_mobile_client_delete_session_xpath)

	def clk_mobile_client_confirm_delete_session_element(self):
		self.click("XPATH", self.btn_mobile_client_confirm_delete_session_xpath)

	def clk_mobile_calendar_month_view(self):
		self.click("CSS_SELECTOR", self.btn_mobile_calendar_month_view_css)

	def clk_mobile_calendar_room_view(self):
		self.click("CSS_SELECTOR", self.btn_mobile_calendar_room_view_css)

	def clk_mobile_calendar_therapist_view(self):
		self.click("CSS_SELECTOR", self.btn_mobile_calendar_therapist_view_css)

	def clk_mobile_calendar_day_view(self):
		self.click("CSS_SELECTOR", self.btn_mobile_calendar_day_view_css)

	def clk_mobile_client_session(self):
		mobile_client_session_info = self.get_text("XPATH", self.tab_mobile_client_session_xpath)
		self.click("XPATH", self.tab_mobile_client_session_xpath)
		return mobile_client_session_info

	def clk_mobile_client_view_session(self):
		self.click("CSS_SELECTOR", self.btn_mobile_client_view_session_css)

	def tab_mobile_personal_session_details(self):
		mobile_personal_session_info = (
			self.get_text("XPATH", self.tab_mobile_personal_session_details_xpath)
		)
		return mobile_personal_session_info

	def clk_appointment_delete_confirm(self):
		self.click("CSS_SELECTOR", self.btn_appointment_delete_confirm_css)

	def sel_mobile_session(self, session_name):
		self.wait_for_element_visibility("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']")
		no_of_sessions = self.get_length(self.tab_client_session_list_xpaths)
		sessions_list = []
		for i in range(1, no_of_sessions + 1):
			session_x = self.get_text("XPATH", "//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div/div[2]")
			sessions_list.append(session_x)
			if session_x == session_name:
				select_session_xpath = (
					"//div[@data-testid='components_common_table-wrapper-mobile']/div[" + str(i) + "]/div"
				)
				sleep(1)
				self.click("XPATH", select_session_xpath)
				break
			else:
				continue
		return sessions_list

	def tab_calendar_today(self):
		self.click("CSS_SELECTOR", self.tab_calendar_today_css)

	def clk_session_delete_appointment_confirm(self):
		self.click("CSS_SELECTOR", self.btn_session_delete_appointment_confirm_css)

	def check_all_day_session(self):
		# self.click_js("CSS_SELECTOR", self.all_day_session_css)
		self.click_js("XPATH", self.all_day_session_xpath)

	def clk_mobile_jump_to_today(self):
		self.click("CSS_SELECTOR", self.tab_mobile_jump_to_today_css)

	def text_mobile_date_info(self):
		act_date_info = self.get_text("CSS_SELECTOR", self.tab_date_info_css)
		return act_date_info

	def clk_all_day_session_slot(self):
		#self.scroll("XPATH", self.all_day_session_slot_xpath)
		self.click("XPATH", self.all_day_session_slot_xpath)

	def clk_all_day_session_info(self):
		self.click("XPATH", self.all_day_session_info_xpath)

	def clk_create_all_day_session(self):
		self.click("XPATH", self.btn_create_all_day_session_xpath)

	def get_no_personal_sessions(self):
		self.wait_for_element_visibility("XPATH", "//div[@class='fc-content-skeleton']")
		no_of_personal_sessions = self.get_length(self.all_day_session_info_xpath)
		return no_of_personal_sessions

	def clk_session_for_delete(self):
		self.click("XPATH", self.tab_session_for_delete_xpath)

	def get_no_of_sessions_for_delete(self):
		no_of_sessions = self.get_length(self.tab_session_for_delete_xpath)
		return no_of_sessions

	def clk_book_session_time(self):
		self.click("XPATH", "//tr[@data-time='09:00:00']")

	def clk_video_session(self):
		self.click("XPATH", self.check_video_session_xpath)

	def check_presence_video_option(self):
		len = self.get_length(self.check_video_session_xpath)
		return len

	def check_video_option_selected(self):
		self.driver.find_elements_by_xpath()

