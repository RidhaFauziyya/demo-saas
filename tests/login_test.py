import pytest
from pages.login_page import LoginPage
from utils.wait_utils import *



#Positive test case
def test_login_positive(driver):
    print("Start testing login with positive cases")
    driver.get("https://demo-saas.bugbug.io/sign-in")
    #Call class for open login page
    login_page = LoginPage(driver)
    login_page.login(email="parkcyoke@gmail.com", password="testqcpass")
    print("Testing data")
    print("Email: parkcyoke@gmail.com")
    print("Password: testqcpass")

    redirect_url ="https://demo-saas.bugbug.io/testingpy/tickets"
    wait_url_contains(driver, redirect_url)
    
    assert redirect_url in driver.current_url    

#Negative test cases
@pytest.mark.parametrize(
    "field,email,password,expected_error",
    [
        ("email", "parkcyoke", "", "Invalid email"),
        ("global", "parkcyoke@gmail.com", "", "Password is required"),
        ("global", "parkcyoke@gmail.com", "testqc", "Invalid email or password"),
        ("global", "parkcy123@gmail.com", "testqcpass", "Invalid email or password"),
    ]
)
def test_login_negative(driver, field, email, password, expected_error):
    print("Start testing login with negative cases")
    driver.get("https://demo-saas.bugbug.io/sign-in")
    #Call class for open login page
    login_page = LoginPage(driver)
    login_page.login(email=email, password=password)
    if field != "global":
        error_text = login_page.get_error_by_field(field_name=field)
    else:
        error_text = login_page.get_message_error()
    
    print("Testing data")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Expected error: {expected_error}")
    print(f"Actual error: {error_text}")

    assert error_text == expected_error
