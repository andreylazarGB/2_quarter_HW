# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

from random import randint

# # n = print(int(input('Введите длину массива -> ')))
# print('Введите длину массива -> ')
# n = int(input())
# lst = []
# for i in range(n):
#     lst = randint(2, 3)
# print(lst)  

list_1 = [1, 3, 3, 3, 3]
k = 3
count = 0
n = 1
i = 0
while n <= len(list_1):
    if list_1[i] == k:
        count += 1
    i += 1
    n += 1 
print(count)