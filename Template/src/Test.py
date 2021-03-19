import threading
import time
import os
from datetime import datetime
from random import randint
# from pages.Browser import Browser


# def search(query_strings):
#     driver = Browser.get_driver()
#     for query in query_strings:
#         driver.get("https://www.google.com/search?q={}".format(query))
#         time.sleep(randint(1, 5))  # just to make it a bit more interesting
# queries = [["test+junkie+selenium", "test+junkie+webdriver", "test+junkie+testing+framework"],
#            ["cats", "cute+cats", "tigers"],
#            ["dogs", "cute+dogs", "wolfs"]]
# threads = []
# for query_set in queries:
#     thread = threading.Thread(target=search, args=(query_set,))
#     threads.append(thread)
#     thread.start()
# for thread in threads:
#     thread.join()

# start = datetime.now()
# time.sleep(15)
# end = datetime.now()

# a = end-start
# print(a)

dir_folder = os.getcwd() + '\\reports'
print(dir_folder)

List_Game = [
            [object, 'Baccarat', 'type=baccarat'],
            [object, 'Sicbo', 'type=sicbo'],
            [object, 'Roulette', 'type=roulette']
]

List_NCC = [
    [object, 'All', 'ncc=all'],
    [object, 'Evolution', 'ncc=evolution'],
    [object, 'Ebet', 'ncc=ebet'],
    [object, 'VivoGaming', 'ncc=vvgaming'],
    [object, 'Allbet', 'ncc=allbet'],
    [object, 'HGaming', 'ncc=hgaming']
]

List_Sort = [
    [object, 'Nhiều người chơi', 'sx=nhieu-nguoi-choi'],
    [object, 'Đang hot', 'sx=dang-hot'],
    [object, 'Phổ biến', 'sx=pho-bien'],
    [object, 'Mới nhất', 'sx=moi-nhat'],
    [object, 'A-Z', 'sx=a-z']
]

DATA = [
    # [object, 'HGaming', 'ncc=hgaming'],
    # [object, 'Baccarat', 'type=baccarat'],
    # [object, 'Sicbo', 'type=sicbo'],
    # [object, 'Roulette', 'type=roulette'],
    [object, 'Phổ biến', 'sx=pho-bien']
]
expected = 'http://dev-ta.mooo.com/casino?'
actual = 'http://dev-ta.mooo.com/casino?sx=pho-bien&game=roulette&game=sicbo&game=baccarat&type=hgaming'
TYPE = []
NCC = []
SORT = []
data_return = [1]
for i in DATA:
    if 'type' in i[2]:
        TYPE.append(i)
    if 'ncc' in i[2]:
        NCC.append(i)
    if 'sx' in i[2]:
        SORT.append(i)
if len(TYPE) > 1:
    for t in range(len(TYPE)):
        if t == 0:
            expected = expected + TYPE[t][2]
        else:
            expected = expected + ','+TYPE[t][2].split('=')[1]
elif len(TYPE) == 1:
    expected = expected + TYPE[0][2]
for t in TYPE:
    data_return.append(t[1])
if len(TYPE) > 0:
    if len(NCC) != 0:
        expected = expected + '&' + NCC[0][2]
        data_return.append(NCC[0][1])
    if len(SORT) != 0:
        expected = expected + '&' + SORT[0][2]
        data_return.append(SORT[0][1])
else:
    if len(NCC) != 0:
        expected = expected + NCC[0][2]
        data_return.append(NCC[0][1])
        if len(SORT) != 0:
            expected = expected + '&' + SORT[0][2]
            data_return.append(SORT[0][1])
    else:
        expected = expected + SORT[0][2]
        data_return.append(SORT[0][1])

while len(data_return) < 6:
    data_return.append('-')
print(expected)
print(data_return)
