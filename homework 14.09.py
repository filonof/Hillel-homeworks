#1
a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
c = int(input('Введите число №3: '))

if a >= 10 and a % 3 == 0:
    if b >= 10 and b % 3 == 0:
        if c >= 10:
            print('yes')
        else:
            print('no')
    else:
        print('no')
else:
    print('no')

#2
a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
c = int(input('Введите число №3: '))
max = max(a, b, c)
print(f'max = {max}')

#*(честно подсмотрел)
number = int(input('Введите трехзначное число: '))
reversed_number = 0

while number > 0:
    num = number % 10
    number = number // 10
    reversed_number = reversed_number * 10
    reversed_number = reversed_number + num

print(reversed_number)
exit()
