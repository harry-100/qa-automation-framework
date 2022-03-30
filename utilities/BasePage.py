import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import *
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, \
    ElementNotInteractableException, InvalidElementStateException, TimeoutException, \
    ElementClickInterceptedException
import utilities.CustomLogger as cl
from selenium.webdriver.common.keys import Keys
from time import sleep


class BasePage(object):
    log = cl.custom_logger(logging.DEBUG)
    wait_secs = 20

    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        self.log.info("getting page title --> " + self.driver.title)
        return self.driver.title

    def get_source(self):
        self.log.info("getting page source --> " + self.driver.page_source)
        return self.driver.page_source

    def select_value_by_text(self, locator_mode, locator, value, waitime=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, waitime)
        select = Select(element)
        select.select_by_visible_text(value)

    def get_length(self, locator):
        length = len(self.driver.find_elements_by_xpath(locator))
        self.log.info("length of " + locator + " --> " + str(length))
        return length
   
    def get_url(self):
        return self.driver.current_url()

    def navigate(self, url):
        self.driver.get(url)

    def get_attribute(self, xpath, attribute):
        value = str(self.driver.find_element_by_xpath(xpath).get_attribute(attribute))
        self.log.info("attribute of " + xpath + "-->" + attribute)
        return value

    def get_display(self, *locator):
        return str(self.driver.find_element_by_xpath(*locator).value_of_css_property('display'))

    def get_text(self, locator_mode, locator, wait_time=wait_secs):
        element_visible = self.wait_for_element_visibility(locator_mode, locator, wait_time)
        if element_visible:
            for itr in range(6):
                try:
                    sleep(0.2)
                    return element_visible.text
                except StaleElementReferenceException:
                    self.log.info("Get text  retry -  " + str(itr))
                except ElementNotInteractableException:
                    self.log.info("Get text  retry -  " + str(itr))
                except InvalidElementStateException:
                    self.log.info("Retry enter " + str(itr))
                except ElementClickInterceptedException:
                    self.log.info("Retry enter " + str(itr))
        else:
            self.log.info("[Fail] element not present  " + locator)
            assert element_visible

    def hover(self, locator_mode, locator, wait_time=wait_secs):
        element_visible = self.wait_for_element_visibility(locator_mode, locator, wait_time)

        if element_visible:
            element = self.driver.find_element_by_xpath(locator)
            hover = ActionChains(self.driver).move_to_element(element)
            hover.perform()
        else:
            self.log("[Fail] element not present " + locator)
            assert element_visible

    def wait_until_element_clickable(self, locator_mode, locator, wait_time=wait_secs):
        try:
            if locator_mode == "ID":
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable((By.ID, locator))
                )
            elif locator_mode == "NAME":
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable((By.NAME, locator))
                )
            elif locator_mode == "XPATH":
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable((By.XPATH, locator))
                )
            elif locator_mode == "CSS_SELECTOR":
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, locator))
                )
            elif locator_mode == "CLASS_NAME":
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.visibility_of_element_located((By.CLASS_NAME, locator))
                )
            else:
                raise Exception("Unsupported locator strategy.")
            self.log.info("[pass] " + locator + " present")
        except NoSuchElementException:
            self.log.info("[fail] " + locator + " not present")
            return None
        # self.high_light_element(element)
        return element

    def wait_for_element_visibility(self, locator_mode, locator, wait_time=wait_secs):
        if locator_mode == "ID":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.ID, locator))
            )
        elif locator_mode == "NAME":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.NAME, locator))
            )
        elif locator_mode == "XPATH":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.XPATH, locator))
            )
        elif locator_mode == "CSS_SELECTOR":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator))
            )
        elif locator_mode == "CLASS_NAME":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.visibility_of_element_located((By.CLASS_NAME, locator))
            )
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def wait_for_element_presence(self, locator_mode, locator, wait_time=wait_secs):
        if locator_mode == "ID":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.ID, locator))
            )
        elif locator_mode == "NAME":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.NAME, locator))
            )
        elif locator_mode == "XPATH":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, locator))
            )
        elif locator_mode == "CSS_SELECTOR":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator))
            )
        elif locator_mode == "CLASS_NAME":
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.CLASS_NAME, locator))
            )
        else:
            raise Exception("Unsupported locator strategy.")
        return element

    def click(self, locator_mode, locator, wait_time=wait_secs):
        element_visible = self.wait_for_element_visibility(locator_mode, locator, wait_time)
        if element_visible:

            element_clickable = self.wait_until_element_clickable(locator_mode, locator, wait_time)
            if element_clickable:
                for itr in range(6):
                    try:
                        sleep(0.2)
                        element_clickable.click()
                        break
                    except StaleElementReferenceException:
                        self.log.info("Retry click " + str(itr))
                    except ElementNotInteractableException:
                        self.log.info("Retry click " + str(itr))
                    except InvalidElementStateException:
                        self.log.info("Retry click " + str(itr))
                    except ElementClickInterceptedException:
                        self.log.info("Retry click " + str(itr))
                self.log.info("[pass] clicked " + locator)
            else:
                self.log.info("[Fail] element not clickable + " + locator)
                assert element_clickable
        else:
            self.log.info("[Fail] element not present + " + locator)
            assert element_visible

    def enter(self, locator_mode, locator, value, wait_time=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, wait_time)
        if element:
            for itr in range(6):
                try:
                    sleep(0.2)
                    element.clear()
                    element.send_keys(value)
                    break
                except StaleElementReferenceException:
                    self.log.info("Retry enter " + str(itr))
                except ElementNotInteractableException:
                    self.log.info("Retry enter " + str(itr))
                except InvalidElementStateException:
                    self.log.info("Retry enter " + str(itr))
                except ElementClickInterceptedException:
                    self.log.info("Retry enter " + str(itr))

            self.log.info("[pass] entered " + str(value) + " in " + locator)
        else:
            self.log.info("[Fail] element not present + " + locator)
            assert element

    def enter_withoutclear(self, locator_mode, locator, value, wait_time=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, wait_time)
        if element:
            for itr in range(6):
                try:
                    sleep(0.2)
                    element.send_keys(value)
                    break
                except StaleElementReferenceException:
                    self.log.info("Retry enter " + str(itr))
                except ElementNotInteractableException:
                    self.log.info("Retry enter " + str(itr))
                except InvalidElementStateException:
                    self.log.info("Retry enter " + str(itr))
                except ElementClickInterceptedException:
                    self.log.info("Retry enter " + str(itr))
            self.log.info("[pass] entered " + str(value) + " in " + locator)
        else:
            self.log.info("[Fail] element not present + " + locator)
            assert element

    def click_js(self, locator_mode, locator, waitime=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, waitime)
        if element:
            for itr in range(6):
                        try:
                            sleep(0.2)
                            self.driver.execute_script("arguments[0].click();", element)
                            break
                        except StaleElementReferenceException:
                            self.log.info("Retry click " + str(itr))
                        except ElementNotInteractableException:
                            self.log.info("Retry click " + str(itr))
                        except InvalidElementStateException:
                            self.log.info("Retry enter " + str(itr))
                        except ElementClickInterceptedException:
                            self.log.info("Retry click " + str(itr))
            else:
                self.log.info("[Fail] clicked " + locator + "by JS")
                assert element

    def set_js(self, locator_mode, locator, value, waitime=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, waitime)
        self.driver.execute_script("arguments[0].value='" + value + "';", element)
        self.log.info("[pass] Set value " + locator + "by JS")
    '''
    def scroll(self, xpath):
        element = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
    '''
    def scroll(self, locator_mode, locator, waitime=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, waitime)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def clear_field(self, locator_mode, locator, wait_time=wait_secs):
        element = self.wait_until_element_clickable(locator_mode, locator, wait_time)
        sleep(0.3)
        if element:
            text = element.get_attribute("value")
        for i in text:
            element.send_keys(Keys.BACKSPACE)
            sleep(0.3)
            self.log.info("[pass] Field cleared " + locator)
        else:
            self.log.info("[Fail] element not present + " + locator)
            assert element

    def enter_character(self, locator_mode, locator, value, wait_time=wait_secs):
        element = self.wait_for_element_visibility(locator_mode, locator, wait_time)
        if element:
            for itr in range(6):
                try:
                    sleep(0.2)
                    no_of_chars = len(value)
                    element.clear()
                    for i in range(no_of_chars):
                        element.send_keys(value[i])
                        sleep(0.3)
                    break
                except StaleElementReferenceException:
                    self.log.info("Retry enter " + str(itr))
                except ElementNotInteractableException:
                    self.log.info("Retry enter " + str(itr))
                except InvalidElementStateException:
                    self.log.info("Retry enter " + str(itr))
                except ElementClickInterceptedException:
                            self.log.info("Retry enter " + str(itr))

            self.log.info("[pass] entered " + str(value) + " in " + locator)
        else:
            self.log.info("[Fail] element not present + " + locator)
            assert element
