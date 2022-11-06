from pytest_bdd import then, given, when, scenarios
from steps.RegistrarseSteps import RegistrarseSteps as Registrarse
from steps.LoginSteps import LoginSteps as Login

scenarios('../features/Registrarse.feature')

@given('El usuario se dirige a la pagina <web>')
def step_impl(web):
    Login().goToUrl(web)

@given('hace click en el boton mi cuenta')
def clickBtnAccount():
    Login().clickBtnAccount()

@given('ingresa <usuario>')
def setUser(usuario):
    Registrarse().setUser(usuario)

@given('ingresa <password>')
def setPass(password):
    Registrarse().setPass(password)

@when('hace click en el boton register')
def clickRegisterBtn():
    Registrarse().clickRegisterBtn()

@then('ingresa a la pantalla principal y se visualiza el texto <texto>')
def validateRegister(texto):
    Registrarse().verifyRegister(texto)

def teardown():
    Registrarse().closeBrowser()
