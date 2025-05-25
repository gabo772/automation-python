import time

from behave import given, when, then
from utils.elementos import  *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

@given('Ingreso a la url "{url}"')
def step_ingreso_a_la_url(context, url):
        context.browser.get(url)


@when('Ingreso el usuario "{nombre_usuario}"')
def step_impl(context,nombre_usuario):
    input_username=buscar_por_id(context,"user-name")
    input_username.click()
    input_username.send_keys(nombre_usuario)


@when('Ingreso password "{password}"')
def step_impl(context,password):
    input_password=buscar_por_id(context,"password")
    input_password.click()
    input_password.send_keys(password)


@when("Presiono el boton Login")
def step_impl(context):
    input_button_login=buscar_por_id(context,"login-button")
    input_button_login.click()


@then('Valido que el mensaje de error sea "{mensaje}"')
def step_impl(context,mensaje):
    elemento_mensaje=buscar_por_xpath(context,"//h3[@data-test='error']")
    element_mensaje_text=elemento_mensaje.text
    assert element_mensaje_text == mensaje, f"El mensaje no corresponde \nencontrado: {element_mensaje_text} \nesperado: {mensaje}"


@then("Valido estoy en la pagina principal")
def step_impl(context):
    try:
        time.sleep(1)
        actions = ActionChains(context.browser)
        actions.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()
    except:
        print("No hay alert :)")
    titulo_pagina_principal=buscar_por_xpath(context,"//div[@class='app_logo']")
    assert titulo_pagina_principal.text=="Swag Labs","No se logró ingresar a la página principal"