import time
import pytest
import allure
from pom.main_page import MainPageSteps, MainPageAsserts


@allure.story('Main page test cases')
@pytest.mark.usefixtures('setup')
class TestMainPage:

    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description('Checking title text')
    def test_title_text(self):
        driver = self.driver
        asserts = MainPageAsserts(driver)
        time.sleep(1)
        with allure.step('Verify that title text is correct'):
            asserts.assert_title_text()

    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description('Checking simple addition')
    def test_addition(self):
        driver = self.driver
        steps = MainPageSteps(driver)
        asserts = MainPageAsserts(driver)
        time.sleep(1)
        with allure.step('Enter first value'):
            steps.enter_first_value(value='8')
        with allure.step('Enter second value'):
            steps.enter_second_value(value='8')
        with allure.step('Click to GO button'):
            steps.click_go_button()
        time.sleep(2)
        with allure.step('Verify that the result on main result field is correct'):
            asserts.assert_main_result_field(value=str(8 + 8))

    @allure.label("owner", "QA Engineer")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('Checking combo expressions')
    def test_combo_expressions(self):
        driver = self.driver
        steps = MainPageSteps(driver)
        asserts = MainPageAsserts(driver)
        time.sleep(1)
        with allure.step('Enter first value for first math operation'):
            steps.enter_first_value(value='16')
        with allure.step('Enter second value for first math operation'):
            steps.enter_second_value(value='4')
        with allure.step('Open dropdown list'):
            steps.click_operator_dropdown()
        with allure.step('Select division operator'):
            steps.select_division_sign()
        with allure.step('Click to GO button'):
            steps.click_go_button()
            time.sleep(2)
        with allure.step('Enter first value for second math operation'):
            steps.enter_first_value(value='4')
        with allure.step('Enter second value for second math operation'):
            steps.enter_second_value(value='4')
        with allure.step('Open dropdown list'):
            steps.click_operator_dropdown()
        with allure.step('Select multiplication operator'):
            steps.select_multiplication_sign()
        with allure.step('Click to GO button'):
            steps.click_go_button()
            time.sleep(2)
        with allure.step('Verify that the result on sub lower field is correct'):
            asserts.assert_lower_sub_result_field(value=str(16 // 4))
        with allure.step('Verify that the result on sub upper field is correct'):
            asserts.assert_upper_sub_result_field(value=str(4 * 4))
            time.sleep(1)
        with allure.step('Verify that there are 2 expressions after 2 math operations'):
            asserts.assert_list_expressions()
