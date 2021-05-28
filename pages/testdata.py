from .base_page import BasePage
import time


class CorrectData(BasePage):
    EMAIL_ID3 = "user3@example.com"
    EMAIL_ID4 = "user4@example.com"
    EMAIL_ID5 = "user5@example.com"
    EMAIL_ID6 = "user6@example.com"
    PASSWORD = "password_0"
    FIRST_NAME = "Ivan"
    LAST_NAME = "Ivanov"
    EMAIL_FOR_REG = str(time.time()) + "@example.com"
    SPONSOR_ID = "2"
    ADMIN_EMAIL = "admin@mlm-soft.com"
    ADMIN_PASSWORD = "9UA27VF2W2Bwn7Jo"
    PASSWORD_FOR_REG = str(time)


class IncorrectData(BasePage):
    PASSWORD = "password_012345"
    SPONSOR_ID = "0900"
