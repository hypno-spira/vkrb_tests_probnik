import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
import time

link = "https://dev-vkhvorostov.onlineoffice.pro/en-US"


def expand_shadow_element(element):
    shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


def is_element_present(how):
    try:
        browser.find_element(how)
    except NoSuchElementException:
        return False
    return True


browser = webdriver.Chrome()
browser.get(link)

shadow_dom = expand_shadow_element(browser.find_element_by_tag_name("v-api2-middleware"))

email_field = shadow_dom.find_element_by_css_selector("input#login.form-control")
email_field.send_keys("user3@example.com")
password_field = shadow_dom.find_element_by_css_selector("input#password.form-control")
password_field.send_keys("password_000")

btn = shadow_dom.find_element_by_css_selector("button#buttonLogin.btn.btn-success.btn-block")
btn.click()
time.sleep(2)
wrong_pass = (shadow_dom.find_element_by_css_selector("div.alert.alert-danger")).text

# тут неверная проверка, надо проверить не просто текст в сообщении, а то,
# что сообщение появилось и какой в нем текст

assert wrong_pass == "Wrong password", "либо не то сообщение, либо его нет"
browser.quit()
