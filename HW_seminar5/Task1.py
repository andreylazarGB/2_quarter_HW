# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.

# Функция не должна ничего выводить, только возвращать значение.

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 

# def degree (a, b):
#     for i in range(b+1):
#         num = a**i
#     return num

# print(degree(a, b))


# def power(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         res = (a * power(a, b - 1))  # 2 * 
#         print(res)
#         return res
    
# a = int(input("Введите число: "))
# b = int(input("Введите его степень: "))
# print("Результат возведения в степень равен:", power(a, b))

def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a

print(f(2, 4))