@login
Feature: Login automation practice

  Scenario Outline: Login exitoso
    Given El usuario se dirige a la pagina <web>
    And hace click en el boton mi cuenta
    And ingresa <usuario>
    And ingresa <password>
    When hace click en el boton login
    Then ingresa a la pantalla principal y se visualiza el texto <texto>
    Examples:
      |web                                   |usuario                  |password| texto|
      |https://practice.automationtesting.in/|albagaitan.fsk@gmail.com |alba1234*|From your account dashboard you can view your|


  Scenario Outline: Login Fallido contraseña incorrecta
    Given El usuario se dirige a la pagina de <web>
    And hace click en el boton mi cuenta
    And ingresa <usuario>
    And ingresa <password>
    When hace click en el boton login
    Then Se verifica que no puede iniciar sesion y se visualiza el error <error>
    Examples:
      |web                                   |usuario                  |password|error|
      |https://practice.automationtesting.in/|albagaitan.fsk@gmail.com |albo1234*| the password you entered for the username |