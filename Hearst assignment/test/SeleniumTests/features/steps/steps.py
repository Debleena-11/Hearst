import time
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException

# Setting up the WebDriver
chrome_driver_path = "C:\\webdriver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

def is_element_missing(driver, by, value):
    for _ in range(5):  # Try for 5 times
        try:
            driver.find_element(by, value)
            # If element found, wait for a short duration and check again
            time.sleep(1)
        except (NoSuchElementException, StaleElementReferenceException):
            # If element not found or stale, return True indicating its absence
            return True
    # If element still found after 5 tries, return False indicating its presence
    return False

@given('I open the application')
def open_application(context):
    driver.get('http://localhost:3000/')
    driver.implicitly_wait(5)

@when('I select number "{number}"')
def select_number(context, number):
    dropdown = driver.find_element(By.TAG_NAME, 'select')
    dropdown.click()
    Select(dropdown).select_by_value(number)

@when('I click the "Send to Endpoint 1" button')
def click_endpoint_1(context):
    button_element = driver.find_element(By.CSS_SELECTOR, "#root .App button:nth-of-type(1)")
    button_element.click()

@then('I expect to see the result as "{result_endpoint_1}"')
def check_result_1(context, result_endpoint_1):
    label = driver.find_element(By.TAG_NAME, 'label')
    assert label.text == result_endpoint_1

@when('I click the "Send to Endpoint 2" button')
def click_endpoint_2(context):
    button_element2 = driver.find_element(By.CSS_SELECTOR, "#root .App div:nth-of-type(2) button")
    button_element2.click()

@then('I expect to see a result as "{result_endpoint_2}"')
def check_general_result(context, result_endpoint_2):
    label = driver.find_element(By.TAG_NAME, 'label')
    assert label.text == result_endpoint_2
        
@then('I expect to see no result')
def step_impl(context):
    result = is_element_missing(driver, By.TAG_NAME, 'label')
    assert result == True, f"Expected true, but got {result}"    

def after_all(context):
    driver.quit()
