# conftest.py
import pytest
from selenium import webdriver
import os, time, allure

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.implicitly_wait(10)
    driver.quit()


# hook untuk screenshot kalau test gagal
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            # ambil screenshot dalam bentuk bytes
            screenshot = driver.get_screenshot_as_png()

            # attach ke allure
            allure.attach(
                screenshot,
                name=f"{item.name}_failure_screenshot_{int(time.time())}",
                attachment_type=allure.attachment_type.PNG
            )