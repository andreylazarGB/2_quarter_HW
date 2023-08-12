# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# Ввод:
# 3 4 2 5 7
# [4,6]
# Вывод:
# 1, 3
import random
l = int(input('Введите длину массива: '))
n = int(input('Введите min значение диапазона: '))
m = int(input(f'Введите max значение диапазона, больше {n}: '))

# array = []
# for i in range(l):
#     i = random.randint(1, 10)
#     array.append(i)
array = [random.randint(1, 10) for i in range(l)]
print(array)

print(f'Индексы элементов массива, значения которых лежат в диапозоне от {n} до {m}: {[i for i in range(len(array)) if array[i] >= n and array[i] <= m]}')