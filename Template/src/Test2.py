from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint
import time

from src.page.UIObject import UiObject
from src.page.Browser import Browser

search_field = UiObject(By.NAME, "q")
search_icon = UiObject(By.XPATH, "//button[@jsname = 'Tg7LZd']")
driver = Browser.get_driver()
driver.get("https://google.com")
for query in ["test automation with Test Junkie",
              "Test Junkie with Selenium WebDriver",
              "Test Junkie tutorials"]:
    search_field.set_text(query)
    if not search_icon.exists():
        search_field.press_key(Keys.ENTER)
    else:
        search_icon.click()
    time.sleep(randint(1, 5))