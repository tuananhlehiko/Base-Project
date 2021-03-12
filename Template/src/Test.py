import threading
import time
from random import randint
from pages.Browser import Browser


def search(query_strings):
    driver = Browser.get_driver()
    for query in query_strings:
        driver.get("https://www.google.com/search?q={}".format(query))
        time.sleep(randint(1, 5))  # just to make it a bit more interesting
queries = [["test+junkie+selenium", "test+junkie+webdriver", "test+junkie+testing+framework"],
           ["cats", "cute+cats", "tigers"],
           ["dogs", "cute+dogs", "wolfs"]]
threads = []
for query_set in queries:
    thread = threading.Thread(target=search, args=(query_set,))
    threads.append(thread)
    thread.start()
for thread in threads:
    thread.join()