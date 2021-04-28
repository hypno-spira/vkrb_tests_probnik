import pytest
from selenium import webdriver
import time

link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"


def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


try:
    browser = webdriver.Chrome()
    browser.get(link)

    outer = expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))
    email_field = outer.find_element_by_css_selector("input#login.form-control")

    # email_field = browser.find_element_by_css_selector("input#login.form-control")
    email_field.send_keys("test")
    password_field = outer.find_element_by_css_selector("input#password.form-control")
    password_field.send_keys("test")

    btn = outer.find_element_by_css_selector("button#buttonLogin.btn.btn-success.btn-block")
    btn.click()

finally:
    time.sleep(70)
    browser.quit()
