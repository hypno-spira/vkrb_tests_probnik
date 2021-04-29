from .pages.login_page import LoginPage
import pytest


def test_guest_can_sign_in_with_valid_data(browser):  # 1. авторизация с корректными данными
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email = "user3@example.com"
    password = "password_0"
    page.sign_in_to_site(email, password, browser)
    page.should_be_username_logo_in_the_header(browser)


def test_guest_cant_sign_in_with_invalid_password(browser): # 2. авторизация с неверным паролем
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email = "user3@example.com"
    password = "password_012345"
    page.sign_in_to_site(email, password, browser)
    page.should_be_message_about_wrong_password(browser)



def test_guest_cant_register_with_invalid_sponsor_id(browser): # 3. регистрация с неверным спонсор айди
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "0900"
    first_name = "Ivan"
    last_name = "Ivanov"
    email = "user10@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_wrong_sponsor_id(browser, sponsor_id)


def test_guest_cant_register_with_an_existing_email(browser): # 4. регистрация с уже сущ. емейлом
    link = "https://dev-vkhvorostov.onlineoffice.pro/ru-RU"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "2"
    first_name = "Iva"
    last_name = "Ivanov"
    email = "user4@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_email_already_exists(browser)  # доделать

@pytest.mark.testing
def test_guest_can_register_with_valid_data(browser): #5. успешная регистрация
    link = "https://dev-vkhvorostov.onlineoffice.pro/ru-RU"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "2"
    first_name = "Maria"
    last_name = "Ivanova"
    email = "usertest@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_registration_confirmation_via_email(browser)  # доделать
