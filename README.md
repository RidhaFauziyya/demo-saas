# Web Authentication Automation Testing using Selenium & Pytest
Automation testing project using Selenium, Pytest, and Allure Report with Page Object Model implementation.

## Tech Stack

- Python
- Selenium
- Pytest
- Allure Report

## Features

- Automated UI Testing
- Page Object Model (POM)
- Screenshot on Failure
- Allure Reporting
- Reusable Fixtures
- Explicit Wait Handling

## Project Structure

- pages/   -> page object classes
- tests/   -> test cases
- utils/   -> helper functions

## Run Test

```bash
pytest -v
```
### Generate Allure Report

```bash
pytest --alluredir=allure-results
allure serve allure-results
```
