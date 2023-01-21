# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным 
# и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# НОВОЕ РЕШЕНИЕ:
from decimal import Decimal
from decimal import getcontext

my_list = [1.1, 1.2, 3.1, 5, 10.01]
my_list = list(map(lambda item: Decimal(item) - Decimal(int(item)), my_list))

minn = 1
for item in my_list:
    if minn > item and item != 0:
        minn = item
        
diff = round((max(my_list) - minn), 2)
print(diff)


# ПРЕДЫДУЩЕЕ РЕШЕНИЕ:
# from decimal import Decimal
# from decimal import getcontext

# my_list = [1.1, 1.2, 3.1, 5, 10.01]

# remains = []
# getcontext().prec = 2
# for item in my_list:
#     remains.append(Decimal(item) - Decimal(int(item)))
# print(remains)

# maxx = max(remains)
# minn = 1

# for item in remains:
#     if minn > item and item != 0:
#         minn = item

# difference = maxx - minn

# print(f'{my_list} -> {difference}')


