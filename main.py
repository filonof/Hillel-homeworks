
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

'''

rows = 5
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0, k):
        print(end=" ")
    k = k - 2
    for j in range(0, i + 1):
        print("* ", end="")
    print("")
