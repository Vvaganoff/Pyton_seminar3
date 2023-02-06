# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5

n = int(input("Введите количество элементов в массиве: "))
array_str = input("Введите массив: ")
x = int(input("Введите искомое число: "))
list_str = array_str.split()

list_int = list()
count = 0
dic = {}
for num in list_str:
    num_int = int(num)
    list_int.append(num_int)
    if x == num_int:
        print(f"Самое близкое к числу {x}  - число {x}.")
        count = 1
    else:
        dic[num_int] = abs(x-num_int)
if count != 1:
    min_value = x
    res_num = 0
    for key, value in dic.items():
        if value < min_value:
            min_value = value
            res_num = key
    print(f"Самое близкое к числу {x}  - число {res_num}.")


