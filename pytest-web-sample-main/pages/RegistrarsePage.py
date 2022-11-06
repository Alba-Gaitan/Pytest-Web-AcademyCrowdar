from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By

def getUserInput():
    return UIElement(By.ID,'reg_email')

def getPassInput():
    return UIElement(By.ID,'reg_password')

def clickBtnRegister():
    return UIElement(By.XPATH,'//*[@id="customer_login"]/div[2]/form/p[3]/input[3]')

def verifyRegister():
    return UIElement(By.XPATH, '//*[@id="page-36"]/div[1]/div[1]/div[1]/p[2]')

