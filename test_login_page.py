from .pages.login_page import LoginPage
from .pages.global_settings_page import GlobalSettingsPage
from .pages.profile_field_settings_page import ProfileFieldSettingsPage
from .pages.admin_personal_account_settings_page import AdminPersonalAccountSettingsPage
from .pages.online_order_page import OnlineOrderPage
import pytest
import time
import allure
from allure_commons.types import AttachmentType


@allure.feature('authorization')
@allure.story("Авторизация пользователя с корректными данными")
@allure.severity("critical")
def test_guest_can_sign_in_with_valid_data(browser):  # 1. авторизация с корректными данными
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email, password = "user3@example.com", "password_0"
    page.sign_in_to_site(email, password, browser)
    page.should_be_username_logo_in_the_header(browser)


@allure.feature('authorization')
@allure.story("Авторизация пользователя с неверным паролем")
@allure.severity("critical")
def test_guest_cant_sign_in_with_invalid_password(browser):  # 2. авторизация с неверным паролем
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email, password = "user3@example.com", "password_012345"
    page.sign_in_to_site(email, password, browser)
    with allure.step("Делаем скриншот"):
        allure.attach(browser.get_screenshot_as_png(), name="Screenshot wrong password",
                      attachment_type=AttachmentType.PNG)
    page.should_be_message_about_wrong_password(browser)


@allure.feature('registration')
@allure.story("Регистрация пользователя с неверным sponsor id")
@allure.severity("critical")
def test_guest_cant_register_with_invalid_sponsor_id(browser):  # 3. регистрация с неверным спонсор айди
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id, first_name, last_name, email = "0900", "Ivan", "Ivanov", "user10@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_wrong_sponsor_id(browser, sponsor_id)



@allure.feature('registration')
@allure.story("Регистрация пользователя с уже существующим email")
@allure.severity("critical")
def test_guest_cant_register_with_an_existing_email(browser):  # 4. регистрация с уже сущ. емейлом
    link = "https://dev-vkhvorostov.onlineoffice.pro/ru-RU"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id, first_name, last_name, email = "2", "Ivvvan", "Ivanov", "user4@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_email_already_exists(browser)  # доделать


@allure.feature('registration')
@allure.story("Успешная регистрация пользователя")
@allure.severity("critical")
def test_guest_can_register_with_valid_data(browser):  # 5. успешная регистрация
    link = "https://dev-vkhvorostov.onlineoffice.pro/ru-RU"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id, first_name, last_name, email = "2", "Marina", "Ivanova", "mukeuy@my.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_registration_confirmation_via_email(browser)  # доделать


@allure.feature("authorization")
@allure.story("Тест ID as Login")
@allure.severity("critical")
def test_id_as_login(browser):
    link = "https://dev-vkhvorostov.mlmsoft.com/admin/settings/global-settings"
    global_settings_page = GlobalSettingsPage(browser, link)
    global_settings_page.open()
    email, password = "admin@mlm-soft.com", "9UA27VF2W2Bwn7Jo"
    global_settings_page.sign_in_configurator(email, password)
    global_settings_page.select_login_type__id_as_login()
    global_settings_page.select_password_creation_type__by_user()
    global_settings_page.save_changes_to_global_settings()
    time.sleep(3)
    # переход к настройкам Profile Fields
    link = "https://dev-vkhvorostov.mlmsoft.com/admin/accounts/profile-fields"
    profile_field_settings_page = ProfileFieldSettingsPage(browser, link)
    profile_field_settings_page.open()
    profile_field_settings_page.uncheck_email_field()
    time.sleep(3)
    # переход к настройкам admin/themes/monarch
    link = "https://dev-vkhvorostov.onlineoffice.pro/admin/themes/monarch"
    admin_personal_account_settings_page = AdminPersonalAccountSettingsPage(browser, link)
    admin_personal_account_settings_page.open()
    admin_personal_account_settings_page.sign_in_admin_cabinet(email, password)
    admin_personal_account_settings_page.select_login_validation_type__account_id()
    admin_personal_account_settings_page.save_changes_to_admin_cabinet()
    # переход к странице входа-регистрации
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    login_page = LoginPage(browser, link)
    login_page.open()
    login_page.should_be_added_fields_password_and_confirm_password(browser)
    # login_page.email_field_is_not_present(browser) - дописать рабочий метод или удалить
    sponsor_id, first_name, last_name, password = "2", "Antony", "Petrov", "AwsEgyudcjdigY65Hfuf764"
    login_page.success_registration(sponsor_id, first_name, last_name, password, browser)
    time.sleep(10)  # без явного ожидания страница не успевает загрузиться и тест падает
    login_page.dashboard_should_be_open()
    time.sleep(3)


