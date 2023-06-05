
from appium.webdriver.common.appiumby import AppiumBy


class commonUtility:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        return driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textMatches(\"' + text + '\").instance(0))').is_displayed()


    @staticmethod
    def customSwipe(X1, Y1, X2, Y2, howManySwipes, driver):
        for i in range(1, howManySwipes + 1):
            driver.swipe(X1, Y1, X2, Y2, 500)


    @staticmethod
    def scrollToEndOfThePage(driver):
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollToEnd(2)').is_displayed()

