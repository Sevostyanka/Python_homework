# 2) Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list1 = [2, 3, 4, 5, 6]
my_list2 = [2,3,5,6]
my_list3 = [-1,-3,4,5,-1]


def sum_elements(my_list):
    i = 0
    new_list = []
    while i < len(my_list)/2:
        new_list.append(my_list[i] + my_list[-i-1])
        i+=1
    return new_list

print(f'{my_list1} => {sum_elements(my_list1)}')
print(f'{my_list2} => {sum_elements(my_list2)}')
print(f'{my_list3} => {sum_elements(my_list3)}')
