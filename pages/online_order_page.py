from .base_page import BasePage
from .locators import AuthorizationPageLocators
from .locators import OnlineOrderPageLocators
import time
import re


class OnlineOrderPage(BasePage):
    def expand_shadow_element(self, element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def sign_in(self, email, password, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        email_input = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_EMAIL)
        password_input = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)
        button = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_BUTTON)
        button.click()

    def add_three_items_to_cart(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_TAG))
        add_button_1 = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.BUTTON_1)
        add_button_1.click()
        time.sleep(1)
        add_button_2 = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.BUTTON_2)
        add_button_2.click()
        time.sleep(1)
        add_button_3 = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.BUTTON_3)
        add_button_3.click()
        time.sleep(1)

    def should_be_3_on_the_cart_icon(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_TAG))
        quantity = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.QUANTITY)).text
        assert quantity == "3", f"вместо '3' встречено количество товаров = {quantity}"

    def should_be_correct_total_price_in_the_cart(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_TAG))
        product_1_price_text = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.PRODUCT_1_PRICE)).text
        product_2_price_text = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.PRODUCT_2_PRICE)).text
        product_3_price_text = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.PRODUCT_3_PRICE)).text
        product_1_price = self.price_text_to_float(product_1_price_text)
        product_2_price = self.price_text_to_float(product_2_price_text)
        product_3_price = self.price_text_to_float(product_3_price_text)
        total_price_of_items = product_1_price + product_2_price + product_3_price
        cart_button = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.CART_BUTTON)
        cart_button.click()
        time.sleep(3)
        total_price_in_the_cart_text = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.CART_PRICE).text)
        total_price_in_the_cart = float(total_price_in_the_cart_text)
        assert total_price_of_items == total_price_in_the_cart, f"Суммы не совпадают, общая сумма товаров = {total_price_of_items}, сумма товаров в корзине = {total_price_in_the_cart}"

    def price_text_to_float(self, text):
        price = float(re.search(r'\d*\.\d+|\d+', text).group(0))
        return price


