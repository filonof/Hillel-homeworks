# 1
a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
c = int(input('Введите число №3: '))

if a >= 10 and a % 3 == 0 and b >= 10 and b % 3 == 0 and c >= 10:
    print('yes')
else:
    print('no')

# 2
a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
c = int(input('Введите число №3: '))
max = max(a, b, c)
print(f'max = {max}')

# *
number = int(input('Введите трехзначное число: '))
reversed_number = 0


def rev(number):
    global reversed_number
    if number > 0:
        a = number % 10
        reversed_number = (reversed_number * 10) + a
        rev(number // 10)
    return reversed_number


reversed_number = rev(number)
print(f'Реверс числа = {reversed_number}')
