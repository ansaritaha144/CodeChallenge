
from appium import webdriver
from pytestframework.PO.HomePage import HomePage
from pytestframework.PO.ProductPage import ProductPage
from pytestframework.PO.CartPage import CartPage
from pytestframework.PO.GooglePage import GooglePage
from pytestframework.configReader import readConfig
from pytestframework.Utilities.commonUtility import commonUtility


def setup_function():
    desired_caps = dict(
        deviceName='Android',
        platformName='Android',
        appPackage=readConfig('Setup Info', 'appPackage'),
        appActivity=readConfig('Setup Info', 'appActivity')
    )
    global driver
    driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)
    driver.implicitly_wait(readConfig('Setup Info', 'implicit.wait'))


def teardown_function():
    driver.quit()


def test_generalStoreE2E():

    HomePage.verifyHomePageIsDisplayed(driver)
    HomePage.selectIndiaFromDropdown(readConfig('UserData', 'CountryName'), driver)
    HomePage.enterUsername(readConfig('UserData', 'Username'), driver)
    HomePage.clickOnLetsShopButton(driver)

    ProductPage.verifyProductPageIsDisplayed(driver)
    ProductPage.scrollUptoTheProduct(readConfig('UserData', 'Product1'), driver)
    PG3_Details = ProductPage.addProductToCartAndGetDetails(readConfig('UserData', 'Product1'), driver)
    product1_name = PG3_Details[0]
    product1_price = PG3_Details[1]
    print(PG3_Details)
    commonUtility.scrollToEndOfThePage(driver)
    NikeProduct_Details = ProductPage.addProductToCartAndGetDetails(readConfig('UserData', 'Product2'), driver)
    product2_name = NikeProduct_Details[0]
    product2_price = NikeProduct_Details[1]
    print(NikeProduct_Details)
    productAdded = [product1_name, product2_name]
    ProductPage.clickOnCartIcon(driver)

    CartPage.verifyCartPageIsDisplayed(driver)
    inCartProducts = CartPage.getProductsInCart(driver)
    print(inCartProducts)
    assert productAdded == inCartProducts, 'Products Are Not Matching'
    total_amt = CartPage.getTotalAmount(driver)
    assert total_amt == product1_price + product2_price, 'Total Amount Is Not Matching'
    CartPage.clickOnSendEmailCheckBox(driver)
    CartPage.clickOnProceedButton(driver)

    GooglePage.enterTextInSearchBox(readConfig('UserData', 'SearchText'), driver)
    GooglePage.navigateBack(driver)

    HomePage.verifyHomePageIsDisplayed(driver)

