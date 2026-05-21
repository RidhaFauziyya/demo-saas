from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.wait_utils import *

class LoginPage:

    #Initiation data for login form
    def __init__(self, driver):
        self.driver = driver
        self.email = (By.NAME, "email") 
        self.password = (By.NAME, "password") 
        self.login_button = (By.XPATH, "//button[@type='submit']//span[@class='m_80f1301b mantine-Button-inner']")
        self.global_error = ( By.XPATH,"//div[contains(@style,'color') and .//p]//p")

    #Function for enter email field
    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    #Function for enter password field
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    #Function for click login button
    def click_login(self):
        button = wait_clickable(self.driver, self.login_button)
        button.click()

    #Function for get error message
    def get_error_by_field(self, field_name):
        locator = (
            By.XPATH,
            f"//input[@name='{field_name}']/ancestor::div[contains(@class,'InputWrapper-root')]//p"
        )
        return self.driver.find_element(*locator).text
    
    def get_message_error(self):
        return self.driver.find_element(*self.global_error).text


    def login(self,email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()