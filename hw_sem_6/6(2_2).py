# Задайте список из n чисел последовательности (1 + 1/n)^n, выведите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

# НОВОЕ РЕШЕНИЕ:
number = int(input('Введите число: '))
f = lambda i: round(((1+1/i)**i), 2)
my_list = [f(i) for i in range(1, number+1)]
print(f'{number} => {my_list}\n{sum(my_list)}')

# ПРЕДЫДУЩЕЕ РЕШЕНИЕ:
# number = int(input('Введите число: '))
# my_list = []
# if number > 0:
#     for i in range(1, number+1):
#         my_list.append(round(((1+1/i)**i), 2))

# print(f'Для n = {number} ->', *my_list, sep=', ', end='')