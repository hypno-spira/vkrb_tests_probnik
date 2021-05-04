from .base_page import BasePage
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):

    def expand_shadow_element(self, element):
        shadow_root = self.browser.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def sign_in_to_site(self, email, password, browser):  # заполнение верными данными
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        email_input = shadow_dom.find_element_by_css_selector("input#login.form-control")
        password_input = shadow_dom.find_element_by_css_selector("input#password.form-control")
        email_input.send_keys(email)
        password_input.send_keys(password)
        button = shadow_dom.find_element_by_css_selector("button#buttonLogin.btn.btn-success.btn-block")
        button.click()
        time.sleep(3)

    def should_be_username_logo_in_the_header(self, browser):
        shadow_dom1 = self.expand_shadow_element(browser.find_element_by_tag_name("v-user-pop"))
        assert shadow_dom1.find_element_by_css_selector("span.span-name"), "В шапке нет имени пользователя - вход не выполнен"

    def should_be_message_about_wrong_password(self, browser):
        self.should_be_message_under_sign_in_button(browser)
        self.message_should_be_about_wrong_password(browser)

    def should_be_message_under_sign_in_button(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        assert shadow_dom.find_element_by_css_selector("div.alert.alert-danger"), "Сообщение не появилось"

    def message_should_be_about_wrong_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        message_text = (shadow_dom.find_element_by_css_selector("div.alert.alert-danger")).text
        assert message_text == "Wrong password", f"Появившееся сообщение - {message_text}"

    def register_on_the_site(self, sponsor_id, first_name, last_name, email, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        button_sign_up = shadow_dom.find_element_by_css_selector("#formLogin>div>h3>span.header-buttons>a")
        button_sign_up.click()
        time.sleep(3)
        sponsor_id_input = shadow_dom.find_element_by_css_selector("#lf-ref")
        first_name_input = shadow_dom.find_element_by_css_selector("#lf-4")
        last_name_input = shadow_dom.find_element_by_css_selector("#lf-5")
        email_input = shadow_dom.find_element_by_css_selector("#lf-6")
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        email_input.send_keys(email)
        button_register = shadow_dom.find_element_by_css_selector("#buttonRegister")
        button_register.click()
        time.sleep(3)

    def should_be_message_about_wrong_sponsor_id(self, browser, sponsor_id):
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_wrong_sponsor_id(browser, sponsor_id)

    def should_be_message_in_the_lower_right_corner(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        assert shadow_dom.find_element_by_css_selector("div>div.snotifyToast__inner"), "Сообщение в правом нижнем углу не появилось"

    def message_should_be_about_wrong_sponsor_id(self, browser, sponsor_id):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        message_text = (shadow_dom.find_element_by_css_selector("div.snotifyToast__body")).text
        assert message_text == f"Sponsor account with Id '{sponsor_id}' not exists", f"Появившееся сообщение - {message_text}"

    def should_be_message_email_already_exists(self, browser): # переписать
        # shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        # message_text = (shadow_dom.find_element_by_css_selector("#formLogin>div>div.content-box-wrapper>div>strong")).text
        # assert message_text != "Аккаунт создан", "Регистрация не должна проходить"
        self.should_be_message_in_the_lower_right_corner(browser)
        self.message_should_be_about_email_already_exists(browser)

    def message_should_be_about_email_already_exists(self, browser): # переписать
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        message_text = (shadow_dom.find_element_by_css_selector("div.snotifyToast__body")).text
        assert message_text == "Can not user create.", f"Появившееся сообщение - {message_text}"

    def should_be_message_about_registration_confirmation_via_email(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        message_text = (shadow_dom.find_element_by_css_selector("#formLogin>div>div.content-box-wrapper>div>strong")).text
        assert message_text == "Аккаунт создан", "Регистрация не была пройдена"


    def sign_in_configurator(self, email, password, browser):
        email_input = browser.find_element_by_css_selector("#adminuserloginform-email")
        email_input.send_keys(email)
        password_input = browser.find_element_by_css_selector("#adminuserloginform-password")
        password_input.send_keys(password)
        button_login = browser.find_element_by_css_selector("#login-form>div>div.button-pane>button")
        button_login.click()

    def select_login_type__id_as_login(self, browser):
        select = Select(browser.find_element_by_css_selector("#globalsettingsform-login_type"))
        select.select_by_visible_text("ID As Login")  # выбираем элемент с текстом "ID As Login"

    def select_password_creation_type__by_user(self, browser):
        select = Select(browser.find_element_by_css_selector("#globalsettingsform-password_creation_type"))
        select.select_by_visible_text("By User")  # выбираем элемент с текстом "By User"

    def save_changes_to_global_settings(self, browser):
        button_submit = browser.find_element_by_css_selector("#w0>div.panel-footer>div>div>button.btn.btn-success")
        button_submit.click()

    def uncheck_email_field(self, browser):
        email_checkbox = browser.find_element_by_css_selector("#profileFieldsGrid-container>table>tbody>tr:nth-child(3)>td:nth-child(4)>input[type=checkbox]")
        email_checkbox.click()

    def sign_in_admin_cabinet(self, email, password, browser):
        email_input = browser.find_element_by_css_selector("#admin-login>form>div>div:nth-child(1)>div>div.form-data.block.size-2-3>div>input[type=text]")
        email_input.send_keys(email)
        password_input = browser.find_element_by_css_selector("#admin-login>form>div>div:nth-child(2)>div>div.form-data.block.size-2-3>div>input[type=password]")
        password_input.send_keys(password)
        button_login = browser.find_element_by_css_selector("#admin-login>form>div>div.form-actions.primary-accent>button")
        button_login.click()

    def select_login_validation_type__account_id(self, browser):
        registration_tab = browser.find_element_by_css_selector("#blueprints > div > div > div.tabs-nav > a:nth-child(3)")
        registration_tab.click()
        div = browser.find_element_by_css_selector("#tab-style_tab\.core_tab\.registration_tab3 > div > div:nth-child(8) > div.form-data.block.size-2-3 > div > div > div.selectize-input.items.full.has-options.has-items")
        div.click()
        div = browser.find_element_by_css_selector("#tab-style_tab\.core_tab\.registration_tab3 > div > div:nth-child(8) > div.form-data.block.size-2-3 > div > div > div.selectize-input.items.has-options.full.has-items > input[type=select-one]")
        div.send_keys(Keys.BACKSPACE)
        div.send_keys("Account ID" + Keys.ENTER)
        time.sleep(3)

    def save_changes_to_admin_cabinet(self, browser):
        button_save = browser.find_element_by_css_selector("#titlebar > div > button")
        button_save.click()

    def email_field_is_not_present(self, browser, timeout=3):
        try:
            shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
            email_input = shadow_dom.find_element_by_css_selector("#lf-6")
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located(email_input))
        except TimeoutException:
            return True
        return False

    def should_be_added_fields_password_and_confirm_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        button_sign_up = shadow_dom.find_element_by_css_selector("#formLogin > div > h3 > span.header-buttons > a")
        button_sign_up.click()
        self.should_be_added_field_password(browser)
        self.should_be_added_field_confirm_password(browser)

    def should_be_added_field_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        assert shadow_dom.find_element_by_css_selector("#password1_reg"), "Поле password1 не появилось"

    def should_be_added_field_confirm_password(self, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        assert shadow_dom.find_element_by_css_selector("#password2_reg"), "Поле password2 не появилось"

    def success_registration(self, sponsor_id, first_name, last_name, password, browser):
        shadow_dom = self.expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
        sponsor_id_input = shadow_dom.find_element_by_css_selector("#lf-ref")
        first_name_input = shadow_dom.find_element_by_css_selector("#lf-4")
        last_name_input = shadow_dom.find_element_by_css_selector("#lf-5")
        password_input = shadow_dom.find_element_by_css_selector("#password1_reg")
        password2_input = shadow_dom.find_element_by_css_selector("#password2_reg")
        sponsor_id_input.send_keys(sponsor_id)
        first_name_input.send_keys(first_name)
        last_name_input.send_keys(last_name)
        password_input.send_keys(password)
        password2_input.send_keys(password)
        button_register = shadow_dom.find_element_by_css_selector("#buttonRegister")
        button_register.click()
        time.sleep(3)

    def dashboard_should_be_open(self, browser):
        dashboard_label = browser.find_element_by_css_selector("#page-title > h2")
        assert dashboard_label.text == "DASHBOARD", f"найден заголовок h2 с текстом {dashboard_label.text}"



