"""
Web Steps

Steps file for web interactions with Selenium
"""
import logging
from behave import when, then
from compare import expect, ensure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions


@when('I visit the "{page_name}"')
def step_impl(context, page_name):
    context.driver.get(context.base_url)


@then('I should see "{text}" in the title')
def step_impl(context, text):
    expect(context.driver.title).to_contain(text)


@then('I should not see "{text}"')
def step_impl(context, text):
    error_msg = f"I should not see '{text}'"
    ensure(text not in context.driver.page_source, True, error_msg)


@when('I set the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)


@when('I select "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    element.select_by_visible_text(text)


@when('I press the "{button}" button')
def step_impl(context, button):
    button_id = button.lower() + '-btn'
    context.driver.find_element(By.ID, button_id).click()


@then('I should see "{name}" in the results')
def step_impl(context, name):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'search_results'),
            name
        )
    )
    expect(found).to_be_true()


@then('I should not see "{name}" in the results')
def step_impl(context, name):
    element = context.driver.find_element(By.ID, 'search_results')
    error_msg = f"I should not see '{name}' in '{element.text}'"
    ensure(name not in element.text, True, error_msg)


@then('I should see the message "{message}"')
def step_impl(context, message):
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element(
            (By.ID, 'flash_message'),
            message
        )
    )
    expect(found).to_be_true()


@then('I should see "{text_string}" in the "{element_name}" field')
def step_impl(context, text_string, element_name):
    element_id = element_name.lower().replace(' ', '_')
    found = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.text_to_be_present_in_element_value(
            (By.ID, element_id),
            text_string
        )
    )
    expect(found).to_be_true()


@then('I should see "{text}" in the "{element_name}" dropdown')
def step_impl(context, text, element_name):
    element_id = element_name.lower().replace(' ', '_')
    element = Select(context.driver.find_element(By.ID, element_id))
    expect(element.first_selected_option.text).to_equal(text)


@when('I change the "{element_name}" to "{text_string}"')
def step_impl(context, element_name, text_string):
    element_id = element_name.lower().replace(' ', '_')
    element = context.driver.find_element(By.ID, element_id)
    element.clear()
    element.send_keys(text_string)


@when('I copy the "{element_name}" field')
def step_impl(context, element_name):
    element_id = element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    context.clipboard = element.get_attribute('value')


@when('I paste the "{element_name}" field')
def step_impl(context, element_name):
    element_id = element_name.lower().replace(' ', '_')
    element = WebDriverWait(context.driver, context.wait_seconds).until(
        expected_conditions.presence_of_element_located((By.ID, element_id))
    )
    element.clear()
    element.send_keys(context.clipboard)
