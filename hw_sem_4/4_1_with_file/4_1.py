# Задана натуральная степень k. Сформировать случайным образом список 
# коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
k = randint(1,15)
print(f'Степень многочлена: {k} \nЗагляни в файл "file_4_1.txt"')

mnogoch = ""
i = 0
while i < k:
    rand = randint(1,100)
    if i != k-1:
        if rand > 0:
            mnogoch += str(rand)
            mnogoch += "*x**"
            mnogoch += str(k-i)
            mnogoch += " + "
        elif rand ==1:
            mnogoch += str(rand)
            mnogoch += "*x**"
            mnogoch += str(k-i)
            mnogoch += " - "
    elif i == k-1:
        mnogoch += str(rand)
        mnogoch += "*x + "
    i+=1
rand1 = randint(1,100)
mnogoch += str(rand1) + " = 0"


file_with_mnogochlen = open("C:/Users/Mikki/Desktop/1 Quater/HomeWork/hw_sem_4/4_1_with_file/file_4_1.txt", 'w')
file_with_mnogochlen.writelines(mnogoch)
file_with_mnogochlen.close()

