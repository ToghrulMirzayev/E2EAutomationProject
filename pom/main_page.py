from base.base_object import BaseObject
from locators.locators import MainPageLocators as l
import pytest_check as check  # pytest_check is used for multiple asserts in order to check all asserts in 1 test case.


class MainPageSteps(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_first_value(self, value):
        self.is_present('tag_name', l.FIRST_FIELD).send_keys(value)

    def enter_second_value(self, value):
        self.is_present('tag_name', l.SECOND_FIELD).send_keys(value)

    def click_operator_dropdown(self):
        self.is_clickable('tag_name', l.OPERATOR)

    def select_division_sign(self):
        self.is_clickable('tag_name', l.DIVISION).click()

    def select_multiplication_sign(self):
        self.is_clickable('tag_name', l.MULTIPLICATION).click()

    def click_go_button(self):
        self.is_clickable('id', l.GO_BUTTON).click()


class MainPageAsserts(BaseObject):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def assert_title_text(self):
        expected_text = 'Super Calculator'
        actual_text = self.is_present('xpath', l.TITLE_TEXT).text
        assert expected_text == actual_text, f'Error. Expected text is {expected_text}, ' \
                                             f'but actual text is {actual_text}'

    def assert_main_result_field(self, value):
        expected_text = value
        actual_text = self.is_present('css', l.MAIN_RESULT_FIELD).text
        assert expected_text == actual_text, f'Error. Expected text is {expected_text}, ' \
                                             f'but actual text is {actual_text}'

    def assert_lower_sub_result_field(self, value):
        expected_text = value
        actual_text = self.is_present('css', l.LOWER_SUB_RESULT_FIELD).text
        check.equal(expected_text, actual_text)

    def assert_upper_sub_result_field(self, value):
        expected_text = value
        actual_text = self.is_present('css', l.UPPER_SUB_RESULT_FIELD).text
        check.equal(expected_text, actual_text)

    def list_exp(self):
        exp_list = []
        exp_list = self.are_visible('css', l.LIST_EXPRESSIONS, 'List of Expressions')
        check.equal(len(exp_list), 2)
