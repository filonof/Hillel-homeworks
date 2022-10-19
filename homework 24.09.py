# 1

test_string = 'Hello% world123'
for symbol in test_string:
    if symbol.isspace() or symbol.islower() or symbol.isupper() or symbol.isdigit():
        print('YES')
    else:
        print('NO')
print()

# 2

count = int(input('Введите число: '))
f1 = f2 = 1
print(f1, f2, end=' ')
i = 2
while i < count:
    f1, f2 = f2, f1+f2
    print(f2, end=' ')
    i += 1
print()

# 3

password = input('Enter your password: ')


# 4



