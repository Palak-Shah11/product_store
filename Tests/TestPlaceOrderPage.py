import time

import pyautogui
import pytest

from Utilities.common_utilities import CommonUtilities
from Utilities.LoginPageUtilities import LoginPageUtilities
from Locators import HomePageLocators as hpl
from conftest import driver


class TestPlaceOrderPage:
    @pytest.mark.usefixtures('initiate_driver')
    def test_verify_to_add_item_to_cart(self):
        '''

        In this case we go to laptops and add mackbook pro to cart then,
        we go to monitors and add asus full hd monitor to cart.

        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.login_successfully()
        driver.refresh()
        lpu.click_laptop()
        pyautogui.press('down')
        cu = CommonUtilities()
        cu.click_element(hpl.macbook_pro)
        cu.click_element(hpl.add_to_cart)
        assert cu.get_alert_text() == "Product added",\
            "Product added alert is not generated"
        cu.alert_accept()
        cu.click_element(hpl.home_btn)
        cu.click_element(hpl.go_to_monitors)
        cu.click_element(hpl.asus_full_hd_monitor)
        cu.click_element(hpl.add_to_cart)
        assert cu.get_alert_text() == "Product added", \
            "Product added alert is not generated"
        cu.alert_accept()

    @pytest.mark.usefixtures('initiate_driver')
    def test_delete_from_cart(self):
        '''

        In this case we will go to cart and delete an item from cart
        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.login_successfully()
        cu = CommonUtilities()
        cu.wait_for_element(hpl.log_out_btn)
        driver.refresh()
        # time.sleep(5)
        # cu = CommonUtilities()
        cu.click_element(hpl.go_to_cart)
        cu.click_element(hpl.delete_item_from_cart)
        cu.click_element(hpl.place_order_btn)
        cu.click_element(hpl.close_from_place_order)
        time.sleep(2)

    @pytest.mark.usefixtures('initiate_driver')
    def test_place_order(self):
        '''

        In this case we will fill required fields to place an order and then log out
        :return:
        '''
        lpu = LoginPageUtilities()
        lpu.login_successfully()
        cu = CommonUtilities()
        cu.wait_for_element(hpl.log_out_btn)
        driver.refresh()
        # cu = CommonUtilities()
        cu.click_element(hpl.go_to_cart)
        cu.wait_for_element(hpl.log_out_btn)
        driver.refresh()
        cu.click_element(hpl.place_order_btn)
        cu.send_text(hpl.name_to_place_order, "Palak")
        cu.send_text(hpl.country_to_place_order, "India")
        cu.send_text(hpl.city_to_place_order, "Ahmedabad")
        cu.send_text(hpl.card_to_place_order, "1243")
        cu.send_text(hpl.month_to_place_order, "August")
        cu.send_text(hpl.year_to_place_order, "2023")
        cu.click_element(hpl.purchase_btn)
        cu.click_element(hpl.purchase_ok_btn)
        driver.refresh()
        cu.click_element(hpl.log_out_btn)
        time.sleep(4)
