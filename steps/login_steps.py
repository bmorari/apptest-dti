from appium import webdriver
from behave import given, when, then
from utils.capabilities import capabilities

@given('que o usuário está na tela de login')
def step_open_login_screen(context):
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', capabilities)

@when('ele insere credenciais inválidas')
def step_enter_invalid_credentials(context):
    context.driver.find_element_by_accessibility_id('username').send_keys('usuario_invalido')
    context.driver.find_element_by_accessibility_id('password').send_keys('senha_invalida')
    context.driver.find_element_by_accessibility_id('login_button').click()

@then('uma mensagem de erro é exibida')
def step_verify_error_message(context):
    error_message = context.driver.find_element_by_accessibility_id('error_message')
    assert error_message.is_displayed()
    context.driver.quit()