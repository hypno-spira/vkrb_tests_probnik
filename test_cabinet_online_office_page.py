from .pages.online_order_page import OnlineOrderPage
from .pages.admin_invoices_page import AdminInvoicesPage
from .pages.links import Links
from .pages.testdata import CorrectData
import pytest
import allure
from allure_commons.types import AttachmentType


@pytest.mark.total_price
@allure.feature("Подсчет суммы товаров в корзине")
@allure.story("№7. Подсчет суммы товаров в корзине")
@allure.severity("critical")
def test_quantity_and_total_price_of_the_goods_in_the_cart(browser):
    page = OnlineOrderPage(browser, Links.ONLINE_ORDER_LINK)
    page.open()
    email = CorrectData.EMAIL_ID4
    password = CorrectData.PASSWORD
    page.sign_in(email, password, browser)
    page.add_three_items_to_cart(browser)
    page.should_be_3_on_the_cart_icon(browser)
    with allure.step("Should be 3 on the cart icon"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Cart icon Screenshot", attachment_type=AttachmentType.PNG)
    page.should_be_correct_total_price_in_the_cart(browser)


@pytest.mark.purchase
@pytest.mark.purchase_1
@allure.feature("Совершение покупки в онлайн-заказе")
@allure.story("№8. Успешное совершение покупки")
@allure.severity("critical")
def test_successful_purchase(browser):
    online_order_page = OnlineOrderPage(browser, Links.ORDER_HISTORY_LINK)  # переход к online order
    online_order_page.open()
    email = CorrectData.EMAIL_ID5
    password = CorrectData.PASSWORD
    online_order_page.sign_in(email, password, browser)
    last_order_id = online_order_page.remember_the_last_order_number(browser)
    online_order_page.add_three_items_to_cart(browser)
    online_order_page.ordering(browser)
    online_order_page.successful_payment_in_test_gateway()
    online_order_page.should_be_green_message_after_purchase(browser)
    new_order_id = online_order_page.should_be_new_order_in_order_history(last_order_id, browser)
    online_order_page.new_order_should_be_successful(browser)
    with allure.step("Should be DONE new order in Order history "):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Order history Screenshot", attachment_type=AttachmentType.PNG)
    invoices_page = AdminInvoicesPage(browser, Links.ADMIN_INVOICE_LINK)  # переход к admin invoices
    invoices_page.open()
    email = CorrectData.ADMIN_EMAIL
    password = CorrectData.ADMIN_PASSWORD
    invoices_page.sign_in(email, password)
    invoices_page.new_order_should_be_in_first_line(new_order_id)
    invoices_page.new_order_should_be_successful()
    with allure.step("Should be DONE new order in admin invoices"):
        allure.attach(browser.get_screenshot_as_png(), name="Admin invoices Screenshot",
                      attachment_type=AttachmentType.PNG)


@pytest.mark.purchase
@pytest.mark.purchase_2
@allure.feature("Совершение покупки в онлайн-заказе")
@allure.story("№9. Неуспешное совершение покупки")
@allure.severity("critical")
def test_unsuccessful_purchase(browser):
    online_order_page = OnlineOrderPage(browser, Links.ORDER_HISTORY_LINK)  # переход к online order
    online_order_page.open()
    email = CorrectData.EMAIL_ID5
    password = CorrectData.PASSWORD
    online_order_page.sign_in(email, password, browser)
    last_order_id = online_order_page.remember_the_last_order_number(browser)
    online_order_page.add_three_items_to_cart(browser)
    online_order_page.ordering(browser)
    online_order_page.unsuccessful_payment_in_test_gateway()
    online_order_page.should_be_yellow_message_after_purchase(browser)
    new_order_id = online_order_page.should_be_new_order_in_order_history(last_order_id, browser)
    online_order_page.new_order_should_be_unsuccessful(browser)
    with allure.step("Should be ERROR new order in Order history "):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Order history Screenshot", attachment_type=AttachmentType.PNG)
    invoices_page = AdminInvoicesPage(browser, Links.ADMIN_INVOICE_LINK)  # переход к admin invoices
    invoices_page.open()
    email = CorrectData.ADMIN_EMAIL
    password = CorrectData.ADMIN_PASSWORD
    invoices_page.sign_in(email, password)
    invoices_page.new_order_should_be_in_first_line(new_order_id)
    invoices_page.new_order_should_be_unsuccessful()
    with allure.step("Should be ERROR new order in admin invoices"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Admin invoices Screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.transfer_wallet
@allure.feature("Перевод с одного бонусного кошелька на другой")
@allure.story("№10. Перевод с одного бонусного кошелька на другой")
@allure.severity("normal")
def test_transfer_wallet(browser):
    page = OnlineOrderPage(browser, Links.WALLET_TRANSFER_LINK)
    page.open()
    email1 = CorrectData.EMAIL_ID3
    email2 = CorrectData.EMAIL_ID5
    password = CorrectData.PASSWORD
    page.sign_in(email2, password, browser)
    recipient_bonus_wallet_before_transfer = page.remember_bonus_wallet_before_transfer(browser)
    page.logout(browser)
    page.sign_in(email1, password, browser)
    sender_bonus_wallet_before_transfer = page.remember_bonus_wallet_before_transfer(browser)
    page.making_a_transfer(browser)
    page.should_be_green_message_after_transfer(browser)
    with allure.step("Should be message Successful transfer"):
        allure.attach(browser.get_screenshot_as_png(), name="Successful transfer Screenshot",
                      attachment_type=AttachmentType.PNG)
    page.sender_bonus_wallet_should_be_less_after_transfer(sender_bonus_wallet_before_transfer, browser)
    page.logout(browser)
    page.sign_in(email2, password, browser)
    page.recipient_bonus_wallet_should_be_more_after_transfer(recipient_bonus_wallet_before_transfer, browser)
