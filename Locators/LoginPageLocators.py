from selenium.webdriver.common.by import By

about_us = (By.XPATH, '//div[@id="navbarExample"]//a[contains(text(),"About us")]')

btn_to_go_on_login_page = (By.XPATH, '//div[@id="navbarExample"]//a[contains(text(),"Log in")]')

btn_to_close_about = (By.XPATH, '//div[@id="videoModal"]//h5[contains(text(),"About us")] /parent ::div//span')

username_fill = (By.CSS_SELECTOR, '#loginusername')

pswrd_fill = (By.CSS_SELECTOR, '#loginpassword')

login_btn = (By.XPATH, '//div[@id="logInModal"]//div/button[contains(text(),"Log in")]')

