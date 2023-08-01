# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите колличество элементов 1-ого множества: '))
list_1 = list()
for i in range(n):
    q = int(input(f'Введите {i} элемент 1-ого множества: '))
    list_1.append(q)

m = int(input('Введите колличество элементов 2-ого множества: '))
list_2 = list() 
for i in range(m):
    w = int(input(f'Введите {i} элемент 2-ого множества: '))
    list_2.append(w)

one = set(list_1).intersection(set(list_2))  
print(f'Пересечение элементов множеств: {sorted(one)}')
