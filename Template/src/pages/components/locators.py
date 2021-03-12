from selenium.webdriver.common.by import By

@staticmethod
class ge(object):
    DOMAIN = 'http://v2.fabet.info/'
    # DOMAIN = 'http://dev-ta.mooo.com/'
    

class HomePageLocators(object):
    btn_login = (By.CLASS_NAME,'btn--home-login')
    btn_register = (By.CLASS_NAME,'btn--home-register')

    txt_username = (By.XPATH,"//div[@id='signInFull']/div/form/div/div/input[@type='text']")
    txt_password = (By.XPATH,"//div[@id='signInFull']/div/form/div/div/input[@type='password']")

    btn_login_full = (By.XPATH,"//div[contains(@class, 'login-form__submit')]/button")
    btn_logout = (By.XPATH,"//div[contains(@class,'user-login-block')]/a[contains(@class, 'logout')]/i")
