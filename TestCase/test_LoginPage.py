import pytest
from TestCase.test_Base import BaseTest
from Pages.LoginPage import LoginPage
from Config.config import TestData
import time


class Test_Login(BaseTest):
    def test_forgetPassword_visible(self):
        self.loginpage = LoginPage(self.driver)
        flag = self.loginpage.is_forget_password_link_exist()
        print(bool(flag))
        assert flag

    def test_loginPage_title(self):
        self.loginpage = LoginPage(self.driver)
        print(self.loginpage.get_title(TestData.Loginpage_title))
        print("PASS")

    def test_Login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.PASSWORD)
        time.sleep(3)
        print(" Test Pass")
