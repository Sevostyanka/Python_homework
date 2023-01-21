# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов 
# списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# НОВОЕ РЕШЕНИЕ:
my_list1 = [2,3,5,9,3]
my_list = [my_list1[i] for i in range(len(my_list1)) if i%2 != 0]
sum = sum(my_list)
print(f'{my_list1} => чётных позициях элементы {my_list}. Их сумма равна {sum}')

# ПРЕДЫДУЩЕЕ РЕШЕНИЕ:
# my_list = [2,3,5,9,3]

# sum = 0
# i = 1
# while i < len(my_list):
#     sum += my_list[i]
#     i += 2

# odd_list = []
# k = 1
# while k <= len(my_list)-1:
#     odd_list.append(str(my_list[k]))
#     k+=2
# print(odd_list)
# print(f'{my_list} -> на нечётных позициях элементы {odd_list}, ответ: {sum}')