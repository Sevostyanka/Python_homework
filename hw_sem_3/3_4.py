# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

num = 45

def bin(a):
    my_list = [] 
    while a >= 1: 
        ost = a % 2
        my_list.append(ost)
        a = int(a/2)
    my_list.reverse()
    return my_list

bin_spisok = bin(num)
bin_spisok = list(map(str, bin_spisok))

bin_number = bin_spisok[0]
i = 1
while i < len(bin_spisok):
    bin_number +=bin_spisok[i]
    i+=1
print(f'{num} -> {bin_number}')
