from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.HomePage import HomePage


class LoginPage(BasePage):

    USERNAME = (By.XPATH,"//input[@name='username']")
    PASSWORD = (By.XPATH,"//input[@name='password']")
    Login_btn = (By.XPATH,"//button[@type='submit']")
    Forget_password = (By.XPATH,"//p[@class='oxd-text oxd-text--p orangehrm-login-forgot-header']")

    def __init__(self,driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_loginPage_title(self,title):
        return self.get_title(title)

    def is_forget_password_link_exist(self):
        return self.is_visible(self.Forget_password)

    def do_login(self,username,password):
        self.do_sendkeys(self.USERNAME,username)
        self.do_sendkeys(self.PASSWORD,password)
        self.do_click(self.Login_btn)
        return HomePage(self.driver)
