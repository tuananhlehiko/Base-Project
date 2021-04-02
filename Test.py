import threading
import time
import os
from datetime import datetime
from random import randint
import re
from TopAsia.src.pages.locators import *
from TopAsia.src.pages.UIObject import UiObject


a = ['!','@','#','$','%','^','&','*','(',')',' ',';',':',"'",'"','`','~','>','.','<','{','}','[',']','\\',',','/','-','=','+']

date = re.sub('[ :-]','',str(datetime.now()).split('.')[0])   


