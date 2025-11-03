import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from base_pages.login_page import LoginPage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()

def test_login(driver):
    login_page=LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(2)
    login_page.enter_username("test")
    time.sleep(2)
    login_page.enter_password("test")
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)
    assert "Successful" in driver.page_source
    driver.save_screenshot(".\\screenshots\\successful_login.png")
    time.sleep(3)