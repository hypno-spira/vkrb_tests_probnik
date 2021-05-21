from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium import webdriver


class CabinetLocators(BasePage):
    CABINET_TAG_1 = "v-online-order"
    BUTTON_1 = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(1) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > button"


class AuthorizationPageLocators(BasePage):
    SHADOW_TAG = "v-api2-middleware"
    AUTH_EMAIL = "input#login.form-control"
    AUTH_PASSWORD = "input#password.form-control"
    AUTH_BUTTON = "#buttonLogin"
    ALERT_DANGER = "div.alert.alert-danger"
    SIGN_UP_BUTTON = "#formLogin>div>h3>span.header-buttons>a"


class DashboardPageLocators(BasePage):
    SHADOW_TAG = "v-user-pop"
    USERNAME_ON_HEADER = "span.span-name"
    DASHBOARD_LABEL = "#page-title > h2"


class RegistrationPageLocators(BasePage):
    SPONSOR_ID = "#lf-ref"
    FIRST_NAME = "#lf-4"
    LAST_NAME = "#lf-5"
    EMAIL = "#lf-6"
    BOTTOM_RIGHT_MESSAGE = "div>div.snotifyToast__inner"
    BOTTOM_RIGHT_MESSAGE_TEXT = "div.snotifyToast__body"
    CONFIRM_MESSAGE = "#formLogin>div>div.content-box-wrapper>div>strong"
    PASSWORD_1 = "#password1_reg"
    PASSWORD_2 = "#password2_reg"
    REGISTER_BUTTON = "#buttonRegister"


class AdminCabinetAuthLocators(BasePage):
    EMAIL = "#adminuserloginform-email"
    PASSWORD = "#adminuserloginform-password"
    LOGIN_BUTTON = "#login-form>div>div.button-pane>button"
    LOGIN_TYPE_SELECT = "#globalsettingsform-login_type"
    PASS_CREATION_TYPE_SELECT = "#globalsettingsform-password_creation_type"
    BUTTON_SUBMIT = "#w0>div.panel-footer>div>div>button.btn.btn-success"
    EMAIL_CHECKBOX = "#profileFieldsGrid-container>table>tbody>tr:nth-child(3)>td:nth-child(4)>input[type=checkbox]"


class AdminMonarchSettingsLocators(BasePage):
    EMAIL = "#admin-login>form>div>div:nth-child(1)>div>div.form-data.block.size-2-3>div>input[type=text]"
    PASSWORD = "#admin-login>form>div>div:nth-child(2)>div>div.form-data.block.size-2-3>div>input[type=password]"
    BUTTON_LOGIN = "#admin-login>form>div>div.form-actions.primary-accent>button"
    REGISTRATION_TAB = "#blueprints > div > div > div.tabs-nav > a:nth-child(3)"
    DIV = "#tab-style_tab\.core_tab\.registration_tab3 > div > div:nth-child(8) > div.form-data.block.size-2-3 > div > div > div.selectize-input.items.full.has-options.has-items"
    DIV_ACTIVE = "#tab-style_tab\.core_tab\.registration_tab3 > div > div:nth-child(8) > div.form-data.block.size-2-3 > div > div > div.selectize-input.items.has-options.full.has-items > input[type=select-one]"
    SAVE_BUTTON = "#titlebar > div > button"

