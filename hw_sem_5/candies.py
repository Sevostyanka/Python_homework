'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход.
a) Добавьте игру против бота
b) Подумайте как наделить бота 'интеллектом'
'''
rules1 = 'За один ход можно брать не более 28 конфет'
print(rules1)
all_candies = int(input('Сколько конфет на столе?\n Впишите число: '))

from random import randint
names = {1: 'Игорь', 2: 'Марина'}

name1 = names.get(randint(1,2))
if name1 == names.get(1): name2 = names.get(2)
else: name2 = names.get(1)
print(f'Первым(ой) ходит {name1}.')

while all_candies > 0:
    # игрок 1:
    pl1 = int(input(f'{name1}, ваш ход: '))
   
    if pl1 <= 0 or pl1 > 28:
        print("ВНИМАНИЕ! Можно взять от 1 до 28 конфет.")
        pl1 = int(input(f'{name1}, ваш ход: '))
    

    all_candies = all_candies - pl1

    if all_candies <= 0:
        print(f'Осталось 0 конфет.\n {name1} выиграл(а)! Поздравляем!!!')
        break
    else:
        print(f'Осталось {all_candies} конфет.')

    
    # игрок 2:
    pl2 = int(input(f'{name2}, ваш ход: '))

    if pl2 <= 0 or pl2 > 28:
        print("ВНИМАНИЕ! Можно взять от 1 до 28 конфет.")
        pl2 = int(input(f'{name2}, ваш ход: '))

    
    all_candies = all_candies - pl2
    if all_candies <= 0:
        print(f'Осталось 0 конфет.\n {name2} выиграл(а)! Поздравляем!!!')
        break
    else:
        print(f'Осталось {all_candies} конфет.')


