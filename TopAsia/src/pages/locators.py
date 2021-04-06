from selenium.webdriver.common.by import By
from TopAsia.src.pages.UIObject import UiObject


class ge(object):
    # DOMAIN = 'http://v2.fabet.info/'
    DOMAIN = 'http://dev-ta.mooo.com/'
    ProjectName = 'TopAsia'


class MainMenuLocators(object):
    MENU_THE_THAO = UiObject(By.CLASS_NAME, 'menu-sports')
    MENU_BAN_CA = UiObject(By.CLASS_NAME, 'menu-fishing')
    MENU_LIVE_CASINO = UiObject(By.CLASS_NAME, 'menu-casino')
    MENU_QUICK_GAME = UiObject(By.CLASS_NAME, 'menu-quickGames')
    MENU_TABLE_GAME = UiObject(By.CLASS_NAME, 'menu-tablegame')
    MENU_CONG_GAME = UiObject(By.CLASS_NAME, 'menu-cong-game')
    MENU_DANG_NHAP = UiObject(By.CLASS_NAME, 'not-login-user-login')
    MENU_DANG_KY = UiObject(By.CLASS_NAME, 'not-login-user-register')
    MENU_USER_INFO_DROP = UiObject(By.XPATH, '//div[@class="info-user"]')


class CongGameLocators(object):
    Type_All = UiObject(By.CLASS_NAME, 'icon-all')
    Type_No_hu = UiObject(By.CLASS_NAME, 'icon-nohu1')
    Type_Ban_ca = UiObject(By.CLASS_NAME, 'icon-banca')
    Type_Lo_de = UiObject(By.CLASS_NAME, 'icon-lode1')
    Type_Ingame = UiObject(By.CLASS_NAME, 'icon-in-game1')
    Type_Table_game = UiObject(By.CLASS_NAME, 'icon-table-game1')
    Type_Game_nhanh = UiObject(By.CLASS_NAME, 'icon-game-nhanh1')

    NCC_selector = UiObject(By.CLASS_NAME, 'btn-secondary')
    NCC_btn_All = UiObject(By.XPATH, '//div/ul/li[1][@role="presentation"]')
    NCC_btn_Techplay = UiObject(By.XPATH, '//input[@value="vingame"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_PragmaticPlay = UiObject(By.XPATH, '//input[@value="pragmatic"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_CQ9 = UiObject(By.XPATH, '//input[@value="cq9"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_Tomhorn = UiObject(By.XPATH, '//input[@value="tomhorn"]/parent::div/parent::label/parent::a/parent::li')
    NCC_btn_PlaynGo = UiObject(By.XPATH, '//input[@value="playngo"]/parent::div/parent::label/parent::a/parent::li')

    Sort_Nhieu_nguoi_choi = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][5]')

    List_Game = UiObject(By.XPATH, '//div[contains(@class,"game-list")]/div')
    List_Game_Heading = UiObject(By.XPATH, '//h1[contains(@class,"game-section__title")]')


class CasinoLocators(object):
    NCC_All = UiObject(By.CLASS_NAME, 'game-menu-item-icon__tab')
    NCC_Evolution = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][2]')
    NCC_Ebet = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][3]')
    NCC_Vivo = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][4]')
    NCC_Allbet = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][5]')
    NCC_HGaming = UiObject(By.XPATH, '//div[contains(@class,"game-menu-item")][6]')

    Game_selector = UiObject(By.CLASS_NAME, 'btn-secondary')
    Game_Baccarat = UiObject(By.XPATH, '//input[@value="baccarat"]/parent::div/parent::label/parent::a/parent::li')
    Game_Sicbo = UiObject(By.XPATH, '//input[@value="sicbo"]/parent::div/parent::label/parent::a/parent::li')
    Game_Roulette = UiObject(By.XPATH, '//input[@value="roulette"]/parent::div/parent::label/parent::a/parent::li')

    Sort_Nhieu_nguoi_choi = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][1]')
    Sort_Dang_hot = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][2]')
    Sort_Pho_bien = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][3]')
    Sort_Moi_nhat = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][4]')
    Sort_a_z = UiObject(By.XPATH, '//label[contains(@class,"base-radio__wrap")][5]')

    List_Game = UiObject(By.XPATH, '//div[contains(@class,"lobby-casino-list")]/div')
    List_Game_Heading = UiObject(By.CLASS_NAME, 'lobby-casino-section__title')


class LoginLocators(object):
    input_username = UiObject(By.XPATH, '//form/div[1]/div/input')
    input_password = UiObject(By.XPATH, '//form/div[2]/div/input')

    text_error_username = UiObject(By.XPATH, '//form/div[1]/p[@class="error"]')
    text_error_password = UiObject(By.XPATH, '//form/div[2]/p[@class="error"]')

    btn_show_password = UiObject(By.CLASS_NAME, 'icon-eye-hide')
    btn_hide_password = UiObject(By.CLASS_NAME, 'icon-eye-show')
    btn_login = UiObject(By.CLASS_NAME, 'login-form__submit')
    btn_close = UiObject(By.CLASS_NAME, 'close-user-modal')

    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')


class SignupLocators(object):
    username = UiObject(By.XPATH, '//form/div[1]/div/input')
    password = UiObject(By.XPATH, '//form/div[2]/div/input')
    re_password = UiObject(By.NAME, 'confirmPassword')
    phoneno = UiObject(By.NAME, 'phoneNumber')
    invite_code = UiObject(By.XPATH, '//form/div[5]/div/input')

    username_error = UiObject(By.XPATH, '//form/div[1]/p[@class="error"]')
    password_error = UiObject(By.XPATH, '//form/div[2]/p[@class="error"]')
    re_password_error = UiObject(By.XPATH, '//form/div[3]/p[@class="error"]')
    phoneno_error = UiObject(By.XPATH, '//form/div[4]/p[@class="error"]')

    show_pass = UiObject(By.XPATH, '//form/div[2]/div/span')
    hide_pass = UiObject(By.XPATH, '//form/div[2]/div/span')
    show_repass = UiObject(By.XPATH, '//form/div[3]/div/span')
    hide_repass = UiObject(By.XPATH, '//form/div[3]/div/span')

    btn_register = UiObject(By.CLASS_NAME, 'register-form__submit')
    btn_close = UiObject(By.CLASS_NAME, 'close-user-modal')
    btn_agree = UiObject(By.CLASS_NAME, 'checkmark')

    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')


class UserInfoLocator(object):
    # DROP DOWN MENU
    drop_info = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][1]')
    drop_nap_tien = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][2]')
    drop_rut_tien = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][3]')
    drop_lich_su = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][4]')
    drop_khuyen_mai = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][5]')
    drop_tin_tuc = UiObject(By.XPATH, '//ul/div/li[@role="presentation"][6]')
    drop_logout = UiObject(By.XPATH, '//ul/div[@class="logout"]')
    drop_username = UiObject(By.XPATH, '//div[@class="user-name"]/span')

    # LEFT MENU
    btn_userinfo = UiObject(By.XPATH, '//span[@class="icon-information"]/parent::a/parent::li')
    btn_nap = UiObject(By.XPATH, '//span[@class="icon-deposit"]/parent::a/parent::li')
    btn_rut = UiObject(By.XPATH, '//span[@class="icon-withdraw"]/parent::a/parent::li')
    btn_history = UiObject(By.XPATH, '//span[@class="icon-history"]/parent::a/parent::li')
    btn_promotion = UiObject(By.XPATH, '//span[@class="icon-promotion"]/parent::a/parent::li')
    btn_logout = UiObject(By.CLASS_NAME, 'menu-info__logout')
    txt_username = UiObject(By.CLASS_NAME, 'menu-info__name')

    # TAB
    tab_info = UiObject(By.XPATH, '//ul/li[@class="nav-item"][1]')
    tab_changepass = UiObject(By.XPATH, '//ul/li[@class="nav-item"][2]')
    tab_bankaccount = UiObject(By.XPATH, '//ul/li[@class="nav-item"][3]')

    # CẬP NHẬT THÔNG TIN CÁ NHÂN
    info_name = UiObject(By.XPATH, '//div/div[1]/div/input')
    info_name_error = UiObject(By.XPATH, '//div/div[1]/p[@class="error"]')
    info_email = UiObject(By.XPATH, '//div/div[2]/div/input')
    info_email_error = UiObject(By.XPATH, '//div/div[2]/p[@class="error"]')
    info_email_authen = UiObject(By.XPATH, '//div/div[2]/div/p[@class="info-personal__authen"')
    info_phone = UiObject(By.XPATH, '//div/div[3]/div/input')
    info_phone_authen = UiObject(By.XPATH, '//div/div[3]/div/p[@class="info-personal__authen"')
    info_confirm = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div/button')

    # CONFIRM POPUP
    popup_cf = UiObject(By.ID, 'authen-email___BV_modal_content_')
    popup_cf_title = UiObject(By.CLASS_NAME, 'modal__content__title')
    popup_cf_content = UiObject(By.CLASS_NAME, 'content-form__desc')
    popup_cf_btn_confirm = UiObject(By.XPATH, '//div[@class="modal__content__inner"]/div/div/button')
    popup_cf_close = UiObject(By.CLASS_NAME, 'icon-close')
    popup_cf_resend = UiObject(By.XPATH, '//p[@class="content-form__note"]/span')

    # ERROR POPUP
    popup_error = UiObject(By.XPATH, '//div[@class="swal-modal"]')
    popup_error_title = UiObject(By.XPATH, '//div[@class="swal-title"]')
    popup_error_content = UiObject(By.XPATH, '//div[@class="swal-text"]')
    popup_error_btn_confirm = UiObject(By.CLASS_NAME, 'swal-button--confirm')

    # THAY ĐỔI MẬT KHẨU
    chg_cur_pass = UiObject(By.XPATH, '//div/div[1]/div/input')
    chg_cur_pass_error = UiObject(By.XPATH, '//div/div[1]/p[@class="error"]')
    chg_new_pass = UiObject(By.XPATH, '//div/div[2]/div/input')
    chg_new_pass_error = UiObject(By.XPATH, '//div/div[2]/p[@class="error"]')
    chg_re_new_pass = UiObject(By.XPATH, '//div/div[3]/div/input')
    chg_re_new_pass_error = UiObject(By.XPATH, '//div/div[3]/p[@class="error"]')
    chg_confirm = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div/button')
    show_cur_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[1]/div/span')
    hide_cur_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[1]/div/span')
    show_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[2]/div/span')
    hide_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[2]/div/span')
    show_re_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[3]/div/span')
    hide_re_new_pass = UiObject(By.XPATH, '//div[@class="tab-content"]/div/div/div/div[3]/div/span')


class RechargeLocators:
    # TYPE OF RECHARGE
    rc_bank = UiObject(By.XPATH, '//span[@class="icon-bank"]/parent::div')
    rc_card = UiObject(By.XPATH, '//span[@class="icon-card"]/parent::div')
    rc_momo = UiObject(By.XPATH, '//span[@class="icon-momo"]/parent::div')
    rc_paywin = UiObject(By.XPATH, '//span[@class="icon-paywin"]/parent::div')

    # SELECT BONUS AT THE FIRST TIME
    first_100 = UiObject(By.CLASS_NAME, 'deposit-welcome__item--package-2')
    first_40 = UiObject(By.CLASS_NAME, 'deposit-welcome__item--package-3')
    first_125 = UiObject(By.CLASS_NAME, 'deposit-welcome__item--package-1')

    first_100_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-welcome__item--package-2")]/div')
    first_40_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-welcome__item--package-3")]/div')
    first_125_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-welcome__item--package-1")]/div')

    # SELECT BANK
    bank_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')
    bank_Sacombank = UiObject(By.LINK_TEXT, 'Sacombank')
    bank_Techcombank = UiObject(By.LINK_TEXT, 'Techcombank')
    bank_Vietcombank = UiObject(By.LINK_TEXT, 'Vietcombank')
    bank_VietinBank = UiObject(By.LINK_TEXT, 'VietinBank')
    bank_ACB = UiObject(By.LINK_TEXT, 'ACB')
    bank_DongA = UiObject(By.LINK_TEXT, 'DongA')

    # BANK INFO
    copy_owner_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][1]/div')
    copy_owner_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][1]/div/p[3]')
    copy_number_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][2]/div')
    copy_number_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][2]/div/p[3]')
    copy_place_btn = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][3]/div')
    copy_place_text = UiObject(By.XPATH, '//li[contains(@class,"deposit-bank-account__item")][3]/div/p[3]')

    # TYPE SELECTOR
    type_ibanking = UiObject(By.XPATH, '//input[@value="ibanking"]/parent::label/div')
    type_atm = UiObject(By.XPATH, '//input[@value="atm"]/parent::label/div')
    type_banking = UiObject(By.XPATH, '//input[@value="banking"]/parent::label/div')

    # INPUT FORM
    in_amount = UiObject(By.NAME, 'amount')
    in_amount_error = UiObject(By.XPATH, '//input[@name="amount"]/parent::div/parent::div/p[@class="error"]')
    out_amount = UiObject(By.XPATH, '//p[@class="base-input-custom__vnd"]')
    in_name = UiObject(By.NAME, 'fromBankName')
    in_name_error = UiObject(By.XPATH, '//input[@name="fromBankName"]/parent::div/parent::div/p[@class="error"]')
    in_code = UiObject(By.NAME, 'bankTrancode')
    in_code_error = UiObject(By.XPATH, '//input[@name="bankTrancode"]/parent::div/parent::div/p[@class="error"]')

    # PROMO SELECTOR
    promo_100 = UiObject(By.CLASS_NAME, 'promotion-item--package-2')
    promo_40 = UiObject(By.CLASS_NAME, 'promotion-item--package-3')
    promo_125 = UiObject(By.CLASS_NAME, 'promotion-item--package-1')

    amount_promo = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/li[1]/p[2]')
    amount_real = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/li[2]/p[2]')
    amount_minbet = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/li[3]/p[2]')
    finished_date = UiObject(By.XPATH, '//div[contains(@class,"deposit-promotion__note")]/ul/p/span')

    # BUTTON
    TAO_PHIEU_NAP = UiObject(By.XPATH, '//div[contains(@class,"deposit-bank")]/div/div/button')

    # DATA HELPTEXT:
    data_helptext = {
        'iBanking': {
            'Vietcombank': 'Vui lòng nhập số lệnh giao dịch',
            'ACB': 'Vui lòng nhập số tài khoản người gửi',
            'DongA': 'Vui lòng nhập số tài khoản người gửi',
            'Vietinbank': 'Vui lòng nhập thời gian chuyển tiền',
            'BIDV': 'Vui lòng nhập số tài khoản người gửi hoặc thời gian chuyển tiền',
            'Sacombank': 'Vui lòng nhập thời gian chuyển tiền',
            'Techcombank': 'Vui lòng nhập số bút toán hoặc số tài khoản người gửi'},
        'ATM': {
            'Vietcombank': 'Vui lòng nhập số tài khoản người gửi',
            'ACB': 'Vui lòng nhập số tài khoản người gửi',
            'DongA': 'Vui lòng nhập số tài khoản người gửi',
            'Vietinbank': 'Vui lòng nhập thời gian chuyển tiền',
            'BIDV': 'Vui lòng nhập số tài khoản người gửi',
            'Sacombank': 'Vui lòng nhập thời gian chuyển tiền',
            'Techcombank': 'Vui lòng nhập số tài khoản người gửi'},
        'Cash': {
            'Vietcombank': 'Vui lòng nhập họ và tên người gửi',
            'ACB': 'Vui lòng nhập họ và tên người gửi',
            'DongA': 'Vui lòng nhập họ và tên người gửi',
            'Vietinbank': 'Vui lòng nhập họ và tên người gửi',
            'BIDV': 'Vui lòng nhập họ và tên người gửi',
            'Sacombank': 'Vui lòng nhập họ và tên người gửi',
            'Techcombank': 'Vui lòng nhập họ và tên người gửi'}
    }
    data_listBanks = {
        'Vietcombank': bank_Vietcombank,
        'ACB': bank_ACB,
        'DongA': bank_DongA,
        'Vietinbank': bank_VietinBank,
        # 'BIDV': bank.BIDV,
        'Sacombank': bank_Sacombank,
        'Techcombank': bank_Techcombank
    }

    data_listBankMethod = {
        'iBanking': type_ibanking,
        'ATM': type_atm,
        'Cash': type_banking
    }
