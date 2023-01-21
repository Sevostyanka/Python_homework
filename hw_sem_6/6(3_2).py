# 2) Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list1 = [2, 3, 4, 5, 6]
my_list2 = [2,3,5,6]
my_list3 = [-1,-3,4,5,-1]

# НОВОЕ РЕШЕНИЕ:
def sum_elements(my_list):
    new_list = []
    s = lambda i: my_list[i] + my_list[-i-1]
    new_list = [s(i) for i in range(round((len(my_list)/2+0.5)))]
    return new_list
print(f'{my_list1} => {sum_elements(my_list1)}')
print(f'{my_list2} => {sum_elements(my_list2)}')
print(f'{my_list3} => {sum_elements(my_list3)}')

# ПРЕДЫДУЩЕЕ РЕШЕНИЕ:
# def sum_elements(my_list):
#     i = 0
#     new_list = []
#     while i < len(my_list)/2:
#         new_list.append(my_list[i] + my_list[-i-1])
#         i+=1
#     return new_list

# print(f'{my_list1} => {sum_elements(my_list1)}')
# print(f'{my_list2} => {sum_elements(my_list2)}')
# print(f'{my_list3} => {sum_elements(my_list3)}')