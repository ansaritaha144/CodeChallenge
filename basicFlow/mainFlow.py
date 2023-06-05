
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from generalUtility import generalUtility

# DRIVER SETUP
desired_caps = dict(
    deviceName='Android',
    platformName='Android',
    appPackage='com.androidsample.generalstore',
    appActivity='com.androidsample.generalstore.SplashActivity'
)
driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

# GENERAL STORE HOMEPAGE
assert driver.find_element(MobileBy.ID, 'com.androidsample.generalstore:id/toolbar_title').is_displayed(), 'General Store App Is Not Displayed'
driver.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/spinnerCountry').click()
generalUtility.scrollToTextByAndroidUIAutomator('India', driver)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textMatches("India").instance(0)').click()
driver.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/nameField').send_keys('Taha Ansari')
driver.hide_keyboard()
driver.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/btnLetsShop').click()

# PRODUCT PAGE
assert driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("Products").instance(0)').is_displayed(), "Product Page is not displayed"
generalUtility.scrollToTextByAndroidUIAutomator("PG 3", driver)
driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="PG 3"]/..//android.widget.TextView[@text="ADD TO CART"]').click()
first_product = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="PG 3"]').text
product_price = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="PG 3"]/..//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productPrice"]').text
first_product_price = float(product_price.split('$')[1])
print(first_product_price)
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollToEnd(2)').is_displayed()
driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Nike SFB Jungle"]/..//android.widget.TextView[@text="ADD TO CART"]').click()
second_product = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Nike SFB Jungle"]').text
product_price = driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Nike SFB Jungle"]/..//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productPrice"]').text
second_product_price = float(product_price.split('$')[1])
print(second_product_price)
driver.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/appbar_btn_cart').click();

# CART PAGE
assert driver.find_element(MobileBy.XPATH, '//android.widget.TextView[@text="Cart"]').is_displayed(), 'Cart Page is not displayed'
assert first_product == driver.find_elements(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productName"]')[0].text
assert second_product == driver.find_elements(MobileBy.XPATH, '//android.widget.TextView[@resource-id="com.androidsample.generalstore:id/productName"]')[1].text
total_amt_str = driver.find_element(MobileBy.ID, 'com.androidsample.generalstore:id/totalAmountLbl').text
total_amt = float(total_amt_str.split('$')[1])
print(total_amt)
assert total_amt == first_product_price + second_product_price
driver.find_element(MobileBy.XPATH, '//android.widget.CheckBox').click()
driver.find_element(AppiumBy.ID, 'com.androidsample.generalstore:id/btnProceed').click()

# GOOGLE PAGE
driver.find_element(MobileBy.XPATH, '//android.widget.EditText').send_keys('General Store !!!')
driver.hide_keyboard()
driver.press_keycode(13)
driver.back()

# GENERAL STORE HOME PAGE
assert driver.find_element(MobileBy.ID, 'com.androidsample.generalstore:id/toolbar_title').is_displayed(), 'General Store App Is Not Displayed After Google Search'
print('TEST PASSED !!!!')
driver.quit()
