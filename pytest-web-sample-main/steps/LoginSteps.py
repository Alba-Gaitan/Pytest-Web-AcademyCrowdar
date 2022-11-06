from pages import LoginPage as page
from core.steps.BaseSteps import BaseStep
from core.assertion.Assertion import Assertion
from selenium import webdriver

class LoginSteps(BaseStep):

    def goToUrl(context, web):
        context.driver = webdriver.Chrome(executable_path='drivers/chromedriver.exe')
        context.driver.get(web)


    def clickBtnAccount(self):
        elem = page.clickBtnAccount()
        elem.click()


    def setUser(self, usuario):
        elem = page.getUserInput()
        elem.setText(usuario)

    def setPass(self, password):
        elem = page.getPassInput()
        elem.setText(password)

    def clickLoginBtn(self):
        elem = page.clickLogin()
        elem.click()

    def verifyLogin(self, texto):
        driverElem = page.verifyLogin()
        Assertion.assertTrue("From your account dashboard you can view your", driverElem.isTextInElement(texto))
        return self

    def verifyError(self, error):
        driverElem = page.verifyError()
        Assertion.assertTrue("the password you entered for the username", driverElem.isTextInElement(error))
        return self