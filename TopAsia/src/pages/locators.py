from selenium.webdriver.common.by import By
from TopAsia.src.pages.UIObject import UiObject


class ge(object):
    # DOMAIN = 'http://v2.fabet.info/'
    # DOMAIN = 'http://dev-ta.mooo.com/'
    DOMAIN = 'http://localhost:6677/'
    ProjectName = 'TopAsia'


class DefaultLocators(object):
    df_btn_close = UiObject(By.XPATH, '//*[@data-hkatt="df-btn-close"]')
    df_btn_logout = UiObject(By.XPATH, '//*[@data-hkatt="df-btn-logout"]')


class MainMenuLocators(object):
    mm_btn_the_thao = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-the-thao']")
    mm_btn_ban_ca = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-ban-ca']")
    mm_btn_live_casino = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-live-casino']")
    mm_btn_game_nhanh = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-game-nhanh']")
    mm_btn_table_game = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-table-game']")
    mm_btn_cong_game = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-cong-game']")
    mm_btn_dang_nhap = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-dang-nhap']")
    mm_btn_dang_ky = UiObject(By.XPATH, "//*[@data-hkatt='mm-btn-dang-ky']")

    mm_btn_khuyen_mai = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-khuyen-mai"]')
    mm_btn_tin_tuc = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-tin-tuc"]')
    mm_btn_game_vua_choi = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-game-vua-choi"]')

    mm_btn_nap_tien = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-nap-tien"]')
    mm_btn_chuyen_vi = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-chuyen-vi"]')
    mm_txt_cvi_tong_vi = UiObject(By.XPATH, '//*[@data-hkatt="mm-txt-cvi-tong-vi"]')
    mm_txt_cvi_vi_chinh = UiObject(By.XPATH, '//*[@data-hkatt="mm-txt-cvi-vi-chinh"]')
    mm_txt_cvi_vi_phu = UiObject(By.XPATH, '//*[@data-hkatt="mm-txt-cvi-vi-phu"]')
    mm_txt_cvi_content = UiObject(By.XPATH, '//*[@data-hkatt="mm-txt-cvi-content"]')
    mm_btn_cvi_nap_tien = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-cvi-nap-tien"]')

    mm_btn_open_dropdown = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-open-dropdown"]')
    mm_btn_drop_userinfo = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-userinfo"]')
    mm_btn_drop_recharge = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-recharge"]')
    mm_btn_drop_withdraw = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-withdraw"]')
    mm_btn_drop_history = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-history"]')
    mm_btn_drop_promo = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-promo"]')
    mm_btn_drop_news = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-news"]')
    mm_btn_drop_logout = UiObject(By.XPATH, '//*[@data-hkatt="mm-btn-drop-logout"]')


class CongGameLocators(object):
    cg_btn_type_all = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-all"]')
    cg_btn_type_no_hu = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-no-hu"]')
    cg_btn_type_ban_ca = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-ban-ca"]')
    cg_btn_type_lo_de = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-lo-de"]')
    cg_btn_type_ingame = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-ingame"]')
    cg_btn_type_table_game = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-table-game"]')
    cg_btn_type_game_nhanh = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-type-game-nhanh"]')

    cg_btn_ncc_selector = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-selector"]')
    cg_btn_ncc_all = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-all"]')
    cg_btn_ncc_techplay = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-techplay"]')
    cg_btn_ncc_pragmatic_play = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-pragmatic-play"]')
    cg_btn_ncc_cq9 = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-cq9"]')
    cg_btn_ncc_tomhorn = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-tomhorn"]')
    cg_btn_ncc_playngo = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-ncc-playngo"]')

    cg_btn_sort_nhieu_nguoi_choi = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-sort-nhieu-nguoi-choi"]')
    cg_btn_sort_dang_hot = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-sort-dang-hot"]')
    cg_btn_sort_pho_bien = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-sort-pho-bien"]')
    cg_btn_sort_moi_nhat = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-sort-moi-nhat"]')
    cg_btn_sort_a_z = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-sort-a-z"]')

    cg_btn_xem_them = UiObject(By.XPATH, '//*[@data-hkatt="cg-btn-xem-them"]')
    cg_lst_danh_sach_game = UiObject(By.XPATH, '//*[@data-hkatt="cg-lst-danh-sach-game"]')
    cg_lst_danh_sach_ten_game = UiObject(By.XPATH, '//*[@data-hkatt="cg-lst-danh-sach-ten-game"]')
    cg_txt_heading_title = UiObject(By.XPATH, '//*[@data-hkatt="cg-txt-heading-title"]')
    # Ce NOT DONE

    data_list_type = [
        [cg_btn_type_all, 'Tất Cả', 'type=all'],
        [cg_btn_type_no_hu, 'Nổ Hũ', 'type=slots'],
        [cg_btn_type_ban_ca, 'Bắn Cá', 'type=fishing'],
        [cg_btn_type_game_nhanh, 'Game Nhanh', 'type=instant'],
        [cg_btn_type_ingame, 'InGame', 'type=ingame'],
        [cg_btn_type_table_game, 'Table Games', 'type=tables'],
        [cg_btn_type_lo_de, 'Lô Đề', 'type=lode']
    ]

    data_list_ncc = [
        # [NCC_btn_All, 'Tất Cả', 'ncc=all'],
        [cg_btn_ncc_pragmatic_play, 'Pragmatic Play', 'ncc=pragmatic'],
        [cg_btn_ncc_cq9, 'CQ9', 'ncc=cq9'],
        [cg_btn_ncc_techplay, 'Techplay', 'ncc=vingame'],
        [cg_btn_ncc_tomhorn, 'Tomhorn Gaming', 'ncc=tomhorn'],
        [cg_btn_ncc_playngo, 'Play’n GO', 'ncc=playngo']
    ]

    data_list_sort = [
        [cg_btn_sort_nhieu_nguoi_choi, 'Nhiều Người Chơi', 'sx=most-played'],
        [cg_btn_sort_dang_hot, 'Đang Hot', 'sx=hot'],
        [cg_btn_sort_pho_bien, 'Phổ Biến', 'sx=popular'],
        [cg_btn_sort_moi_nhat, 'Mới Nhất', 'sx=new'],
        [cg_btn_sort_a_z, 'A-Z', 'sx=name']
    ]


class CasinoLocators(object):
    lc_btn_ncc_all = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-ncc-all"]')
    lc_btn_ncc_evolution = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-ncc-evolution"]')
    lc_btn_ncc_ebet = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-ncc-ebet"]')
    lc_btn_ncc_vivogaming = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-ncc-vivogaming"]')
    lc_btn_ncc_allbet = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-ncc-allbet"]')
    lc_btn_ncc_hogaming = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-ncc-hogaming"]')

    lc_btn_game_type_selector = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-game-type-selector"]')
    lc_btn_game_type_baccarat = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-game-type-baccarat"]')
    lc_btn_game_type_sicbo = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-game-type-sicbo"]')
    lc_btn_game_type_roulette = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-game-type-roulette"]')

    lc_btn_sort_nhieu_nguoi_choi = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-sort-nhieu-nguoi-choi"]')
    lc_btn_sort_dang_hot = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-sort-dang-hot"]')
    lc_btn_sort_pho_bien = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-sort-pho-bien"]')
    lc_btn_sort_moi_nhat = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-sort-moi-nhat"]')
    lc_btn_sort_a_z = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-sort-a-z"]')

    lc_btn_xem_them = UiObject(By.XPATH, '//*[@data-hkatt="lc-btn-xem-them"]')
    lc_lst_danh_sach_game = UiObject(By.XPATH, '//*[@data-hkatt="lc-lst-danh-sach-game"]')
    lc_lst_danh_sach_ten_game = UiObject(By.XPATH, '//*[@data-hkatt="lc-lst-danh-sach-ten-game"]')
    lc_txt_heading_title = UiObject(By.XPATH, '//*[@data-hkatt="lc-txt-heading-title"]')

    # Data
    data_list_game_type = [
        [lc_btn_game_type_baccarat, 'Baccarat', 'type=baccarat'],
        # [lc_btn_game_type_sicbo, 'Sicbo', 'type=sicbo'],
        [lc_btn_game_type_roulette, 'Roulette', 'type=roulette']
    ]

    data_list_ncc = [
        [lc_btn_ncc_all, 'All', 'ncc=all'],
        [lc_btn_ncc_evolution, 'Evolution', 'ncc=evo'],
        [lc_btn_ncc_ebet, 'Ebet', 'ncc=ebet'],
        [lc_btn_ncc_vivogaming, 'VivoGaming', 'ncc=vivo'],
        [lc_btn_ncc_allbet, 'Allbet', 'ncc=allbet'],
        [lc_btn_ncc_hogaming, 'HGaming', 'ncc=hogaming']
    ]

    data_list_sort = [
        [lc_btn_sort_nhieu_nguoi_choi, 'Nhiều Người Chơi', 'sx=most-played'],
        [lc_btn_sort_dang_hot, 'Đang Hot', 'sx=hot'],
        [lc_btn_sort_pho_bien, 'Phổ Biến', 'sx=popular'],
        [lc_btn_sort_moi_nhat, 'Mới Nhất', 'sx=new'],
        # [lc_btn_sort_a_z, 'A-Z', 'sx=name']
    ]


class LoginLocators(object):
    lg_in_username = UiObject(By.XPATH, '//*[@data-hkatt="lg-in-username"]')
    lg_btn_forgot_password = UiObject(By.XPATH, '//*[@data-hkatt="lg-btn-forgot-password"]')
    lg_in_password = UiObject(By.XPATH, '//*[@data-hkatt="lg-in-password"]')

    lg_in_password_error = UiObject(By.XPATH, '//*[@data-hkatt="lg-in-password-error"]')
    lg_in_username_error = UiObject(By.XPATH, '//*[@data-hkatt="lg-in-username-error"]')

    lg_ico_show_password = UiObject(By.XPATH, '//*[@data-hkatt="lg-ico-show-password"]')
    lg_ico_hide_password = UiObject(By.XPATH, '//*[@data-hkatt="lg-ico-hide-password"]')
    lg_btn_login = UiObject(By.XPATH, '//*[@data-hkatt="lg-btn-login"]')


class PopupLocators(object):
    pop_el_is_display = UiObject(By.XPATH, '//*[contains(@class,"swal-modal")]')
    pop_txt_title = UiObject(By.XPATH, '//*[contains(@class,"swal-title")]')
    pop_txt_content = UiObject(By.XPATH, '//*[contains(@class,"swal-text")]')
    pop_btn_confirm = UiObject(By.XPATH, '//*[contains(@class,"swal-button")]')


class SignupLocators(object):
    su_in_username = UiObject(By.XPATH, '//*[@data-hkatt="su-in-username"]')
    su_in_password = UiObject(By.XPATH, '//*[@data-hkatt="su-in-password"]')
    su_in_repassword = UiObject(By.XPATH, '//*[@data-hkatt="su-in-repassword"]')
    su_in_phone_no = UiObject(By.XPATH, '//*[@data-hkatt="su-in-phone-no"]')
    su_in_invite_code = UiObject(By.XPATH, '//*[@data-hkatt="su-in-invite-code"]')

    su_txt_username_error = UiObject(By.XPATH, '//*[@data-hkatt="su-txt-username-error"]')
    su_txt_password_error = UiObject(By.XPATH, '//*[@data-hkatt="su-txt-password-error"]')
    su_txt_repassword_error = UiObject(By.XPATH, '//*[@data-hkatt="su-txt-repassword-error"]')
    su_txt_phone_no_error = UiObject(By.XPATH, '//*[@data-hkatt="su-txt-phone-no-error"]')

    su_ico_show_password = UiObject(By.XPATH, '//*[@data-hkatt="su-ico-show-password"]')
    su_ico_hide_password = UiObject(By.XPATH, '//*[@data-hkatt="su-ico-hide-password"]')
    su_ico_show_repassword = UiObject(By.XPATH, '//*[@data-hkatt="su-ico-show-repassword"]')
    su_ico_hide_repassword = UiObject(By.XPATH, '//*[@data-hkatt="su-ico-hide-repassword"]')

    su_btn_agree_tou = UiObject(By.XPATH, '//*[@data-hkatt="su-btn-agree-tou"]')
    su_btn_register = UiObject(By.XPATH, '//*[@data-hkatt="su-btn-register"]')
    su_btn_close = UiObject(By.XPATH, '//*[@data-hkatt="su-btn-close"]')


class LeftPanelLocator(object):
    lp_txt_left_panel_username = UiObject(By.XPATH, '//*[@data-hkatt="lp-txt-left-panel-username"]')
    lp_txt_left_panel_so_tien = UiObject(By.XPATH, '//*[@data-hkatt="lp-txt-left-panel-so-tien"]')
    lp_txt_left_panel_vi_chinh = UiObject(By.XPATH, '//*[@data-hkatt="lp-txt-left-panel-vi-chinh"]')
    lp_txt_left_panel_vi_phu = UiObject(By.XPATH, '//*[@data-hkatt="lp-txt-left-panel-vi-phu"]')

    lp_btn_left_panel_user_info = UiObject(By.XPATH, '//*[@data-hkatt="lp-btn-left-panel-user-info"]')
    lp_btn_left_panel_recharge = UiObject(By.XPATH, '//*[@data-hkatt="lp-btn-left-panel-recharge"]')
    lp_btn_left_panel_withdraw = UiObject(By.XPATH, '//*[@data-hkatt="lp-btn-left-panel-withdraw"]')
    lp_btn_left_panel_history = UiObject(By.XPATH, '//*[@data-hkatt="lp-btn-left-panel-history"]')
    lp_btn_left_panel_promo = UiObject(By.XPATH, '//*[@data-hkatt="lp-btn-left-panel-promo"]')
    lp_btn_left_panel_logout = UiObject(By.XPATH, '//*[@data-hkatt="lp-btn-left-panel-logout"]')


class UserInfoLocator(object):
    ui_btn_tab_user_info = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-tab-user-info"]')
    ui_btn_tab_change_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-tab-change-pass"]')
    ui_btn_tab_bank_info = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-tab-bank-info"]')

    ui_in_account_name = UiObject(By.XPATH, '//*[@data-hkatt="ui-in-account-name"]')
    ui_in_account_email = UiObject(By.XPATH, '//*[@data-hkatt="ui-in-account-email"]')
    ui_in_phone_no = UiObject(By.XPATH, '//*[@data-hkatt="ui-in-phone-no"]')
    ui_txt_account_name_error = UiObject(By.XPATH, '//*[@data-hkatt="ui-txt-account-name-error"]')
    ui_txt_account_email_error = UiObject(By.XPATH, '//*[@data-hkatt="ui-txt-account-email-error"]')
    ui_txt_phone_no_error = UiObject(By.XPATH, '//*[@data-hkatt="ui-txt-phone-no-error"]')
    ui_btn_email_confirm = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-email-confirm"]')
    ui_btn_phone_no_confirm = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-phone-no-confirm"]')
    ui_btn_info_confirm = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-info-confirm"]')

    ui_in_current_password = UiObject(By.XPATH, '//*[@data-hkatt="ui-in-current-password"]')
    ui_in_new_password = UiObject(By.XPATH, '//*[@data-hkatt="ui-in-new-password"]')
    ui_in_re_new_password = UiObject(By.XPATH, '//*[@data-hkatt="ui-in-re-new-password"]')
    ui_ico_show_current_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-ico-show-current-pass"]')
    ui_ico_hide_current_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-ico-hide-current-pass"]')
    ui_ico_show_new_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-ico-show-new-pass"]')
    ui_ico_hide_new_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-ico-hide-new-pass"]')
    ui_ico_show_re_new_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-ico-show-re-new-pass"]')
    ui_ico_hide_re_new_pass = UiObject(By.XPATH, '//*[@data-hkatt="ui-ico-hide-re-new-pass"]')
    ui_btn_change_pass_confirm = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-change-pass-confirm"]')

    ui_btn_them_ngan_hang = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-them-ngan-hang"]')

    # CONFIRM POPUP
    ui_el_confirm_popup = UiObject(By.XPATH, '//*[@data-hkatt="ui-el-confirm-popup"]')
    ui_btn_confirm_confirm = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-confirm-confirm"]')
    ui_btn_confirm_close = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-confirm-close"]')
    ui_btn_confirm_resend = UiObject(By.XPATH, '//*[@data-hkatt="ui-btn-confirm-resend"]')
    ui_txt_title = UiObject(By.XPATH, '//*[@data-hkatt="ui-txt-title"]')
    ui_txt_content = UiObject(By.XPATH, '//*[@data-hkatt="ui-txt-content"]')


class RechargeLocators(object):
    # REUSE LOCATOR
    rc_btn_recharge_confirm = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-recharge-confirm"]')
    rc_btn_huong_dan_nap_tien = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-huong-dan-nap-tien"]')

    rc_btn_promo_100 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-promo-100"]')
    rc_btn_promo_40 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-promo-40"]')
    rc_btn_promo_1dot6 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-promo-1dot6"]')

    rc_btn_first_recharge_100 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-first-recharge-100"]')
    rc_btn_first_recharge_40 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-first-recharge-40"]')
    rc_btn_first_recharge_1dot6 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-first-recharge-1dot6"]')

    # USING BANK LOCATOR
    rc_btn_tab_bank = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-tab-bank"]')
    rc_btn_tab_card = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-tab-card"]')
    rc_btn_tab_momo = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-tab-momo"]')
    rc_btn_tab_paywin = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-tab-paywin"]')

    rc_btn_bank_selector = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-selector"]')
    rc_btn_sacombank = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-sacombank"]')
    rc_btn_techcombank = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-techcombank"]')
    rc_btn_vietcombank = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-vietcombank"]')
    rc_btn_vietinbank = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-vietinbank"]')
    rc_btn_acb = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-acb"]')
    rc_btn_bidv = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bidv"]')
    rc_btn_donga = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-donga"]')

    rc_btn_bank_type_ibanking = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-type-ibanking"]')
    rc_btn_bank_type_atm = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-type-atm"]')
    rc_btn_bank_type_banking = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-type-banking"]')

    rc_in_bank_amount = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-bank-amount"]')
    rc_in_bank_sender_name = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-bank-sender-name"]')
    rc_in_bank_code = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-bank-code"]')
    rc_txt_bank_amount_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-amount-error"]')
    rc_txt_bank_sender_name_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-sender-name-error"]')
    rc_txt_bank_code_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-code-error"]')

    rc_btn_bank_promo_100 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-promo-100"]')
    rc_btn_bank_promo_40 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-promo-40"]')
    rc_btn_bank_promo_1dot6 = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-promo-1dot6"]')

    rc_txt_bank_output_amount = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-output-amount"]')

    rc_txt_bank_amount_promo = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-amount-promo"]')
    rc_txt_bank_amount_real = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-amount-real"]')
    rc_txt_bank_amount_min_of_bet = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-amount-min-of-bet"]')
    rc_txt_bank_time_to_finish = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-time-to-finish"]')

    rc_btn_bank_recharge_confirm = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-recharge-confirm"]')
    rc_txt_bank_suggest_text = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-suggest-text"]')

    rc_btn_bank_copy_owner = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-copy-owner"]')
    rc_btn_bank_copy_account_no = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-copy-account-no"]')
    rc_btn_bank_copy_brand = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-bank-copy-brand"]')
    rc_txt_bank_copy_owner = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-copy-owner"]')
    rc_txt_bank_copy_account_no = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-copy-account-no"]')
    rc_txt_bank_copy_brand = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-bank-copy-brand"]')

    # RECHARGE USING CARD SELECTOR
    rc_btn_ncc_viettel = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-ncc-viettel"]')
    rc_btn_ncc_vinaphone = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-ncc-vinaphone"]')
    rc_btn_ncc_mobifone = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-ncc-mobifone"]')

    data_percentage_card_fee = {
        'viettel': 32,
        'vinaphone': 32,
        'mobifone': 34
    }

    rc_btn_card_selector = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-selector"]')
    rc_btn_card_10k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-10k"]')
    rc_btn_card_20k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-20k"]')
    rc_btn_card_30k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-30k"]')
    rc_btn_card_50k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-50k"]')
    rc_btn_card_100k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-100k"]')
    rc_btn_card_200k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-200k"]')
    rc_btn_card_300k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-300k"]')
    rc_btn_card_500k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-500k"]')
    rc_btn_card_1000k = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-card-1000k"]')

    rc_in_card_pin = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-card-pin"]')
    rc_in_card_series = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-card-series"]')
    rc_txt_card_pin_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-card-pin-error"]')
    rc_txt_card_series_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-card-series-error"]')

    rc_txt_card_fee = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-card-fee"]')
    rc_txt_card_real_received = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-card-real-received"]')

    # RECHARGE USING MOMO LOCATOR
    rc_btn_momo_selector = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-momo-selector"]')
    rc_btn_momo_account = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-momo-account"]')

    rc_in_momo_amount = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-momo-amount"]')
    rc_in_momo_sender_name = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-momo-sender-name"]')
    rc_in_momo_code = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-momo-code"]')

    rc_txt_momo_amount_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-momo-amount-error"]')
    rc_txt_momo_sender_name_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-momo-sender-name-error"]')
    rc_txt_momo_code_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-momo-code-error"]')

    rc_btn_momo_copy_phone_no = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-momo-copy-phone-no"]')
    rc_btn_momo_copy_owner = UiObject(By.XPATH, '//*[@data-hkatt="rc-btn-momo-copy-owner"]')
    rc_txt_momo_copy_phone_no = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-momo-copy-phone-no"]')
    rc_txt_momo_copy_owner = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-momo-copy-owner"]')

    # RECHARGE USING PAYWIN
    rc_el_paywin_page_is_load = UiObject(By.XPATH, '//*[@data-hkatt="rc-el-paywin-page-is-load"]')

    rc_in_paywin_amount = UiObject(By.XPATH, '//*[@data-hkatt="rc-in-paywin-amount"]')
    rc_txt_paywin_amount_error = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-paywin-amount-error"]')
    rc_txt_paywin_output_amount = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-paywin-output-amount"]')

    rc_txt_paywin_amount_promo = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-paywin-amount-promo"]')
    rc_txt_paywin_amount_real = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-paywin-amount-real"]')
    rc_txt_paywin_amount_min_of_bet = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-paywin-amount-min-of-bet"]')
    rc_txt_paywin_time_to_finish = UiObject(By.XPATH, '//*[@data-hkatt="rc-txt-paywin-time-to-finish"]')

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

    data_list_banks_bank = {
        'Vietcombank': rc_btn_vietcombank,
        'ACB': rc_btn_acb,
        'DongA': rc_btn_donga,
        'Vietinbank': rc_btn_vietinbank,
        # 'BIDV': rc_btn_bidv,
        'Sacombank': rc_btn_sacombank,
        'Techcombank': rc_btn_techcombank
    }

    data_list_banks_paywin = {
        'Vietcombank': rc_btn_vietcombank,
        'ACB': rc_btn_acb,
        # 'DongA': rc_btn_donga,
        'Vietinbank': rc_btn_vietinbank,
        # 'BIDV': rc_btn_bidv,
        'Sacombank': rc_btn_sacombank,
        'Techcombank': rc_btn_techcombank
    }

    data_list_bank_method = {
        'iBanking': rc_btn_bank_type_ibanking,
        'ATM': rc_btn_bank_type_atm,
        'Cash': rc_btn_bank_type_banking
    }

    data_list_card_amount = {
        'viettel': {
            '10k': [rc_btn_card_10k, 10000],
            '20k': [rc_btn_card_20k, 20000],
            '30k': [rc_btn_card_30k, 30000],
            '50k': [rc_btn_card_50k, 50000],
            '100k': [rc_btn_card_100k, 100000],
            '200k': [rc_btn_card_200k, 200000],
            '300k': [rc_btn_card_300k, 300000],
            '500k': [rc_btn_card_500k, 500000],
            '1000k': [rc_btn_card_1000k, 1000000]},
        'vinaphone': {
            '10k': [rc_btn_card_10k, 10000],
            '20k': [rc_btn_card_20k, 20000],
            '30k': [rc_btn_card_30k, 30000],
            '50k': [rc_btn_card_50k, 50000],
            '100k': [rc_btn_card_100k, 100000],
            '200k': [rc_btn_card_200k, 200000],
            '300k': [rc_btn_card_300k, 300000],
            '500k': [rc_btn_card_500k, 500000]},
        'mobifone': {
            '10k': [rc_btn_card_10k, 10000],
            '20k': [rc_btn_card_20k, 20000],
            '30k': [rc_btn_card_30k, 30000],
            '50k': [rc_btn_card_50k, 50000],
            '100k': [rc_btn_card_100k, 100000],
            '200k': [rc_btn_card_200k, 200000],
            '300k': [rc_btn_card_300k, 300000],
            '500k': [rc_btn_card_500k, 500000]}
    }

    data_list_card_supplier = {
        'viettel': rc_btn_ncc_viettel,
        'vinaphone': rc_btn_ncc_vinaphone,
        'mobifone': rc_btn_ncc_mobifone
    }


class WithdrawLocators:
    wd_btn_card_selector = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-selector"]')
    wd_btn_card_10k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-10k"]')
    wd_btn_card_20k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-20k"]')
    wd_btn_card_30k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-30k"]')
    wd_btn_card_50k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-50k"]')
    wd_btn_card_100k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-100k"]')
    wd_btn_card_200k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-200k"]')
    wd_btn_card_300k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-300k"]')
    wd_btn_card_500k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-500k"]')
    wd_btn_card_1000k = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-card-1000k"]')

    wd_btn_withdraw_confirm = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-withdraw-confirm"]')
    wd_btn_tab_bank = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-tab-bank"]')
    wd_btn_tab_card = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-tab-card"]')

    wd_btn_bank_select_account = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-bank-select-account"]')
    wd_lst_bank_account_list = UiObject(By.XPATH, '//*[@data-hkatt="wd-lst-bank-account-list"]')
    wd_in_bank_amount = UiObject(By.XPATH, '//*[@data-hkatt="wd-in-bank-amount"]')
    wd_in_bank_password = UiObject(By.XPATH, '//*[@data-hkatt="wd-in-bank-password"]')
    wd_txt_bank_output_amount = UiObject(By.XPATH, '//*[@data-hkatt="wd-txt-bank-output-amount"]')
    wd_ico_bank_show_password = UiObject(By.XPATH, '//*[@data-hkatt="wd-ico-bank-show-password"]')
    wd_ico_bank_hide_password = UiObject(By.XPATH, '//*[@data-hkatt="wd-ico-bank-hide-password"]')

    wd_btn_viettel = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-viettel"]')
    wd_btn_vinaphone = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-vinaphone"]')
    wd_btn_mobifone = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-mobifone"]')
    wd_in_card_password = UiObject(By.XPATH, '//*[@data-hkatt="wd-in-card-password"]')
    wd_ico_card_show_password = UiObject(By.XPATH, '//*[@data-hkatt="wd-ico-card-show-password"]')
    wd_ico_card_hide_password = UiObject(By.XPATH, '//*[@data-hkatt="wd-ico-card-hide-password"]')

    card_Selector = UiObject(By.CLASS_NAME, 'base-select__inner')

    data_listCardAmount = {
        'viettel': {
            '10k': [wd_btn_card_10k, 10000],
            '20k': [wd_btn_card_20k, 20000],
            '30k': [wd_btn_card_30k, 30000],
            '50k': [wd_btn_card_50k, 50000],
            '100k': [wd_btn_card_100k, 100000],
            '200k': [wd_btn_card_200k, 200000],
            '300k': [wd_btn_card_300k, 300000],
            '500k': [wd_btn_card_500k, 500000],
            '1000k': [wd_btn_card_1000k, 1000000]},
        'vinaphone': {
            '10k': [wd_btn_card_10k, 10000],
            '20k': [wd_btn_card_20k, 20000],
            '30k': [wd_btn_card_30k, 30000],
            '50k': [wd_btn_card_50k, 50000],
            '100k': [wd_btn_card_100k, 100000],
            '200k': [wd_btn_card_200k, 200000],
            '300k': [wd_btn_card_300k, 300000],
            '500k': [wd_btn_card_500k, 500000]},
        'mobifone': {
            '10k': [wd_btn_card_10k, 10000],
            '20k': [wd_btn_card_20k, 20000],
            '30k': [wd_btn_card_30k, 30000],
            '50k': [wd_btn_card_50k, 50000],
            '100k': [wd_btn_card_100k, 100000],
            '200k': [wd_btn_card_200k, 200000],
            '300k': [wd_btn_card_300k, 300000],
            '500k': [wd_btn_card_500k, 500000]}
    }

    wd_btn_ncc_viettel = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-ncc-viettel"]')
    wd_btn_ncc_vinaphone = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-ncc-vinaphone"]')
    wd_btn_ncc_mobifone = UiObject(By.XPATH, '//*[@data-hkatt="wd-btn-ncc-mobifone"]')

    data_list_card_supplier = {
        'viettel': wd_btn_viettel,
        'vinaphone': wd_btn_vinaphone,
        'mobifone': wd_btn_mobifone
    }
