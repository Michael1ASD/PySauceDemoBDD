from pytest_bdd import scenarios, given, when, then

scenarios('minimal.feature')

@given('I am on the homepage')
def homepage():
    pass

@when('I click the button')
def click_button():
    pass

@then('I see the result')
def see_result():
    pass