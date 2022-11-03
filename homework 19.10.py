# 1

'''
Дан список словарей, в каждом из словарей есть ключ name и position, он отвечает за расположение элемента в списке.
Position всегда должен быть последовательным, например у нас есть список
И мы хотим удалить элемент у которого position = 2
Придерживаясь такой логики, необходимо реализовать:
1. Удаление элемента
'''

import pprint

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
    {'name': 'Test 4', 'position': 4},
]


def del_position(list_A, position_num):
    list_A.pop(position_num - 1)
    for i, j in enumerate(list_A):
        j['position'] = i + 1
    return list_A


pprint.pprint(del_position(data, 2))
print()

# 2

'''
2. Добавление элемента с любым position,
например мы хотим в наш исходный список добавить элемент у которого position = 1
'''

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]


def add_position(list_A, position_num, position_arg):
    dict_A = {'name': f'{position_arg} {len(list_A) + 1}', 'position': None}
    list_A.insert(position_num - 1, dict_A)
    for i, j in enumerate(list_A):
        j['position'] = i + 1
    return list_A


pprint.pprint(add_position(data, 1, 'Test'))
print()

# 3

'''
Поменять элементы местами, например position 1 и position 3
'''

data = [
    {'name': 'Test 1', 'position': 1},
    {'name': 'Test 2', 'position': 2},
    {'name': 'Test 3', 'position': 3},
]


def change_position(list_A, position1, position2):
    list_A.insert(position1 - 1, list_A[position2 - 1])
    list_A.pop(position2)
    list_A.insert(position2, list_A[position1])
    list_A.pop(position1)
    for i, j in enumerate(list_A):
        j['position'] = i + 1
    return list_A


pprint.pprint(change_position(data, 1, 3))
print()


