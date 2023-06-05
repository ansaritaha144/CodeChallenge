
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from pytestframework.Utilities.commonUtility import commonUtility
from pytestframework.configReader import readConfig


class HomePage:

    @staticmethod
    def verifyHomePageIsDisplayed(driver):
        assert driver.find_element(MobileBy.ID, readConfig('Locator-HomePage', 'GeneralStoreTitle')).is_displayed(), 'General Store App Is Not Displayed'

    @staticmethod
    def selectIndiaFromDropdown(countryName, driver):
        driver.find_element(AppiumBy.ID, readConfig('Locator-HomePage', 'CountryDropdown')).click()
        commonUtility.scrollToTextByAndroidUIAutomator(countryName, driver)
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches(\"' + countryName + '\").instance(0)').click()

    @staticmethod
    def enterUsername(userName, driver):
        driver.find_element(AppiumBy.ID, readConfig('Locator-HomePage', 'UsernameInputBox')).send_keys(userName)
        driver.hide_keyboard()

    @staticmethod
    def clickOnLetsShopButton(driver):
        driver.find_element(AppiumBy.ID, readConfig('Locator-HomePage', 'ShopButton')).click()
