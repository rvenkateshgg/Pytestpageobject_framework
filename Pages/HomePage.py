from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from Config.config import TestData


class HomePage(BasePage):

    Admin_lnk = (By.XPATH,"//li[@class='oxd-main-menu-item-wrapper']")

    def __int__(self,driver):
        super().__int__(driver)

    def Click_Admin(self):
        self.do_click(self.Admin_lnk)

