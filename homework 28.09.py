'''
Задание 1:
Запросить у пользователя 5 чисел и записать их в список
'''
list_of_numbers = []

for i in range(5):
    list_of_numbers.append(int(input(f'Enter digit №{i+1}: ')))

print(f'A = {list_of_numbers}')
'''
Задание 2:
Дан список A = [1, 2, 3, 4, 5]
Удалить последнее число из списка
'''
list_A = []

for i in range(5):
    list_A.append(i + 1)

list_A.remove(5)

print(f'A = {list_A}')
'''
Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
'''
list_A = []

for i in range(10):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

N = int(input('Enter digit N: '))
print(list_A)
print(f'Number of repeated N in ist A: {list_A.count(N)}')

'''
Задание 4:
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
'''
list_A = []
N = int(input('Enter list length (N): '))

for i in range(N):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

list_A.reverse()
print(list_A)
'''
Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
'''
list_A = []
list_C = []

for i in range(5):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

for j in list_A:
    if j > 5:
        list_C.append(j)

print(list_A)
print(list_C)
'''
Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.
'''
list_A = []
N = int(input('Enter list length (N): '))

for i in range(N):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

mindigit = list_A[0]
maxdigit = list_A[0]
for j in range(len(list_A)):
    if maxdigit < list_A[j]:
        maxdigit = list_A[j]
for k in range(len(list_A)):
    if mindigit > list_A[k]:
        mindigit = list_A[k]
print(maxdigit, mindigit)

'''
Задание 7:
Пользователь вводит текст нужно вывести количество цифр в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество цифр: 7
'''

text = input('Enter your sentence: ')
number_of_digits = sum(c.isdigit() for c in text)
print(number_of_digits)
