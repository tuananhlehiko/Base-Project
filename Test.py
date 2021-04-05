import threading
import unittest
from selenium import webdriver
import time
from datetime import datetime
import xlsxwriter

from TopAsia.src.pages.Browser import Browser
import time
import os
from datetime import datetime
from random import randint
import re
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.UIObject import UiObject


a = ['!','@','#','$','%','^','&','*','(',')',' ',';',':',"'",'"','`','~','>','.','<','{','}','[',']','\\',',','/','-','=','+']

date = re.sub('[ :-]','',str(datetime.now()).split('.')[0])   

class CasinoLobbyHeadingTitle(unittest.TestCase):
    def setUp(self):
        self.driver = Browser.get_driver()
        self.driver.get(ge.DOMAIN)

    # TOP - Link url check
    def test_Heading_Title_Content(self):
        item = UiObject(*MainMenuLocators.MENU_CONG_GAME)
        print(item.get_attribute('class'))

  


    def tearDown(self):
        self.driver.close()
a= {'iBanking':{'Vietcombank':'Vui lòng nhập số lệnh giao dịch','ACB':'Vui lòng nhập số tài khoản người gửi','DongA':'Vui lòng nhập số tài khoản người gửi','Vietinbank':'Vui lòng nhập thời gian chuyển tiền','BIDV':'Vui lòng nhập số tài khoản người gửi hoặc thời gian chuyển tiền','Sacombank':'Vui lòng nhập thời gian chuyển tiền','Techcombank':'Vui lòng nhập số bút toán hoặc số tài khoản người gửi',},	'ATM':{'Vietcombank':'Vui lòng nhập số tài khoản người gửi','ACB':'Vui lòng nhập số tài khoản người gửi','DongA':'Vui lòng nhập số tài khoản người gửi','Vietinbank':'Vui lòng nhập thời gian chuyển tiền','BIDV':'Vui lòng nhập số tài khoản người gửi','Sacombank':'Vui lòng nhập thời gian chuyển tiền','Techcombank':'Vui lòng nhập số tài khoản người gửi',},	'Cash':{'Vietcombank':'Vui lòng nhập họ và tên người gửi','ACB':'Vui lòng nhập họ và tên người gửi','DongA':'Vui lòng nhập họ và tên người gửi','Vietinbank':'Vui lòng nhập họ và tên người gửi','BIDV':'Vui lòng nhập họ và tên người gửi','Sacombank':'Vui lòng nhập họ và tên người gửi','Techcombank':'Vui lòng nhập họ và tên người gửi',},}

print(a['iBanking']['Vietcombank'])


# if __name__ == "__main__":
#     unittest.main()
