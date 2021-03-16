from selenium.webdriver.common.by import By

class ge(object):
    # DOMAIN = 'http://v2.fabet.info/'
    DOMAIN = 'http://dev-ta.mooo.com/'
    

class MainMenuLocators(object):
    MENU_THE_THAO = (By.CLASS_NAME,'menu-sports')
    MENU_BAN_CA = (By.CLASS_NAME,'menu-fishing')
    MENU_LIVE_CASINO = (By.CLASS_NAME,'menu-casino')
    MENU_QUICK_GAME = (By.CLASS_NAME,'menu-quickGames')
    MENU_TABLE_GAME = (By.CLASS_NAME,'menu-tablegame')
    MENU_CONG_GAME = (By.CLASS_NAME,'menu-lobby')

class CongGameLocators(object):
    Type_All = (By.CLASS_NAME,'icon-all')
    Type_No_hu = (By.CLASS_NAME,'icon-nohu1')
    Type_Ban_ca = (By.CLASS_NAME,'icon-banca')
    Type_Lo_de = (By.CLASS_NAME,'icon-lode1')
    Type_Ingame = (By.CLASS_NAME,'icon-in-game1')
    Type_Table_game = (By.CLASS_NAME,'icon-table-game1')
    Type_Game_nhanh = (By.CLASS_NAME,'icon-game-nhanh1')

    NCC_selector = (By.CLASS_NAME,'btn-secondary')
    NCC_btn_Techplay = (By.CLASS_NAME,'icon-techplay')
    NCC_btn_PragmaticPlay = (By.CLASS_NAME,'icon-prag')
    NCC_btn_CQ9 = (By.CLASS_NAME,'icon-cq9')

    Sort_Nhieu_nguoi_choi = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = (By.XPATH,'//label[contains(@class,"base-radio__wrap")][5]')

class HomePageLocators(object):
    btn_register = (By.CLASS_NAME,'btn--home-register')

    txt_username = (By.XPATH,"//div[@id='signInFull']/div/form/div/div/input[@type='text']")
    txt_password = (By.XPATH,"//div[@id='signInFull']/div/form/div/div/input[@type='password']")

    btn_login_full = (By.XPATH,"//div[contains(@class, 'login-form__submit')]/button")
    btn_logout = (By.XPATH,"//div[contains(@class,'user-login-block')]/a[contains(@class, 'logout')]/i")


