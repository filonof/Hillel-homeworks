# 1
N = int(input('Введите ширину треугольника: '))
i = 1
while i <= N:
    j = N
    while j >= i:
        print('*', end='')
        j -= 1
    print()
    i += 1
# 2
N = int(input('Введите ширину треугольника: '))
i = 1
while i <= N:
    j = 1
    while j <= i:
        print('*', end='')
        j += 1
    print()
    i += 1
# 3
N = int(input('Введите ширину треугольника: '))
i = N
while i >= 1:
    j = N
    while j > i:
        print(' ', end='')
        j -= 1
    k = 1
    while k <= i:
        print('*', end='')
        k += 1
    print()
    i -= 1

