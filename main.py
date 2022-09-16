a = int(input('Введите число №1: '))
b = int(input('Введите число №2: '))
c = int(input('Введите число №3: '))

if a > b > c:
    print(f'max = {a}')
    if b > a > c:
        print(f'max = {b}')
        if c > a > b:
            print(f'max = {c}')

