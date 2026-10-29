from selenium.webdriver.common.by import By
from .base_page import BasePage

class LobbyLoginPage(BasePage):
    USERNAME_FIELD = (By.ID, 'username')
    LOGIN_BUTTON = (By.ID, 'btn-login')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message')

    def login(self, username):
        self.enter_text(self.USERNAME_FIELD, username)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.find_element(self.ERROR_MESSAGE).text
