from behave import when, then
import httpx

BASE_URL = "http://localhost:8000"

@when('I retrieve numbers from endpoint1')
def step_retrieve_numbers(context):
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/endpoint1")
    context.response = response
    
@then('the response should contain numbers from 1 to 10')
def step_validate_numbers(context):
    assert context.response.json() == {"numbers": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

@when('I send a number {number} to endpoint2')
def step_send_number_endpoint2(context, number):
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/endpoint2/{number}")
    context.response = response

@then('I receive its square {square:d}')
def step_validate_square(context, square):
    assert context.response.json() == {"result": square}

@when('I send the odd number {oddNumber} to endpoint3')
def step_send_odd_number_endpoint3(context, oddNumber):
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/endpoint3/{oddNumber}")
    context.response = response

@then('I should get {halfNumber:f} as the result')
def step_validate_divided_number(context, halfNumber):
    assert context.response.json() == {"result": halfNumber}

@when('I send the even number {evenNumber:d} to endpoint3')
def step_send_even_number_endpoint3(context, evenNumber):
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/endpoint3/{evenNumber}")
    context.response = response

@then('I should receive an error')
def step_validate_error(context):
    assert context.response.status_code == 500    
    
@given('I send the character "{char}" to endpoint2')
def step_send_char_endpoint2(context, char):
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/endpoint2/{char}")
    context.response = response

@given('I send the character "{char}" to endpoint3')
def step_send_char_endpoint3(context, char):
    with httpx.Client() as client:
        response = client.get(f"{BASE_URL}/endpoint3/{char}")
    context.response = response

@then('I should receive a validation error')
def step_validate_validation_error(context):
    assert context.response.status_code == 422  # 422 Unprocessable Entity for validation errors
    assert "detail" in context.response.json()


##################### 