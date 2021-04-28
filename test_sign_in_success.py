import pytest
from selenium import webdriver
import time

link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"


def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

browser = webdriver.Chrome()
browser.get(link)

shadow_dom = expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))

email_field = shadow_dom.find_element_by_css_selector("input#login.form-control")
email_field.send_keys("user3@example.com")
password_field = shadow_dom.find_element_by_css_selector("input#password.form-control")
password_field.send_keys("password_0")

btn = shadow_dom.find_element_by_css_selector("button#buttonLogin.btn.btn-success.btn-block")
btn.click()

# переопределить на новой странице
shadow_dom = expand_shadow_element(browser.find_element_by_tag_name("v-user-pop"))
time.sleep(5)
user_name = (shadow_dom.find_element_by_css_selector("span.span-name")).text

assert user_name == "Lesa Miller", "регистрация не прошла"
browser.quit()
