# Created by gabri at 06/05/2025
Feature: Validación de carrito de compras
  # Enter feature description here

  Background:
    Given Ingreso a la url "https://www.saucedemo.com/"
    When Ingreso el usuario "standard_user"
    And Ingreso password "secret_sauce1"
    And Presiono el boton Login
    Then Valido estoy en la pagina principal

  Scenario: Validar ingreso de item al carrito
    Given Valido item "Sauce Labs Backpack"
    When Agrego item al carrito de compras
    And Ingreso al carrito de compras
    Then Valido que este elemento agregado al carrito
