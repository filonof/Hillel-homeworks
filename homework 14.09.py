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

if not 100 <= number <= 999:
    print('Ошибка. Попробуйте другое число')
    exit()

first_num = number % 10
second_num = number % 100 // 10
third_num = number // 100

final_num = first_num * 100 + second_num * 10 + third_num

print(final_num)
exit()
