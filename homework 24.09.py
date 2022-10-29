# 1
'''
Написать программу которая проверяет что в строке есть хотя бы один пробел, число, буква нижнего и верхнего регистра.
Если это так, то вывести 'YES', иначе 'NO'
'''

test_string = input('Enter a string: ')

space = False
lower = False
upper = False
digit = False

for symbol in test_string:
    if symbol.isspace():
        space = True
    elif symbol.islower():
        lower = True
    elif symbol.isupper():
        upper = True
    elif symbol.isdigit():
        digit = True

summary = space + lower + upper + digit

if summary == 4:
    print('YES')
else:
    print('NO')
print()

# 2
'''
Напишите программу где пользователь вводит число - count, а программа выводит count чисел фибоначчи.
'''
count = int(input('Введите число: '))
f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < count:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    i += 1
print()

# 3
'''
Напишите программу где пользователь вводит пароль, а программа проверяет сложность пароля и выводит свой результат в оценочной шкале от 1 до 5.
1 - у пользователя пароль == 'qwerty' or 'admin' или пароль пустой
2 - у пользователя только цифры или спец. символы или все буквы в верхнем или нижнем регистре
3 - у пользователя в пароле соблюдается два условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
4 - у пользователя в пароле соблюдается три условия из (цифры, буква нижнего регистра, буква верхнего регистра, спец. символы)
5 - у пользователя есть цифры, буквы нижнего и верхнего регистра, спец. символы и длинна пароля больше 8 символов
'''

password = input('Enter your password: ')

space = False
lower = False
upper = False
digit = False

if not password or password == 'qwerty' or password == 'admin':
    print('level 1')
    exit()

for char in password:
    if char.isspace():
        space = True
    elif char.islower():
        lower = True
    elif char.isupper():
        upper = True
    elif char.isdigit():
        digit = True

pass_len = len(password) > 8
summary = space + lower + upper + digit

if summary == 1:
    print('level 2')
elif summary == 2:
    print('level 3')
elif summary >= 3 and not pass_len:
    print('level 4')
elif summary == 4 and pass_len:
    print('level 5')

# *

'''
Напишите программу где пользователь вводит число symbol_len,
а программа генерирует пароль длинной symbol_len. Чем выше будет сложность пароля, тем лучше.
Сложность пароля буду оценивать по шкале от 1 до 5 из задании #3
'''

import string
import random

password_len = int(input('Enter password length: '))
password = ''
char_count = password_len // 4
rest_char = password_len % 4
symbols_all = string.ascii_letters + string.digits + string.punctuation
consistent_password = ''

for symbols in string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation:
    if char_count > len(symbols):
        consistent_password += ''.join(random.choices(symbols, k=char_count))
    else:
        consistent_password += ''.join(random.sample(symbols, k=char_count))

consistent_password += ''.join(random.choices(symbols_all, k=rest_char))

for _ in range(password_len):
    random_char = random.sample(consistent_password, k=1)[0]
    password += random_char
    consistent_password = consistent_password.replace(random_char, '', 1)

print(f'Your password: {password}')
