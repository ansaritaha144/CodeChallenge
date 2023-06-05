
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from pytestframework.Utilities.commonUtility import commonUtility
from pytestframework.configReader import readConfig


class ProductPage:

    @staticmethod
    def verifyProductPageIsDisplayed(driver):
        assert driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, readConfig('Locator-ProductPage', 'ProductPageTitle')).is_displayed(), "Product Page is not displayed"

    @staticmethod
    def scrollUptoTheProduct(text, driver):
        commonUtility.scrollToTextByAndroidUIAutomator(text, driver)


    @staticmethod
    def addProductToCartAndGetDetails(text, driver):
        driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="' + text + '"]/..//android.widget.TextView[@text="ADD TO CART"]').click()
        product_name = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="' + text + '"]').text
        price_element = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="' + text + '"]/..//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productPrice"]').text
        product_price = float(price_element.split('$')[1])
        Product_Details = [product_name, product_price]
        return Product_Details


    @staticmethod
    def clickOnCartIcon(driver):
        driver.find_element(AppiumBy.ID, readConfig('Locator-ProductPage', 'CartButton')).click();

