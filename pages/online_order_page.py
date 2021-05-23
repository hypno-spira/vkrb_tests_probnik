from .base_page import BasePage
from .locators import AuthorizationPageLocators
from .locators import OnlineOrderPageLocators
import time
import re


class OnlineOrderPage(BasePage):
    order_id = 1

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

    def remember_the_last_order_number(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_HISTORY_TAG))
        time.sleep(3)
        last_order_id = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.LAST_ORDER_ID)).text
        order_id = int(last_order_id)

        online_order_link = self.browser.find_element_by_css_selector(OnlineOrderPageLocators.ONLINE_ORDER_LINK)
        online_order_link.click()
        time.sleep(1)
        return order_id

    def ordering(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_TAG))
        cart_button = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.CART_BUTTON)
        cart_button.click()
        time.sleep(3)
        button_to_2_step = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.BUTTON_F1T2_STEP)
        #browser.execute_script("return arguments[0].scrollIntoView(true);", button_to_2_step)
        button_to_2_step.click()
        time.sleep(3)
        address_input = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.ADDRESS)
        address_input.send_keys("Новосибирская обл, г Новосибирск, ул Новосибирская, д 999, кв 999")  # ?
        #pick_up_radio = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.PICK_UP_RADIO)
        #browser.execute_script("return arguments[0].scrollIntoView(true);", pick_up_radio)
        #pick_up_radio.click()
        button_to_3_step = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.BUTTON_F2T3_STEP)
        button_to_3_step.click()
        time.sleep(3)
        test_gateway_radio = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.TEST_GATEWAY_RADIO)
        #browser.execute_script("return arguments[0].scrollIntoView(true);", test_gateway_radio)
        test_gateway_radio.click()
        time.sleep(2)
        agree_checkbox = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.AGREE_CHECKBOX)
        #browser.execute_script("return arguments[0].scrollIntoView(true);", agree_checkbox)
        agree_checkbox.click()
        proceed_to_check_out = shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.PROCEED_TO_CHECK_OUT)
        proceed_to_check_out.click()
        time.sleep(3)

    def successful_payment_in_test_gateway(self):
        successful_payment_button = self.browser.find_element_by_css_selector(OnlineOrderPageLocators.SUCCESSFUL_PAYMENT_BUTTON)
        successful_payment_button.click()
        time.sleep(2)
        return_payment_button = self.browser.find_element_by_css_selector(OnlineOrderPageLocators.RETURN_BUTTON)
        return_payment_button.click()
        time.sleep(6)

    def should_be_green_message_after_purchase(self, browser):
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_contain_a_successful_icon(browser)
        order_history_link = self.browser.find_element_by_css_selector(OnlineOrderPageLocators.ORDER_HISTORY_LINK)
        order_history_link.click()
        time.sleep(2)

    def should_be_message_in_the_lower_right_corner(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.BOTTOM_RIGHT_MESSAGE), "Сообщение в правом нижнем углу не появилось"

    def message_should_contain_a_successful_icon(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.ICON_SUCCESS), f"иконка не отобразилась"

    def should_be_new_order_in_order_history(self, last_order_id, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_HISTORY_TAG))
        time.sleep(3)
        new_order_id = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.LAST_ORDER_ID)).text
        new_order_id = int(new_order_id)
        self.new_id_should_be_greater_then_last_id(new_order_id, last_order_id)
        return new_order_id

    def new_id_should_be_greater_then_last_id(self, new_order_id, last_order_id):
        assert new_order_id > last_order_id, f"новая запись не добавлена, id старого заказа - {last_order_id}, нового - {new_order_id}"

    def new_order_should_be_successful(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_HISTORY_TAG))
        new_order_status = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.NEW_ORDER_STATUS)).text
        assert new_order_status == "DONE", f"ожидался статус заказа DONE, встречен - {new_order_status}"

    def unsuccessful_payment_in_test_gateway(self):
        unsuccessful_payment_checkbox = self.browser.find_element_by_css_selector(
            OnlineOrderPageLocators.UNSUCCESSFUL_PAYMENT_CHECKBOX)
        unsuccessful_payment_checkbox.click()
        successful_payment_button = self.browser.find_element_by_css_selector(
            OnlineOrderPageLocators.SUCCESSFUL_PAYMENT_BUTTON)
        successful_payment_button.click()
        time.sleep(1)
        return_payment_button = self.browser.find_element_by_css_selector(OnlineOrderPageLocators.RETURN_BUTTON)
        return_payment_button.click()
        time.sleep(6)

    def should_be_yellow_message_after_purchase(self, browser):
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_contain_a_warning_icon(browser)
        order_history_link = self.browser.find_element_by_css_selector(OnlineOrderPageLocators.ORDER_HISTORY_LINK)
        order_history_link.click()
        time.sleep(2)

    def message_should_contain_a_warning_icon(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.ICON_WARNING), f"иконка не отобразилась"

    def new_order_should_be_unsuccessful(self, browser):
        shadow_dom = self.expand_shadow_element(
            browser.find_element_by_tag_name(OnlineOrderPageLocators.ONLINE_ORDER_HISTORY_TAG))
        new_order_status = (shadow_dom.find_element_by_css_selector(OnlineOrderPageLocators.NEW_ORDER_STATUS)).text
        assert new_order_status == "ERROR", f"ожидался статус заказа ERROR, встречен - {new_order_status}"

