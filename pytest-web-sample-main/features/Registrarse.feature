@registro
Feature: Registrarse en automation practice

 Scenario Outline: Registrar usuario exitosamente
    Given El usuario se dirige a la pagina <web>
    And hace click en el boton mi cuenta
    And ingresa <usuario>
    And ingresa <password>
    When hace click en el boton register
    Then ingresa a la pantalla principal y se visualiza el texto <texto>
    Examples:
      |web                                   |usuario           |password   | texto                                       |
      |https://practice.automationtesting.in/|em2556b@gmail.com |prueb123*4*|From your account dashboard you can view your|