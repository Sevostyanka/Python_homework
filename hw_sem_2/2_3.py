# Реализуйте алгоритм перемешивания списка. 
# НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, максимум использование 
# библиотеки Random для и получения случайного int

from random import randint

my_list = ['blue', 'green', 'yellow', 'purple', 'pink']
new_list =[]
old_randoms = []
i = 0
while i < len(my_list):
    rand = randint(0, len(my_list)-1)
    if rand in old_randoms:
        continue
    else:
        new_list.append(my_list[rand])
        i +=1
        old_randoms.append(rand)

print(new_list)