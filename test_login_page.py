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


def test_guest_cant_sign_in_with_invalid_password(browser):
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    email = "user3@example.com"
    password = "password_012345"
    page.sign_in_to_site(email, password, browser)
    page.should_be_message_about_wrong_password(browser)

def test_guest_cant_register_with_invalid_sponsor_id(browser):
    link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"
    page = LoginPage(browser, link)
    page.open()
    sponsor_id = "0900"
    first_name = "Ivan"
    last_name = "Ivanov"
    email = "user10@example.com"
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_wrong_sponsor_id(browser)
