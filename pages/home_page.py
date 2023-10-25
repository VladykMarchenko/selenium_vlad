from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def username_input_field(self):
        return self.driver.find_element(By.ID, 'login')

    @property
    def password_input_field(self):
        return self.driver.find_element(By.ID, 'password')

    @property
    def login_button(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[type=submit] > div')

    def setting_menu_group(self):
        self.driver.find_element(By.CSS_SELECTOR, '[data-cid="settings_menu_group"]').click()

    def navigate(self):
        self.driver.get('https://web.remonline.app/')

    def enter_username(self, username):
        self.username_input_field.send_keys(username)

    def enter_password(self, valid_password):
        self.password_input_field.send_keys(valid_password)

    def click_login_button(self):
        self.login_button.click()

    def click_subscription(self):
        self.driver.find_element(By. CSS_SELECTOR, '[data-cid="payments_menu_group"]').click()

    def incorrect_login_or_password(self):
        self.driver.find_element(By. CSS_SELECTOR, '[data-cid="error-login"]')




