import pytest

import config.credential as cd

from Utilities.common_utilities import CommonUtilities
from Utilities.LoginPageUtilities import LoginPageUtilities
from Locators import HomePageLocators as hpl
from conftest import driver


class TestLoginPage:

    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_login_without_entering_uname(self):
        '''
        In this case we will click login button without entering username

        Expected result: alert will generate to fill username

        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.click_such_elements()
        lpu.fill_pswrd(cd.valid_pswrd)
        lpu.click_login_btn()
        cu = CommonUtilities()
        assert cu.get_alert_text() == "Please fill out Username and Password.",\
            "Please fill out Username and Password alert is not generated"
        cu.alert_accept()


    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_login_with_wrong_uname(self):
        '''

        In this case we will click login button with wrong username and correct password

        Expected result: alert will generate to fill username

        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.click_such_elements()
        lpu.fill_uname(cd.invalid_uname)
        lpu.fill_pswrd(cd.valid_pswrd)
        lpu.click_login_btn()
        cu = CommonUtilities()
        assert cu.get_alert_text() == "User does not exist.",\
            "User does not exist alert is not generated"
        cu.alert_accept()

    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_login_without_entering_pswrd(self):
        '''

        In this case we will click login button without entering password

        Expected result: alert will generate to fill password

        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.click_such_elements()
        lpu.fill_uname(cd.valid_uname)
        lpu.click_login_btn()
        cu = CommonUtilities()
        assert cu.get_alert_text() == "Please fill out Username and Password.",\
            "Please fill out Username and Password alert is not generated"
        cu.alert_accept()

    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_login_with_wrong_pswrd(self):
        '''

        In this case we will click login button with correct username and incorrect password

        Expected result: alert will generate to fill password

        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.click_such_elements()
        lpu.fill_uname(cd.valid_uname)
        lpu.fill_pswrd(cd.invalid_pswrd)
        lpu.click_login_btn()
        cu = CommonUtilities()
        assert cu.get_alert_text() == "Wrong password.",\
            "Wrong password alert is not generated"
        cu.alert_accept()

    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_login_with_valid_uname_and_pswrd(self):
        '''

        In this case we will click login button with correct username and correct password

        Expected result:

        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.login_successfully()
        cu = CommonUtilities()
        assert cu.get_text(hpl.wlcm_uname) in "Welcome palak_shah", "Welcome is not available"

    @pytest.mark.usefixtures('initiate_driver')
    def test_send_msg_to_contact(self):
        '''

        In this case we will click contact btn and fill required fields to send message.
        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.login_successfully()
        driver.refresh()
        cu = CommonUtilities()
        cu.click_element(hpl.contact_btn)
        cu.send_text(hpl.email_to_contact, 'dummy.com')
        cu.send_text(hpl.name_to_contact, 'dummy')
        cu.send_text(hpl.message_to_contact, 'dummy plz')
        cu.click_element(hpl.send_msg_btn)







