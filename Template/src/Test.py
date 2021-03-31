import threading
import time
import os
from datetime import datetime
from random import randint
import re
from pages.locators import *
from pages.UIObject import UiObject


a = ['!','@','#','$','%','^','&','*','(',')',' ',';',':',"'",'"','`','~','>','.','<','{','}','[',']','\\',',','/','-','=','+']

date = re.sub('[ :-]','',str(datetime.now()).split('.')[0])   
    
print(date)
# for i in a:
#     print(i)