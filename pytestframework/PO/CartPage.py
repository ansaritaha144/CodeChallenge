
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from pytestframework.configReader import readConfig


class CartPage:


    @staticmethod
    def verifyCartPageIsDisplayed(driver):
        assert driver.find_element(MobileBy.XPATH, readConfig('Locator-CartPage', 'CartPageTitle')).is_displayed(), 'Cart Page is not displayed'


    @staticmethod
    def getProductsInCart(driver):
        inCartProducts = driver.find_elements(MobileBy.XPATH, readConfig('Locator-CartPage', 'CartPage_ProductTitle'))
        inCartProductNames = []
        for product in inCartProducts:
            inCartProductNames.append(product.text)
        return inCartProductNames

    @staticmethod
    def getTotalAmount(driver):
        total_amt_str = driver.find_element(MobileBy.ID, readConfig('Locator-CartPage', 'CartPage_TotalAmount')).text
        total_amt = float(total_amt_str.split('$')[1])
        return total_amt


    @staticmethod
    def clickOnSendEmailCheckBox(driver):
        driver.find_element(MobileBy.XPATH, readConfig('Locator-CartPage', 'CartPage_Checkbox')).click()


    @staticmethod
    def clickOnProceedButton(driver):
        driver.find_element(AppiumBy.ID, readConfig('Locator-CartPage', 'CartPage_ProceedButton')).click()

