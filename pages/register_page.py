from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.wait_utils import *

class RegisterPage:

    #Initiation data for register form
    def __init__(self, driver):
        self.driver = driver
        self.first_name = (By.NAME, "firstName")
        self.last_name = (By.NAME, "lastName")
        self.email = (By.NAME, "email") 
        self.password = (By.NAME, "password") 
        self.regist_button = (By.XPATH,"//button[@type='submit']//span[@class='m_80f1301b mantine-Button-inner']")
        self.global_error = ( By.XPATH,"//div[contains(@style,'color') and .//p]//p")

    #Function for enter first_name field
    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)

    #Function for enter last_name field
    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)

    #Function for enter email field
    def enter_email(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    #Function for enter password field
    def enter_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    #Function for click register button
    def click_register(self):
        button = wait_clickable(self.driver, self.regist_button)
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


    def register(self, first_name, last_name, email, password):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)
        self.click_register()
   