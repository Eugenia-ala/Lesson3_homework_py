
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [int(input()) for _ in range(int()))]
# sum = 0
# for i in range(1, len(list), 2):
#     sum += list[i]
# print(sum)


#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#Пример:
#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# list = [float("0." + str(i).split(".")[1]) for i in [1.1, 1.2, 3.1, 5, 10.01] if "." in str(i)]
# print(max(list) - min(list)


# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# n = int(input())
#
# str = ""
# while n > 0:
#     str = str(n % 2) + str
#     n //= 2
# print(str)


