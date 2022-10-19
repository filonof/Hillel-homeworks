# 1

list_of_numbers = []

for i in range(5):
    list_of_numbers.append(int(input(f'Enter digit №{i+1}: ')))

print(f'A = {list_of_numbers}')

# 2

list_A = []

for i in range(5):
    list_A.append(i + 1)

print(f'A = {list_A}')

list_A.pop()

print(f'A = {list_A}')

# 3

list_A = []

for i in range(10):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

N = int(input('Enter digit N: '))

print(list_A)

print(f'Number of repeated N in ist A: {list_A.count(N)}')

# 4

list_A = []

N = int(input('Enter list length (N): '))

for i in range(N):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

list_A.reverse()

print(list_A)

# 5

list_A = []
list_C = []

for i in range(5):
    list_A.append(int(input(f'Enter digit №{i+1}: ')))

for j in list_A:
    if j > 5:
        list_C.append(j)

print(list_A)
print(list_C)

# 6

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

# 7

text = input('Enter your sentence: ')

number_of_digits = sum(c.isdigit() for c in text)

print(number_of_digits)
