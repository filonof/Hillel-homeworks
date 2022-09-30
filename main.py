"""
1) Пользователя вводит два числа A и B, нужно вывести сумму чисел в диапазоне от A до B.
2) Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.
3) Пользователь вводит два числа A и B, нужно вывести прямоугольник со сторонами A и B с помощью символа '*' используя цикл.
В коде можно использовать символ '*' только один раз.
4) Запросить у пользователя число N, вывести треугольник шириной N используя символ '*'.
Input:
N = 6
Output:
******
*****
****
***
**
*
"""
'''
A = int(input('Введите число А: '))
B = int(input('Введите число B: '))
while A < B:
    print(A)
    A += 1
    for n in range(A, B):
        n = A + B

print(f'Сумма: {n}')

print('* ' * (2 * 4 - 1))
for i in range(1, 4):
    print(' ' * i, end='')
    print('* ' * (4 - i), end='')
    print('  ' * (i - 1), end='')
    print('* ' * (4 - i))
    
N = int(input('Введите ширину треугольника: '))
i = 1
while i <= N:
    j = N
    while j >= i:
        print('*', end='')
        j -= 1
    print()
    i += 1


rows = 5
for i in range(0, rows):
    # nested loop for each column
    for j in range(0, i + 1):
        # print star
        print("*", end=' ')
    # new line after each row
    print("\r")

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")


A = int(input('Введите число А: '))
B = int(input('Введите число B: '))
summ = 0

while A < B:
    summ += A
    A += 1
print(summ)

for i in range(A, B):
    summ += i
print(summ)

s1 = int(input('Type a number from 1 to 10: '))
for i in range(1, 11):
    print(f'{s1}*{i}={s1 * i}')
    
s1 = 3
for i in range(1, 11):
    s2 = s1 * i
    print(f'3*{i}={s2}')
    
for i in range(1, 11):
    for j in range(1, 11):
        s1 = i, i * j
        print(s1)
exit()
n = int(input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(i * j, " " * (5 - len(str(i * j))), end=" ")
    print("\n", end="")
    
for i in range(1, 11):
    print(f'{i}: ')
    for j in range(1, 11):
        print(f'{i} * {j} = {i * j}')
exit()

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j:2}', end=' ')
    print()
exit()

symbol = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя01234567890123456789'
input1 = input("Введите строку: ")
sdvig = int(input('Введите сдвиг: '))
output = ''
for i in input1:
    char = symbol.find(i)
    new_symbol = char + sdvig
    if i in symbol:
        output += symbol[new_symbol]
    else:
        output += i
print(output)
print()


import random

number = random.randint(1, 10)
n = int(input('Введите число: '))
for number in range(1, 11):
    if number > n:
        print('Бери меньше')
    if number < n:
        print('Бери больше')
    else:
        print('Ты угадал')
'''

#  ЗАДАНИЕ 0
"""
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
1. isspace
2. islower
3. isupper
4. isdigit
test_string = 'Hello world123'
for symbol in test_string:
    print(symbol)
    print(symbol.isspace())
    print(symbol.islower())
    print(symbol.isupper())
    print(symbol.isdigit())
    print('======================')
"""

'''test_string = 'Hello% world123'

for symbol in test_string:
    if symbol.isspace() or symbol.islower() or symbol.isupper() or symbol.isdigit():
        print('YES')
    else:
        print('NO')'''

'''
1. Напишите программу где пользователь вводит число symbol_len, а программа генерирует пароль длинной symbol_len.
Чем выше будет сложность пароля, тем лучше.
2. Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат
в оценочной шкале от 1 до 5.
3. Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.

count = int(input('Введите число: '))
f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < count:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    i += 1
print()
'''
# 1
'''import random

ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'
punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

all = ascii_lowercase + ascii_uppercase + digits + punctuation
k = 5
symbols = random.choices(ascii_lowercase, k)  # Сгенерировали 5 рандомных символов из букв ascii_lowercase
done_str = ''.join(symbols)(all,k)
print(done_str)
chr = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя01234567890123456789'
'''
# 4

'''import random

number = random.randint(1, 10)
n = int(input('Введи число: '))
while n != number:
    if n < number:
        print("Бери больше")
    elif n > number:
        print("Бери меньше")
    n = int(input("Повтори попытку:"))
print("Ты угадал!")'''


'''
while K!=N:
    if K<N:
        print("Ваше число меньше, чем задумал компьютер")
    elif K>N:
        print("Ваше число больше, чем задумал компьютер")
    K=int(input("Повторите попытку:")
print("Вы угадали")

while n != number:
    n = int(input('Try more: '))
    if n > number:
        print('Try less')
    elif n < number:
        print('Try more')
    else:
        print('You\'ve guessed correct')
exit()

from random import randint
N=randint(1,10)
K=int(input("Угадайте целое число от 1 до 10:"))
while K!=N:
    K=int(input("Повторите попытку:"))
    if K<N:
        print("Ваше число меньше, чем задумал компьютер")
    elif K>N:
        print("Ваше число больше, чем задумал компьютер")
    else:
        print("Вы угадали")
print(K)
print(N)'''

import random

guesses = 1
number = random.randint(1, 10)

while guesses < 4:
    guess = int(input(f'Попытка #{guesses}: '))
    guesses += 1
    if guess < number:
        print('Бери больше')
    if guess > number:
        print('Бери меньше')
    if guess == number:
        break

if guess == number:
    print('Ты угадал!')
else:
    print('Ты не угадал')
