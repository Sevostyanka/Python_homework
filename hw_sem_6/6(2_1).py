# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0.56 -> 11

# НОВОЕ РЕШЕНИЕ:
my_list = list(input('Введите вещественное число: '))
my_list.remove('.')
my_list = list(map(int, my_list))
sum = 0
for i in my_list:
    sum +=i

print(sum)

# ПРЕДЫДУЩЕЕ РЕШЕНИЕ:
# number = input("Введите число: ")
# my_list = list(number)

# my_list.remove('.')
# print(my_list)

# def dig(a):
#     return int(a)

# d_list = []
# for i in my_list:
#     d_list.append(dig(i))

# sum = 0
# for i in d_list:
#     sum +=i

# print(f'{number} -> {sum}')