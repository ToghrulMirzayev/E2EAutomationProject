# Here I've used several locators for web elements
class MainPageLocators:
    TITLE_TEXT = "//h3[contains(text(),'Super Calculator')]"
    FIRST_FIELD = '[ng-model="first"]'
    SECOND_FIELD = '[ng-model="second"]'
    OPERATOR = '[ng-model="operator"]'
    GO_BUTTON = 'gobutton'
    MAIN_RESULT_FIELD = '.form-inline .ng-binding'
    LOWER_SUB_RESULT_FIELD = "tr:nth-child(2) > td:nth-child(3)"
    UPPER_SUB_RESULT_FIELD = "tr:nth-child(1) > td:nth-child(3)"
    DIVISION = '[value="DIVISION"]'
    MULTIPLICATION = '[value="MULTIPLICATION"]'
    LIST_EXPRESSIONS = '.table .ng-scope'
