from .pages.login_page import LoginPage
import pytest
import time


def test_guest_can_sign_in_with_valid_data(browser):  # 1. авторизация с корректными данными
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email = "user3@example.com"
    password = "password_0"
    page.sign_in_to_site(email, password, browser)
    page.should_be_username_logo_in_the_header(browser)


def test_guest_cant_sign_in_with_invalid_password(browser):  # 2. авторизация с неверным паролем
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email = "user3@example.com"
    password = "password_012345"
    page.sign_in_to_site(email, password, browser)
    page.should_be_message_about_wrong_password(browser)


def test_guest_cant_register_with_invalid_sponsor_id(browser):  # 3. регистрация с неверным спонсор айди
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "0900"
    first_name = "Ivan"
    last_name = "Ivanov"
    email = "user10@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_wrong_sponsor_id(browser, sponsor_id)


def test_guest_cant_register_with_an_existing_email(browser):  # 4. регистрация с уже сущ. емейлом
    link = "https://dev-vkhvorostov.onlineoffice.pro/ru-RU"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "2"
    first_name = "Iva"
    last_name = "Ivanov"
    email = "user4@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_email_already_exists(browser)  # доделать


def test_guest_can_register_with_valid_data(browser):  # 5. успешная регистрация
    link = "https://dev-vkhvorostov.onlineoffice.pro/ru-RU"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "2"
    first_name = "Maria"
    last_name = "Ivanova"
    email = "my@my"  # письмо отправляется на ящик с ошибкой
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_registration_confirmation_via_email(browser)  # доделать


@pytest.mark.testing
def test_id_as_login(browser):
    link = "https://dev-vkhvorostov.mlmsoft.com/admin/settings/global-settings"
    page = LoginPage(browser, link)
    page.open()
    email = "admin@mlm-soft.com"
    password = "9UA27VF2W2Bwn7Jo"
    page.sign_in_configurator(email, password, browser)
    page.select_login_type__id_as_login(browser)
    page.select_password_creation_type__by_user(browser)
    page.save_changes_to_global_settings(browser)
    time.sleep(3)
    ##
    link_2 = "https://dev-vkhvorostov.mlmsoft.com/admin/accounts/profile-fields"
    page_2 = LoginPage(browser, link_2)
    page_2.open()
    page_2.uncheck_email_field(browser)
    time.sleep(3)
    ##
    link_3 = "https://dev-vkhvorostov.onlineoffice.pro/admin/themes/monarch"
    page_3 = LoginPage(browser, link_3)
    page_3.open()
    page_3.sign_in_admin_cabinet(email, password, browser)
    page_3.select_login_validation_type__account_id(browser)
    page_3.save_changes_to_admin_cabinet(browser)
    ##
    link_4 = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page_4 = LoginPage(browser, link_4)
    page_4.open()
    time.sleep(10)
    page.should_be_added_fields_password_and_confirm_password(browser)
    #page_4.email_field_is_not_present(browser)
    sponsor_id = "2"
    first_name = "Bator"
    last_name = "Ivanov"
    password = "AwsEdrFtgY65Hu764"
    page_4.success_registration(sponsor_id, first_name, last_name, password, browser)
    time.sleep(10)
    page_4.dashboard_should_be_open(browser)
    time.sleep(3)


#@pytest.mark.testing
#def test_prob(browser):


