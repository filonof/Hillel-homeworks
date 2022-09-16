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


