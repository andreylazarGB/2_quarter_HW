# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

# list_1 = [1, 3, 2, 8, 4]
# k = 2

# Вариант 1
# list_1.insert(0, k)
# list_1.sort()
# print(list_1)

# i = 0      
# while i < len(list_1)-1:
#     if list_1[len(list_1)-1] == k:
#         print(list_1[len(list_1)-2])
#         break
#     elif list_1[0] == k:
#         print(list_1[1])
#         break
#     if list_1[i] == k:
#         if k - list_1[i-1] < list_1[i+1] - k:
#             print(list_1[i-1])
#             break
#         else:
#             print(list_1[i+1])
#             break
#     i += 1


# Вариант 2

list_1 = [1, 3, 2, 8, 4]
list_1.sort()
print(list_1)
k = 10

min = abs(k - list_1[0])

for i in range(len(list_1)):
    if abs(k - list_1[i]) < min:
        min = abs(k - list_1[i])
        nearest = list_1[i]
print(nearest)
print(min)


