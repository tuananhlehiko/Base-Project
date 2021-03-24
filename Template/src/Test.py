import threading
import time
import os
from datetime import datetime
from random import randint
import os
from pages.locators import *
from pages.UIObject import UiObject

# from TestCase.GameLobby_url_format import *
# from TestCase.CasinoLobby_url_format import *


DATA = [
    # [object, 'Tất cả', 'type=all'],
    # [object, 'Nổ hũ', 'type=no-hu'],
    # [object, 'Bắn Cá', 'type=ban-ca'],
    # [object, 'Game nhanh', 'type=quick-game'],
    # [object, 'Ingame', 'type=ingame'],
    # [object, 'Table game', 'type=table-games'],
    # [object, 'Lô đề', 'type=lo-de'],

    # [object, 'Pragmatic Play', 'ncc=pragmatic-play'],
    # [object, 'Đang hot', 'sx=dang-hot']
]


def check_link(data, number):
    expected = ''
    TYPE = []
    NCC = []
    SORT = []
    data_return = [number]
    # self.no += 1
    for i in data:
        if i != 0:
            if 'type' in i[2]:
                TYPE.append(i)
            if 'ncc' in i[2]:
                NCC.append(i)
            if 'sx' in i[2]:
                SORT.append(i)

    # RULE 1
    if len(NCC) > 0 or len(SORT) > 0:
        expected = expected + 'Top'

    # RULE 2, 3
    if len(NCC) > 0 or len(SORT) > 0:
        # listgame = UiObject(*CongGameLocators.List_Game)
        # number_of_game = len(listgame.get_elements())
        number_of_game = 79
        if number_of_game > 1:
            expected = expected + ' ' + str(number_of_game) + ' Trò Chơi'
    # RULE 4
    if len(TYPE) > 0:
        if TYPE[0][1] == 'Lô đề':
            expected = 'Lô Đề Truyền Thống Siêu Tốc'

        else:
            if len(TYPE) > 1:
                for t in TYPE:
                    expected = expected + ' ' + t[1]
            else:
                if TYPE[0][1] == 'type=all':
                    expected = ' Cổng Game'
                else:
                    expected = expected + ' ' + TYPE[0][1]
            if len(NCC) == 0 and len(SORT) == 0:
                expected = expected + ' Online'
            # RULE 5
            if len(SORT) > 0:
                expected = expected + ' ' + SORT[0][1]
            # RULE 6 & 7
            if len(NCC) > 0:
                expected = expected + ' Của ' + NCC[0][1]
    else:
        if len(NCC) == 0 and len(SORT) == 0:
            expected = expected + 'Cổng Game Online'
        # RULE 5
        if len(SORT) > 0:
            expected = expected + ' ' + SORT[0][1]
        # RULE 6 & 7
        if len(NCC) > 0:
            expected = expected + ' Của ' + NCC[0][1]

    for t in TYPE:
        data_return.append(t[1])
    if len(TYPE) > 0:
        if len(NCC) != 0:
            data_return.append(NCC[0][1])
        if len(SORT) != 0:
            data_return.append(SORT[0][1])
    else:
        if len(NCC) != 0:
            data_return.append(NCC[0][1])
            if len(SORT) != 0:
                data_return.append(SORT[0][1])
        else:
            if len(SORT) != 0:
                data_return.append(SORT[0][1])

    while len(data_return) < 4:
        data_return.append('-')
    data_return.append(expected)
    actual = 'Top 70 Trò Chơi'
    data_return.append(actual)
    if actual != expected:
        data_return.append('FAILED')
        # lobby.screenshot_window(str(number) + '_' + data_return[1] + '_' + data_return[2] + '_' + data_return[3]+ '_' + data_return[4]+ '_' + data_return[5])
    else:
        data_return.append('PASSED')
    print('\n', '-'*15, ' Case: ', number,
          ': ', data_return[6], ' ', 15*'-')
    print(data_return[1], ' - ', data_return[2], ' - ', data_return[3], ' - ')
    print('Expected link: \t', data_return[4])
    print('Actual link: \t', data_return[5])
    return data_return


check_link(DATA, 1)

# List_Game = [
#             [object, 'Baccarat', 'type=baccarat'],
#             [object, 'Sicbo', 'type=sicbo'],
#             [object, 'Roulette', 'type=roulette']
# ]

# List_NCC = [
#     [object, 'All', 'ncc=all'],
#     [object, 'Evolution', 'ncc=evolution'],
#     [object, 'Ebet', 'ncc=ebet'],
#     [object, 'VivoGaming', 'ncc=vvgaming'],
#     [object, 'Allbet', 'ncc=allbet'],
#     [object, 'HGaming', 'ncc=hgaming']
# ]

# List_Sort = [
#     [object, 'Nhiều người chơi', 'sx=nhieu-nguoi-choi'],
#     [object, 'Đang hot', 'sx=dang-hot'],
#     [object, 'Phổ biến', 'sx=pho-bien'],
#     [object, 'Mới nhất', 'sx=moi-nhat'],
#     [object, 'A-Z', 'sx=a-z']
# ]

# DATA = [
#     # [object, 'HGaming', 'ncc=hgaming'],
#     # [object, 'Baccarat', 'type=baccarat'],
#     # [object, 'Sicbo', 'type=sicbo'],
#     # [object, 'Roulette', 'type=roulette'],
#     [object, 'Phổ biến', 'sx=pho-bien']
# ]
# expected = 'http://dev-ta.mooo.com/casino?'
# actual = 'http://dev-ta.mooo.com/casino?sx=pho-bien&game=roulette&game=sicbo&game=baccarat&type=hgaming'
# TYPE = []
# NCC = []
# SORT = []
# data_return = [1]
# for i in DATA:
#     if 'type' in i[2]:
#         TYPE.append(i)
#     if 'ncc' in i[2]:
#         NCC.append(i)
#     if 'sx' in i[2]:
#         SORT.append(i)
# if len(TYPE) > 1:
#     for t in range(len(TYPE)):
#         if t == 0:
#             expected = expected + TYPE[t][2]
#         else:
#             expected = expected + ','+TYPE[t][2].split('=')[1]
# elif len(TYPE) == 1:
#     expected = expected + TYPE[0][2]
# for t in TYPE:
#     data_return.append(t[1])
# if len(TYPE) > 0:
#     if len(NCC) != 0:
#         expected = expected + '&' + NCC[0][2]
#         data_return.append(NCC[0][1])
#     if len(SORT) != 0:
#         expected = expected + '&' + SORT[0][2]
#         data_return.append(SORT[0][1])
# else:
#     if len(NCC) != 0:
#         expected = expected + NCC[0][2]
#         data_return.append(NCC[0][1])
#         if len(SORT) != 0:
#             expected = expected + '&' + SORT[0][2]
#             data_return.append(SORT[0][1])
#     else:
#         expected = expected + SORT[0][2]
#         data_return.append(SORT[0][1])

# while len(data_return) < 6:
#     data_return.append('-')
# print(expected)
# print(data_return)
