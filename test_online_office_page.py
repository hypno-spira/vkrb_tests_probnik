from .pages.login_page import LoginPage
from .pages.global_settings_page import GlobalSettingsPage
from .pages.profile_field_settings_page import ProfileFieldSettingsPage
from .pages.admin_personal_account_settings_page import AdminPersonalAccountSettingsPage
from .pages.online_order_page import OnlineOrderPage
from .pages.admin_invoices_page import AdminInvoicesPage
import pytest
import time
import allure
from allure_commons.types import AttachmentType



def test_quantity_and_total_price_of_the_goods_in_the_cart(browser):
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US/order/online-order"
    online_order_page = OnlineOrderPage(browser, link)
    online_order_page.open()
    email, password = "user3@example.com", "password_0"
    online_order_page.sign_in(email, password, browser)
    online_order_page.add_three_items_to_cart(browser)
    online_order_page.should_be_3_on_the_cart_icon(browser)
    online_order_page.should_be_correct_total_price_in_the_cart(browser)

@pytest.mark.testing
def test_successful_purchase(browser):
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US/order/order-history"
    online_order_page = OnlineOrderPage(browser, link)
    online_order_page.open()
    email, password = "user5@example.com", "password_0"
    online_order_page.sign_in(email, password, browser)
    last_order_id = online_order_page.remember_the_last_order_number(browser)
    online_order_page.add_three_items_to_cart(browser)
    online_order_page.ordering(browser)
    online_order_page.successful_payment_in_test_gateway()
    online_order_page.should_be_green_message_after_purchase(browser)
    new_order_id = online_order_page.should_be_new_order_in_order_history(last_order_id, browser)
    online_order_page.new_order_should_be_successful(browser)
    link = "https://dev-vkhvorostov.mlmsoft.com/finance/invoice"
    invoices_page = AdminInvoicesPage(browser, link)
    invoices_page.open()
    email, password = "admin@mlm-soft.com", "9UA27VF2W2Bwn7Jo"
    invoices_page.sign_in(email, password)
    invoices_page.new_order_should_be_in_first_line(new_order_id)
    invoices_page.new_order_should_be_successful()





