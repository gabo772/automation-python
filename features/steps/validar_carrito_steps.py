from behave import *

from utils.elementos import buscar_por_xpath


@given('Valido item "{item}"')
def step_impl(context,item):
    elemento_item = buscar_por_xpath(context,f"//div[@data-test='inventory-item-name' and text()='{item}']")
    assert elemento_item.is_displayed(),"No se encuentra elemento "+item
    context.item = item


@when("Agrego item al carrito de compras")
def step_impl(context):
    boton_add=buscar_por_xpath(context,f"//div[@data-test='inventory-item-name' and text()='{context.item}']/parent::*/parent::*/following-sibling::*//button")
    assert boton_add.is_displayed(),f"No se encuentra elemento de {context.item} para agregarlo al carrito de compra"
    boton_add.click()


@step("Ingreso al carrito de compras")
def step_impl(context):
    elem_carrito=buscar_por_xpath(context,"//a[@class='shopping_cart_link']")
    assert elem_carrito.is_displayed(),"No se encuentra elemento carrito de compras"
    elem_carrito.click()


@then("Valido que este elemento agregado al carrito")
def step_impl(context):
    elem_item_en_carrito=buscar_por_xpath(context,f"//div[@data-test='cart-list']//*[contains(text(),'{context.item}')]")
    assert elem_item_en_carrito.is_displayed(),"No se encuentra elemento en el carrito de compra"
