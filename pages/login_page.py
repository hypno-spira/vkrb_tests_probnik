from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import CabinetLocators
from .locators import AuthorizationPageLocators
from .locators import DashboardPageLocators
from .locators import RegistrationPageLocators
import re


class LoginPage(BasePage):

    def expand_shadow_element(self, element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def sign_in_to_site(self, email, password, browser):  # авторизация - верные данные
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        email_input = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_EMAIL)
        password_input = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_PASSWORD)
        email_input.send_keys(email)
        password_input.send_keys(password)
        button = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.AUTH_BUTTON)
        button.click()
        time.sleep(3)

    def should_be_username_logo_in_the_header(self, browser):  # отображение имени Lesa Miller в шапке
        shadow_dom1 = self.expand_shadow_element(browser.find_element_by_tag_name(DashboardPageLocators.SHADOW_TAG))
        username = (shadow_dom1.find_element_by_css_selector(DashboardPageLocators.USERNAME_ON_HEADER)).text
        assert username == "Lesa Miller", f"В шапке либо отсутствует, либо другое имя пользователя - {username} "

    def should_be_message_about_wrong_password(self, browser):  # появление сообщения - неверный пароль
        self.should_be_message_under_sign_in_button(browser)
        self.message_should_be_about_wrong_password(browser)

    def should_be_message_under_sign_in_button(self, browser):  # появление сообщения
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.ALERT_DANGER), "Сообщение не появилось"

    def message_should_be_about_wrong_password(self, browser):  # сообщение о неверном пароле?
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.ALERT_DANGER)).text
        assert message_text == "Wrong password", f"Появившееся сообщение - {message_text}"

    def register_on_the_site(self, sponsor_id, first_name, last_name, email, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        button_sign_up = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.SIGN_UP_BUTTON)
        button_sign_up.click()
        time.sleep(3)
        sponsor_id_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.SPONSOR_ID)
        first_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.FIRST_NAME)
        last_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.LAST_NAME)
        email_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.EMAIL)
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        button_register = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.REGISTER_BUTTON)
        button_register.click()
        time.sleep(3)

    def should_be_message_about_wrong_sponsor_id(self, browser, sponsor_id):
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_wrong_sponsor_id(browser, sponsor_id)

    def should_be_message_in_the_lower_right_corner(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(RegistrationPageLocators.BOTTOM_RIGHT_MESSAGE), "Сообщение в правом нижнем углу не появилось"

    def message_should_be_about_wrong_sponsor_id(self, browser, sponsor_id):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (shadow_dom.find_element_by_css_selector(RegistrationPageLocators.BOTTOM_RIGHT_MESSAGE_TEXT)).text
        assert message_text == f"Sponsor account with Id '{sponsor_id}' not exists", f"Появившееся сообщение - {message_text}"

    def should_be_message_email_already_exists(self, browser):  # переписать
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_email_already_exists(browser)

    def message_should_be_about_email_already_exists(self, browser):  # переписать
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (shadow_dom.find_element_by_css_selector(RegistrationPageLocators.BOTTOM_RIGHT_MESSAGE_TEXT)).text
        assert message_text == "Can not user create." or message_text == "User already exists", f"Появившееся сообщение - {message_text}"

    def should_be_message_about_registration_confirmation_via_email(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        message_text = (
            shadow_dom.find_element_by_css_selector(RegistrationPageLocators.CONFIRM_MESSAGE)).text
        assert message_text == "Аккаунт создан", "Регистрация не была пройдена"

    def email_field_is_not_present(self, browser, timeout=3):  # падает
        try:
            shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
            email_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.EMAIL)
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(email_input))
        except TimeoutException:
            return True
        return False

    def should_be_added_fields_password_and_confirm_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        button_sign_up = shadow_dom.find_element_by_css_selector(AuthorizationPageLocators.SIGN_UP_BUTTON)
        button_sign_up.click()
        self.should_be_added_field_password(browser)
        self.should_be_added_field_confirm_password(browser)

    def should_be_added_field_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_1), "Поле password1 не появилось"

    def should_be_added_field_confirm_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        assert shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_1), "Поле password2 не появилось"

    def success_registration(self, sponsor_id, first_name, last_name, password, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name(AuthorizationPageLocators.SHADOW_TAG))
        sponsor_id_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.SPONSOR_ID)
        first_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.FIRST_NAME)
        last_name_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.LAST_NAME)
        password_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_1)
        password2_input = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.PASSWORD_2)
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        password_input.send_keys(password)
        password2_input.send_keys(password)
        button_register = shadow_dom.find_element_by_css_selector(RegistrationPageLocators.REGISTER_BUTTON)
        button_register.click()
        time.sleep(3)

    def dashboard_should_be_open(self):  # придумать другую проверку
        dashboard_label = self.browser.find_element_by_css_selector(DashboardPageLocators.DASHBOARD_LABEL)
        assert dashboard_label.text == "DASHBOARD", f"заголовок h2 не найден или найден с текстом {dashboard_label.text}"





###################################################################
    # def oalla(self, browser):
    #     shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-online-order"))
    #     product_1 = shadow_dom.find_element_by_css_selector(
    #         "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(1) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > p.text-sm.text-grey-darker.mb-2.product-price")
    #     product_1_price = product_1.text
    #     nums1 = float(re.search(r'\d*\.\d+|\d+', product_1_price).group(0))
    #     # nums1 = re.findall(r'\d*\.\d+|\d+', product_1_price)
    #     # nums1 = [float(i) for i in nums1]
    #     print(nums1)
    #     b1 = shadow_dom.find_element_by_css_selector(
    #         "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(1) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > button")
    #     b1.click()
    #     time.sleep(2)
    #     product_2 = shadow_dom.find_element_by_css_selector(
    #         "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(2) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > p.text-sm.text-grey-darker.mb-2.product-price")
    #     product_2_price = product_2.text
    #     nums2 = float(re.search(r'\d*\.\d+|\d+', product_2_price).group(0))
    #     # nums2 = re.findall(r'\d*\.\d+|\d+', product_2_price)
    #     # nums2 = [float(i) for i in nums2]
    #     print(nums2)
    #     b2 = shadow_dom.find_element_by_css_selector(
    #         "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(2) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > button")
    #     b2.click()
    #     time.sleep(3)
    #     bkorzina = shadow_dom.find_element_by_css_selector("div > button > span > svg")
    #     bkorzina.click()
    #     time.sleep(2)
    #     sum_in_cart = float((shadow_dom.find_element_by_css_selector(
    #         "#step-1 > div > div.mt-6.mx-auto.ml-lg-0.ml-xl-0 > div.content-box.radius-all-6 > div > div:nth-child(2) > div > h1")).text)
    #     print(sum_in_cart)
    #     sum_of_products = nums1 + nums2
    #     print(sum_of_products)
    #     assert sum_of_products == sum_in_cart, f"товар1 это {nums1}, товар2 это {nums2}, сумма в корзине это {float(sum_in_cart)} , сумма по факту это {sum_of_products}"


