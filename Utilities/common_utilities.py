from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from config.time_for_wait import explicit_wait_time
from conftest import driver


class CommonUtilities:

    def click_element(self, element):
        WebDriverWait(driver=driver, timeout=explicit_wait_time). \
            until(EC.element_to_be_clickable(element))
        driver.find_element(element[0], element[1]).click()

    def send_text(self, element, text):
        WebDriverWait(driver=driver, timeout=explicit_wait_time). \
            until(EC.element_to_be_clickable(element)).send_keys(text)

    def get_alert_text(self):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(EC.alert_is_present())
        al_text = driver.switch_to.alert.text
        return al_text

    def alert_accept(self):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(EC.alert_is_present())
        driver.switch_to.alert.accept()

    def get_text(self, element):
        get = WebDriverWait(driver=driver, timeout=explicit_wait_time). \
            until(EC.presence_of_element_located(element))
        # return driver.find_element(by=element[0], value=element[1]).text
        return get.text

    def wait_for_element(self, element):
        WebDriverWait(driver=driver, timeout=explicit_wait_time).until(EC.visibility_of_element_located(element))

