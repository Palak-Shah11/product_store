from selenium.webdriver.common.by import By

wlcm_uname = (By.CSS_SELECTOR, '#nameofuser')

go_to_laptops = (By.XPATH, '//div[@id="contcont"]//a[contains(text(),"Laptops")]')

macbook_pro = (By.XPATH, '//div[@id="tbodyid"]//a[contains(text(),"MacBook Pro")]')

add_to_cart = (By.XPATH, '//div[@id="tbodyid"]//a[contains(text(),"Add to cart")]')

go_to_cart = (By.XPATH, '//div[@id="navbarExample"]//a[contains(text(),"Cart")]')

home_btn = (By.XPATH, '//div[@id="navbarExample"]//a[@href="index.html"]')

go_to_monitors = (By.XPATH, '//div[@id="contcont"]//a[contains(text(),"Monitors")]')

asus_full_hd_monitor = (By.XPATH, '//div[@id="tbodyid"]//a[contains(text(),"ASUS Full HD")]')

delete_item_from_cart = (By.XPATH, '//td[contains(text(),"ASUS Full HD")]/parent::tr/td/following-sibling::td/a[contains(text(),"Delete")]')

place_order_btn = (By.XPATH, '//div[@id="page-wrapper"]//button[contains(text(),"Place Order")]')

close_from_place_order = (By.XPATH, '//div[@id="orderModal"]//button[@class="close"]')

contact_btn = (By.XPATH, '//div[@id="navbarExample"]//a[contains(text(),"Contact")]')

email_to_contact = (By.CSS_SELECTOR, '#recipient-email')
name_to_contact = (By.CSS_SELECTOR, '#recipient-name')
message_to_contact = (By.CSS_SELECTOR, '#message-text')
send_msg_btn = (By.XPATH, '//div[@id="exampleModal"]//button[contains(text(),"Send message")]')

name_to_place_order = (By.CSS_SELECTOR, '#name')
country_to_place_order = (By.CSS_SELECTOR, '#country')
city_to_place_order = (By.CSS_SELECTOR, '#city')
card_to_place_order = (By.CSS_SELECTOR, '#card')
month_to_place_order = (By.CSS_SELECTOR, '#month')
year_to_place_order = (By.CSS_SELECTOR, '#year')

purchase_btn = (By.XPATH, '//div[@id="orderModal"]//button[contains(text(),"Purchase")]')
purchase_ok_btn = (By.CSS_SELECTOR, 'button.confirm.btn.btn-lg.btn-primary')

log_out_btn = (By.XPATH, '//div[@id="navbarExample"]//a[contains(text(),"Log out")]')
