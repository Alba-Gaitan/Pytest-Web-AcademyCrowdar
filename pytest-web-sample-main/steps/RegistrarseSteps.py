from core.assertion.Assertion import Assertion
from pages import RegistrarsePage as page
from core.steps.BaseSteps import BaseStep

class RegistrarseSteps(BaseStep):

    def setUser(self, usuario):
        elem = page.getUserInput()
        elem.setText(usuario)

    def setPass(self, password):
        elem = page.getPassInput()
        elem.setText(password)

    def clickRegisterBtn(self):
        elem = page.clickBtnRegister()
        elem.click()

    def verifyRegister(self, texto):
        driverElem = page.verifyRegister()
        Assertion.assertTrue("From your account dashboard you can view your", driverElem.isTextInElement(texto))
        return self


