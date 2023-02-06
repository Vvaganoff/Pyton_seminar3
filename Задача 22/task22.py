# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input("Введите количество элементов в массиве: "))
array_str = input("Введите массив: ")
x = int(input("Введите искомое число: "))
list_str = array_str.split()
print(list_str)
list_int = list()
count = 0
for num in list_str:
    num_int = int(num)
    list_int.append(num_int)
    if x == num_int:
        count = count + 1
print(list_int)
print(f"Число {x} встречается в массиве {count} раз.")
