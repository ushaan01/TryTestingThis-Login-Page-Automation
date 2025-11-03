from selenium.webdriver.common.by import By

#locators:web_element
class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username_id=(By.ID,"uname")
        self.password_id=(By.ID,"pwd")
        self.login_button=(By.XPATH,"//input[@value='Login']")

#actions:methods
    def open_page(self,url):
        self.driver.get(url)

    def enter_username(self,username):
        #self.driver.find_element(self.username_id).clear()
        self.driver.find_element(*self.username_id).send_keys(username)

    def enter_password(self,password):
        #self.driver.find_element(self.password_id).clear()
        self.driver.find_element(*self.password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

