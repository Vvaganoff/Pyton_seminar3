# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# a = set(input())
# if len(a) == 1:
#     print(1)
# else:
#     print(len(a))

# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# list_1 = [5, 4, 6, 7, 8, -10]
# k = 3
#
# list_result = list()
# for i in range(k):
#     list_result.append(list_1[len(list_1) - 1 - i])
#     print(list_result)
# print(1)
# for i in range(len(list_1) - k):
#     list_result.append(list_1[i])
#     print(list_result)
# print(list_result)

#Напишите программу для печати всех уникальных значений в словаре.  \
# list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
# set_result = set()
# for i in list_1:
#     for j in i:
#         set_result.add(i[j])
# print(set_result)

# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.
