from random import randint

# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
# одной и той же стороной. Выведите минимальное количество монет,которые нужно перевернуть.

print ('введите колличество монет: ')
n = int(input())

gerb = 0
tails = 1
count_gerb = 0
k = 1

# for i in range(n):
#     weigth = randint(0, 1)
#     print(weigth)
#     if gerb == weigth:
#         count_gerb += 1

while k <= n:
    coin = int(input(f'Введите сторону монеты: '))
    if gerb == coin:
       count_gerb += 1
    k += 1

if count_gerb > n//2:
    res = n - count_gerb
    print(f'Минимальное количество монет,которые нужно перевернуть: {res}')
else:
    res = count_gerb
    print(f'Минимальное количество монет,которые нужно перевернуть: {res}')




