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
    LANGUAGE_BUTTON = "#__BVID__20__BV_toggle_"
    LANGUAGE_ENG = "#__BVID__20 > ul > li:nth-child(1) > a"


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


class OnlineOrderPageLocators(BasePage):
    ONLINE_ORDER_TAG = "v-online-order"
    ONLINE_ORDER_HISTORY_TAG = "v-online-order-history"
    BUTTON_1 = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(1) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > button"
    BUTTON_2 = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(2) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > button"
    BUTTON_3 = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(3) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > button"
    QUANTITY = "div > button > span > p"
    PRODUCT_1_PRICE = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(1) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > p.text-sm.text-grey-darker.mb-2.product-price"
    PRODUCT_2_PRICE = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(2) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > p.text-sm.text-grey-darker.mb-2.product-price"
    PRODUCT_3_PRICE = "#app > div > div.body > div > div > div > div > div.flex.flex-wrap.overflow-y-hidden > div:nth-child(3) > div > div.shadow-lg.rounded-lg.overflow-hidden.bg-white > div.p-3 > p.text-sm.text-grey-darker.mb-2.product-price"
    CART_BUTTON = "div > button > span > svg"
    CART_PRICE = "#step-1 > div > div.mt-6.mx-auto.ml-lg-0.ml-xl-0 > div.content-box.radius-all-6 > div > div:nth-child(2) > div > h1"
    BUTTON_F1T2_STEP = "#step-1 > div > div.mt-6.mx-auto.ml-lg-0.ml-xl-0 > div.row > div:nth-child(2) > button"
    ADDRESS = "#step-2 > div > div:nth-child(1) > div:nth-child(1) > div > div.checkout-address > input"
    PICK_UP_RADIO = "#__BVID__169 > div:nth-child(2) > label"
    BUTTON_F2T3_STEP = "#step-2 > div > div.mt-6.mx-auto.ml-lg-0.ml-xl-0 > div.row > div:nth-child(2) > button"
    TEST_GATEWAY_RADIO = "#radio-group-1 > div:nth-child(4) > label"
    AGREE_CHECKBOX = "div.custom-control.custom-checkbox"
    PROCEED_TO_CHECK_OUT = "#step-3 > div > div.mt-6.mx-auto.ml-lg-0.ml-xl-0 > div.row > div:nth-child(2) > button"
    SUCCESSFUL_PAYMENT_BUTTON = "body > div > form > button.btn.btn-primary"
    RETURN_BUTTON = "body > div > form > button.btn.btn-secondary"
    BOTTOM_RIGHT_MESSAGE = "div>div.snotifyToast__inner"
    ICON_SUCCESS = ".snotify-icon.snotify-icon--success"
    ICON_WARNING = ".snotify-icon.snotify-icon--warning"
    LAST_ORDER_ID = "tr:nth-child(1) > td:nth-child(1)"
    ONLINE_ORDER_LINK = "#sidebar-menu > li:nth-child(6) > a"
    NEW_ORDER_STATUS = "#__BVID__20 > tbody > tr:nth-child(1) > td:nth-child(5) > span"
    ORDER_HISTORY_LINK = "#sidebar-menu > li:nth-child(7) > a"
    UNSUCCESSFUL_PAYMENT_CHECKBOX = "body > div > form > div > div:nth-child(2) > label"
    TRANSFER_WALLET_TAG = "v-account-to-account"
    BONUS_WALLET = "div > div > div.plan-price"
    RECIPIENT_INPUT = "#input-search"
    RECIPIENT_FIRST_LINE = "#__BVID__27 > tbody > tr:nth-child(1)"
    AMOUNT_TO_TRANSFER_INPUT = "#id_amount_input"
    BUTTON_SUBMIT = "div > div > div.panel > div > form > div.button-pane.mrg20T > button.btn.btn-primary"
    LOGOUT_TAB = "#sidebar-menu > li.no-menu > span > a"



class AdminInvoicesPageLocators(BasePage):
    ORDER_ID_IN_THE_FIRST_LINE = "#invoice-grid-container > table > tbody > tr:nth-child(1) > td:nth-child(1) > a"
    STATUS_IN_THE_FIRST_LINE = "#invoice-grid-container > table > tbody > tr:nth-child(1) > td:nth-child(5)"



