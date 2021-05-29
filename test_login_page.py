import time
import allure
import pytest
from .pages.login_page import LoginPage
from .pages.global_settings_page import GlobalSettingsPage
from .pages.profile_field_settings_page import ProfileFieldSettingsPage
from .pages.admin_personal_account_settings_page import AdminPersonalAccountSettingsPage
from .pages.links import Links
from .pages.testdata import CorrectData, IncorrectData
from allure_commons.types import AttachmentType


@pytest.mark.authorization
@pytest.mark.authorization_1
@allure.feature("Авторизация в OnlineOffice")
@allure.story("№1. Авторизация пользователя с корректными данными")
@allure.severity("critical")
def test_guest_can_sign_in_with_valid_data(browser):
    page = LoginPage(browser, Links.DASHBOARD_LINK)
    page.open()
    email = CorrectData.EMAIL_ID3
    password = CorrectData.PASSWORD
    page.sign_in_to_site(email, password, browser)
    page.dashboard_should_be_open(browser)
    with allure.step("Dashboard should be open"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Dashboard Screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.authorization
@pytest.mark.authorization_2
@allure.feature("Авторизация в OnlineOffice")
@allure.story("№2. Авторизация пользователя с неверным паролем")
@allure.severity("critical")
def test_guest_cant_sign_in_with_invalid_password(browser):
    page = LoginPage(browser, Links.DASHBOARD_LINK)
    page.open()
    email = CorrectData.EMAIL_ID3
    password = IncorrectData.PASSWORD
    page.sign_in_to_site(email, password, browser)
    page.should_be_message_about_wrong_password(browser)
    with allure.step("Should be message wrong password"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Wrong password message Screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.registration
@pytest.mark.registration_1
@allure.feature("Регистрация в OnlineOffice")
@allure.story("№3. Регистрация пользователя с неверно указанным Sponsor ID")
@allure.severity("critical")
def test_guest_cant_register_with_invalid_sponsor_id(browser):
    page = LoginPage(browser, Links.DASHBOARD_LINK)
    page.open()
    sponsor_id = IncorrectData.SPONSOR_ID
    first_name = CorrectData.FIRST_NAME
    last_name = CorrectData.LAST_NAME
    email = CorrectData.EMAIL_FOR_REG
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_wrong_sponsor_id(browser, sponsor_id)
    with allure.step("Should be message wrong sponsor id"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Wrong sponsor id message Screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.registration
@pytest.mark.registration_2
@allure.feature("Регистрация в OnlineOffice")
@allure.story("№4. Регистрация пользователя с указанием уже существующего email")
@allure.severity("critical")
def test_guest_cant_register_with_an_existing_email(browser):
    page = LoginPage(browser, Links.DASHBOARD_LINK)
    page.open()
    sponsor_id = CorrectData.SPONSOR_ID
    first_name = CorrectData.FIRST_NAME
    last_name = CorrectData.LAST_NAME
    email = CorrectData.EMAIL_ID3
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_email_already_exists(browser)
    with allure.step("Should be message email already exist"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Email already exist message Screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.registration
@pytest.mark.registration_3
@allure.feature("Регистрация в OnlineOffice")
@allure.story("№5. Успешная регистрация пользователя")
@allure.severity("critical")
def test_guest_can_register_with_valid_data(browser):
    page = LoginPage(browser, Links.DASHBOARD_LINK)
    page.open()
    sponsor_id = CorrectData.SPONSOR_ID
    first_name = CorrectData.FIRST_NAME
    last_name = CorrectData.LAST_NAME
    email = CorrectData.EMAIL_FOR_REG
    page.register_on_the_site(sponsor_id, first_name, last_name, email, browser)
    page.should_be_message_about_registration_confirmation_via_email(browser)
    with allure.step("Should be message User created"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="User created message Screenshot", attachment_type=AttachmentType.PNG)


@pytest.mark.xfail
@pytest.mark.id_as_login
@allure.feature("Тест ID as Login")
@allure.story("Тест ID as Login")
@allure.severity("normal")
def test_id_as_login(browser):
    page = GlobalSettingsPage(browser, Links.GLOBAL_SETTINGS_LINK)  # переход к настройкам Global Settings
    page.open()
    email = CorrectData.ADMIN_EMAIL
    password = CorrectData.ADMIN_PASSWORD
    page.sign_in_configurator(email, password)
    page.select_login_type__id_as_login()
    page.select_password_creation_type__by_user()
    page.save_changes_to_global_settings()
    time.sleep(3)
    page = ProfileFieldSettingsPage(browser, Links.PROFILE_FIELDS_SETTINGS_LINK)  # переход к настройкам Profile Fields
    page.open()
    page.uncheck_email_field()
    time.sleep(3)
    page = AdminPersonalAccountSettingsPage(browser, Links.ADMIN_PERSONAL_ACCOUNT_SETTINGS_LINK)  # переход к настройкам admin/themes/monarch
    page.open()
    page.sign_in_admin_cabinet(email, password)
    page.select_login_validation_type__account_id()
    page.save_changes_to_admin_cabinet()
    page = LoginPage(browser, Links.DASHBOARD_LINK)  # переход к странице входа-регистрации
    page.open()
    page.should_be_added_fields_password_and_confirm_password(browser)
    with allure.step("Should be added password fields"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Password fields Screenshot", attachment_type=AttachmentType.PNG)
    sponsor_id = CorrectData.SPONSOR_ID
    first_name = CorrectData.FIRST_NAME
    last_name = CorrectData.LAST_NAME
    password = CorrectData.PASSWORD_FOR_REG
    page.success_registration(sponsor_id, first_name, last_name, password, browser)
    time.sleep(10)
    page.dashboard_should_be_open(browser)
    with allure.step("Dashboard should be open"):
        allure.attach(browser.get_screenshot_as_png(),
                      name="Dashboard Screenshot", attachment_type=AttachmentType.PNG)
    time.sleep(3)
