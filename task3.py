#3 Задайте последовательность чисел. Напишите программу, которая
# выведет список неповторяющихся элементов исходной 
# последовательности.
list_num = input('Введите числа через пробел ->  ').split()
print(list_num)
list_new = []
for i in list_num:
    if i not in list_new:
        list_new.append(i)
print(list_new)