import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import config.credential as cd
driver = webdriver.Chrome(ChromeDriverManager().install())


@pytest.fixture()
def initiate_driver():
    # set-up part
    driver.get('https://www.demoblaze.com/index.html')
    driver.maximize_window()

    yield driver
    # Tear Down Part
    driver.quit()
