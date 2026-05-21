import pytest
from pages.register_page import RegisterPage
from utils.wait_utils import *

#Positive test case
def test_register_positive(driver):
    print("Start testing register with positive cases")
    driver.get("https://demo-saas.bugbug.io/sign-up")
    #Call class for open register page
    register_page = RegisterPage(driver)
    register_page.register(first_name="Kim", last_name="test", email="testgmail08@gmail.com", password="testqcpass")
    print("Testing data")
    print("Firstname: Kim")
    print("Lastname: test")
    print("Email: testgmail08@gmail.com")
    print("Password: testqcpass")

    redirect_url ="https://demo-saas.bugbug.io/verify-email"
    wait_url_contains(driver, redirect_url)
    
    assert redirect_url in driver.current_url    

#Negative test cases
@pytest.mark.parametrize(
    "field, first_name,last_name,email,password,expected_error",
    [
        ("firstName", "", "test", "emailtest@gmail.com", "testqcpass", "String must contain at least 1 character(s)"),
        ("lastName", "Kim", "", "emailtest@gmail.com", "testqcpass", "String must contain at least 1 character(s)"),
        ("email", "Kim", "test", "emailtest", "testqcpass", "Invalid email"),
        ("password", "Kim", "test", "emailtest@gmail.com", "test", "String must contain at least 8 character(s)"),
        ("global", "Kim", "test", "test@gmail.com", "testqcpass", "User already exists"),
    ]
)
def test_register_negative(driver, field, first_name, last_name, email, password, expected_error):
    print("Start testing register with negative cases")
    driver.get("https://demo-saas.bugbug.io/sign-up")
    #Call class for open register page
    register_page = RegisterPage(driver)
    register_page.register(first_name=first_name, last_name=last_name, email=email, password=password)
    if field != "global":
        error_text = register_page.get_error_by_field(field_name=field)
    else:
        error_text = register_page.get_message_error()
    
    print("Testing data")
    print(f"Firstname: {first_name}")
    print(f"Lastname: {last_name}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Expected error: {expected_error}")
    print(f"Actual error: {error_text}")

    assert error_text == expected_error
