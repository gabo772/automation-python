Feature: probando pagina login

    @validacion_login_incorrecto @chrome
    Scenario: validacion ingreso incorrecto
        Given Ingreso a la url "https://www.saucedemo.com/"
        When Ingreso el usuario "user1"
        And Ingreso password "epic1"
        And Presiono el boton Login
        Then Valido que el mensaje de error sea "Epic sadface: Username and password do not match any user in this service"
    @validacion_login_correcto @firefox
    Scenario: validacion ingreso correcto
        Given Ingreso a la url "https://www.saucedemo.com/"
        When Ingreso el usuario "standard_user"
        And Ingreso password "secret_sauce"
        And Presiono el boton Login
        Then Valido estoy en la pagina principal