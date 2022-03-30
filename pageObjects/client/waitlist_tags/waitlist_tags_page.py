from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from utilities.BasePage import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class WaitlistTagsPage(BasePage):
	client_add_tags_css = "*[data-testid='components_client-top-panel_add-tags']"
	dd_client_tags_xpath = "//*[@id='components_client-top-panel_add-tag-select']/div/div[2]"
	dd_mobile_client_tags_xpath = "//*[@id='containers_client_add-tag']/div[1]"
	dd_client_tags_input_xpath = (
		"//div[contains(@class, 'TagSelect__TagSelectField')]/div[1]/div[1]/div[2]/div[1]/input[1]"
	)
	tag_list_container_css = "*[components_client-tag-stack_tag-list-container]"
	btn_remove_client_tag_css = "*[data-testid='components_tag_remove-tag']"

	settings_tags_css = "//button[normalize-space()='Tags']"
	txt_tag_title_xpath = "//input[@name='title']"
	btn_settings_add_tag_css = "*[data-testid='forms_settings_practice-details_add-tag']"
	txt_settings_add_color_xpath = "//div[@data-testid='forms_settings_practice-details_add-tag_color']"
	btn_settings_edit_tag_xpath = "//button[@aria-label='Edit Tag']"
	btn_settings_delete_tag = "//button[@aria-label='Delete Tag']"
	get_client_tag_name_xpaths = "//div[@data-testid='components_client-tag-stack_tag-list-container']/span"
	settings_tags_xpaths = "//div[@data-testid='components_table']/div[1]/div"
	btn_confirm_delete_settings_tag_xpath = "//button[@aria-label='delete tag']"
	txt_settings_edit_tag_xpath = "//div[contains(@class,'EditTag')]//input[@name='title']"
	btn_save_settings_tag_css = "*[data-testid='containers_settings_practice-details_save-tag']"
	select_first_tag_xpath = "(//div[@data-testid='components_table']/div[1]/div[1]/div[2]/span[1]/span)[1]"
	btn_mobile_close_client_profile_xpath = "//button[@aria-label='Close']"

	# mobile elements
	#mobile_client_tag_id = "containers_client_add-tag"

	# waitlist elements

	def __init__(self, driver):
		super().__init__(driver)
		self.driver = driver
		self.wait = WebDriverWait(self.driver, 10)

	# tag methods

	def clk_client_add_tags(self):
		self.click("CSS_SELECTOR", self.client_add_tags_css)

	def sel_client_tag(self, tag_name):
		self.click("XPATH", self.dd_client_tags_xpath)
		self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", tag_name))

	def clk_remove_client_tag(self):
		self.click("CSS_SELECTOR", self.btn_remove_client_tag_css)

	def clk_settings_tags(self):
		self.click("XPATH", self.settings_tags_css)

	def clk_settings_add_tag(self):
		self.click("CSS_SELECTOR", self.btn_settings_add_tag_css)

	def clk_settings_edit_tag(self):
		self.click("XPATH", self.btn_settings_edit_tag_xpath)

	def clk_settings_delete_tag(self):
		self.click("XPATH", self.btn_settings_delete_tag)

	def input_settings_tag_title(self, tag_title):
		self.enter("XPATH", self.txt_tag_title_xpath, tag_title)

	def input_settings_tag_color(self, color):
		self.enter("XPATH", self.txt_settings_add_color_xpath, color)

	def get_client_tags_list(self):
		self.wait_for_element_visibility("CSS_SELECTOR", self.client_add_tags_css)
		no_of_tags = self.get_length(self.get_client_tag_name_xpaths)
		tags_name_list = []
		for i in range(1, no_of_tags + 1, 2):
			tag_name_x = self.get_text("XPATH", "//div[@data-testid='components_client-tag-stack_tag-list-container']/span[" + str(i) + "]")
			tags_name_list.append(tag_name_x)
		print("tags name list ", tags_name_list)
		return tags_name_list

	def delete_settings_tag(self, tag_name):
		self.wait_for_element_visibility("XPATH", self.txt_tag_title_xpath)
		no_of_tags = self.get_length(self.settings_tags_xpaths)
		tags_name_list = []
		for i in range(1, no_of_tags + 1):
			tag_name_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[1]/div[" + str(i) + "]/div[2]/span[1]/span")
			tags_name_list.append(tag_name_x)
			if tag_name_x == tag_name:
				select_tag_xpath = "//div[@data-testid='components_table']/div[1]/div[" + str(i) + "]/div[3]/span/button[2]"
				sleep(0.5)
				self.click_js("XPATH", select_tag_xpath)
				break
			else:
				continue

	def clk_confirm_delete_settings_tag(self):
		self.click("XPATH", self.btn_confirm_delete_settings_tag_xpath)

	def get_settings_tags_list(self):
		self.wait_for_element_visibility("XPATH", self.txt_tag_title_xpath)
		no_of_tags = self.get_length(self.settings_tags_xpaths)
		tags_name_list = []
		for i in range(1, no_of_tags + 1):
			tag_name_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[1]/div[" + str(i) + "]/div[2]/span[1]/span")
			tags_name_list.append(tag_name_x)
		return tags_name_list

	def edit_settings_tag(self, tag_name):
		self.wait_for_element_visibility("XPATH", self.txt_tag_title_xpath)
		no_of_tags = self.get_length(self.settings_tags_xpaths)
		tags_name_list = []
		for i in range(1, no_of_tags + 1):
			tag_name_x = self.get_text("XPATH", "//div[@data-testid='components_table']/div[1]/div[" + str(i) + "]/div[2]/span[1]/span")
			tags_name_list.append(tag_name_x)
			if tag_name_x == tag_name:
				select_tag_xpath = "//div[@data-testid='components_table']/div[1]/div[" + str(i) + "]/div[3]/span/button[1]"
				sleep(0.5)
				self.click_js("XPATH", select_tag_xpath)
				break
			else:
				continue

	def input_settings_new_tag_name(self, new_tag_title):
		self.clear_field("XPATH", self.txt_settings_edit_tag_xpath)
		self.enter("XPATH", self.txt_settings_edit_tag_xpath, new_tag_title)

	def clk_save_settings_tag(self):

		self.click("CSS_SELECTOR", self.btn_save_settings_tag_css)
	def get_number_of_settings_tag(self):
		self.wait_for_element_visibility("XPATH", self.txt_tag_title_xpath)
		no_of_tags = self.get_length(self.settings_tags_xpaths)
		return no_of_tags
	'''
	def sel_mobile_client_tag(self, tag_name):
		print("tag name ", tag_name)
		mobile_client_tag_id = "containers_client_add-tag"
		element = self.wait_for_element_visibility("ID", mobile_client_tag_id)
		select = Select(element)
		select.select_by_value(tag_name)
	'''
	def sel_mobile_client_tag(self, tag_name):
		print("tage name ", tag_name)
		self.click("XPATH", self.dd_mobile_client_tags_xpath)
		self.enter_character("XPATH", self.dd_mobile_client_tags_xpath, tag_name)
		#self.enter("XPATH", self.dd_mobile_client_tags_xpath, Keys.RETURN)
		self.click("XPATH", "//div[contains(@class, 'react-select__menu')]//div[text()='OPTION_VALUE']".replace("OPTION_VALUE", tag_name))
	'''
	def sel_mobile_client_tag(self, tag_name):
		print("tage name ", tag_name)
		tag_element = self.wait_for_element_visibility("XPATH", self.dd_mobile_client_tags_xpath)
		self.click("XPATH", self.dd_mobile_client_tags_xpath)
		self.driver.execute_script("arguments[0].value= '';", tag_element)
		self.driver.execute_script("arguments[0].value= '" + tag_name + "';", tag_element)
	'''
	def get_mobile_client_tags_list(self):
		self.wait_for_element_visibility("XPATH", self.dd_mobile_client_tags_xpath)
		no_of_tags = self.get_length(self.get_client_tag_name_xpaths)
		print("\n no of tags ", no_of_tags)
		tags_name_list = []
		#for i in range(1, no_of_tags + 1, 4):
		for i in range(1, no_of_tags, 4):
			tag_name_x = self.get_text("XPATH", "//div[@data-testid='components_client-tag-stack_tag-list-container']/span[" + str(i) + "]")
			tags_name_list.append(tag_name_x)
		print("tags name list ", tags_name_list)
		return tags_name_list

	def clk_first_settings_tag(self):
		select_tag_xpath = "//div[@data-testid='components_table']/div[1]/div[1]/div[3]/span/button[2]"
		sleep(0.5)
		self.click_js("XPATH", select_tag_xpath)

	def get_no_of_settings_tags(self):
		self.wait_for_element_visibility("XPATH", self.txt_tag_title_xpath)
		no_of_tags = self.get_length(self.settings_tags_xpaths)
		return no_of_tags

	def clk_mobile_client_profile_close(self):
		self.click("XPATH", self.btn_mobile_close_client_profile_xpath)

	# waitlist methods
