
from appium.webdriver.common.mobileby import MobileBy
from pytestframework.configReader import readConfig


class GooglePage:


    @staticmethod
    def enterTextInSearchBox(text, driver):
        driver.find_element(MobileBy.XPATH, readConfig('Locator-GooglePage', 'InputBox')).send_keys(text)
        driver.hide_keyboard()
        driver.press_keycode(13)


    @staticmethod
    def navigateBack(driver):
        driver.back()

