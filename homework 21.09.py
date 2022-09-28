# 1

str1 = '5 4 3 2 1'
for value in [str1]:
    print(value)
print()

# 2

for i in range(1, 11):
    print(f'3*{i}={3 * i}')
print()

# 3

# 4

for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i * j:4}', end=' ')
    print()
print()

# 5

symbol = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя01234567890123456789'
input1 = input("Введите строку: ")
shift = int(input('Введите сдвиг: '))
output = ''
for i in input1:
    char = symbol.find(i)
    new_symbol = char + shift
    if i in symbol:
        output += symbol[new_symbol]
    else:
        output += i
print(output)
print()
