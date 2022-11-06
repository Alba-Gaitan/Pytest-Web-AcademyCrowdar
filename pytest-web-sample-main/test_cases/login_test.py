from pytest_bdd import then, given, when, scenarios

from steps.LoginSteps import LoginSteps as Login

scenarios('../features/Login.feature')

@given('El usuario se dirige a la pagina <web>')
def step_impl(web):
    Login().goToUrl(web)

@given('hace click en el boton mi cuenta')
def clickBtnAccount():
    Login().clickBtnAccount()

@given('ingresa <usuario>')
def setUser(usuario):
    Login().setUser(usuario)

@given('ingresa <password>')
def setPass(password):
    Login().setPass(password)

@when('hace click en el boton login')
def clickBtnLogin():
    Login().clickLoginBtn()

@then('ingresa a la pantalla principal y se visualiza el texto <texto>')
def validateHome(texto):
    Login().verifyLogin(texto)

@then('Se verifica que no puede iniciar sesion y se visualiza el error <error>')
def verifyError(error):
    Login().verifyError(error)

def teardown():
    Login().closeBrowser()
