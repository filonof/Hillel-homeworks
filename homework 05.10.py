# 1

'''
Задание #1:
Дано два множества A и B
В множестве А находятся имена должников за Сентябрь
В множестве B находятся имена должников за Октябрь
Найти:
* Вывести имена людей которые должны за Сентябрь и Октябрь
* Вывести должников за Октябрь у которых нет долга за Сентябрь
'''

A = {'Артем', 'Андрей', 'Александра', 'Пётр', 'Даниил', 'Вячеслав'}
B = {'Дмитрий', 'Анатолий', 'Владислав', 'Давид', 'Александра', 'Артем'}

print(A | B)
print(B - A)
print()

# 2

'''Задание #2:
Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt

Пример вывода:
Access denied
OK
OK
OK
OK
'''

n = int(input('Number of files: '))
action = {'write': 'W', 'read': 'R', 'execute': 'X'}
A = {}

for i in range(n):
    a, b = input('Enter file name and permission action: ').split()
    A[a] = b

m = int(input('Number of file requests: '))

for i in range(m):
    x, y = input('Enter file permission and file name: ').split()
    if action[x] in A[y]:
        print('OK')
    else:
        print('Access denied')

