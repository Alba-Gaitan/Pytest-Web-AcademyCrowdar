from core.ui.WebUIElement import WebUIElement as UIElement
from core.ui.By import By


def clickBtnAccount():
    return UIElement(By.XPATH, '//*[@id="menu-item-50"]/a[1]')

def getUserInput():
    return UIElement(By.ID, 'username')

def getPassInput():
    return UIElement(By.ID, 'password')

def clickLogin():
    return UIElement(By.XPATH, '//*[@id="customer_login"]/div[1]/form[1]/p[3]/input[3]')

def verifyError():
    return UIElement(By.XPATH, '//*[@id="page-36"]/div[1]/div[1]/ul[1]/li[1]')

def verifyLogin():
    return UIElement(By.XPATH, '//*[@id="page-36"]/div[1]/div[1]/div[1]/p[2]')

