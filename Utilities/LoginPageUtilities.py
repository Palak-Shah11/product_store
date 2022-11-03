import config.credential as cd

from Utilities.common_utilities import CommonUtilities
import Locators.LoginPageLocators as lpl
import Locators.HomePageLocators as hpl


class LoginPageUtilities(CommonUtilities):

    def perform_login(self, uname, pswrd):
        self.fill_uname(uname)
        self.fill_pswrd(pswrd)
        self.click_such_elements()
        self.click_login_btn()
        self.get_alert_text()

    def fill_uname(self, uname):
        self.send_text(lpl.username_fill, uname)

    def fill_pswrd(self, pswrd):
        self.send_text(lpl.pswrd_fill, pswrd)

    def click_such_elements(self):
        self.click_element(lpl.about_us)
        self.click_element(lpl.btn_to_close_about)
        self.click_element(lpl.btn_to_go_on_login_page)

    def click_login_btn(self):
        self.click_element(lpl.login_btn)

    def click_laptop(self):
        self.click_element(hpl.go_to_laptops)

    def login_successfully(self):
        self.click_such_elements()
        self.fill_uname(cd.valid_uname)
        self.fill_pswrd(cd.valid_pswrd)
        self.click_login_btn()


