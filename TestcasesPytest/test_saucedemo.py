import time
import pytest

from pages.saucedemologin_page import LoginSaucePage
from pages.addtocart_page import AddtocartPage
from pages.checkout_page import CheckoutPage
from pages.fillInfo_page import FillInfoPage
from pages.finish_page import FinishPage

from utilities.excel_utils import get_excel_data
from utilities.logger import get_logger


logger = get_logger()

# test data stored in excel sheet
test_data = get_excel_data(
    "C:/Users/bhash/PycharmProjects/Feb2026SeleniumPytestPOM/testdata/test_data.xlsx",
    "Sheet1"
)


class Test_SauceDemo:

    @pytest.mark.parametrize("username,password", test_data)
    def test_complete_flow(self, driver, username, password):

        logger.info("Opening SauceDemo")
        driver.get("https://www.saucedemo.com/")
        time.sleep(2)

        # login page
        lp = LoginSaucePage(driver)
        lp.login(username, password)
        time.sleep(2)
        # add product
        ip = AddtocartPage(driver)
        ip.add_product_to_cart()
        ip.go_to_cart()
        time.sleep(2)

        # checkout
        cp = CheckoutPage(driver)
        cp.go_to_checkout()
        time.sleep(2)

        # fill info
        fp = FillInfoPage(driver)
        fp.fill_info("Bhashkar", "Mishra", "700001")
        fp.click_continue()
        time.sleep(2)

        # finish
        finish = FinishPage(driver)
        finish.click_finish()
        time.sleep(2)

        assert "checkout-complete" in driver.current_url
        logger.info("Order success")

