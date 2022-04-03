# E2EAutomationProject
## Project details
This is the E2E Test Automation project which is created by me. I have used Page Object Model pattern and my self-written test framework by using below listed technical stacks:

1. Python as a programming language
2. Pytest as a test framework
3. Allure as a reporting tool
4. Selenium library is used for browser automation

Test object URL: http://juliemr.github.io/protractor-demo/

## Simple run tests from IDE terminal
Python -m pytest -v -s e2e_tests/test_cases.py

## Run tests with reports
Use below steps if you want to run tests with allure reports.

1. Python -m pytest -v -s --alluredir="*path to project*\report" e2e_tests/test_cases.py
2. cd *path to local project folder*
3. allure serve report
