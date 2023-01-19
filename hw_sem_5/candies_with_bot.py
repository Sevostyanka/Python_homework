rules1 = 'За один ход можно брать не более 28 конфет'
print(rules1)
all_candies = int(input('Сколько конфет на столе?\n Впишите число: '))
max_candies = all_candies

from random import randint

name1 = 'Бот Игорь'
name2 = 'Марина'

while all_candies > 0:

    # игрок 1:
    
    if all_candies == max_candies: pl1 = all_candies%(28+1)
    else: pl1 = 28 + 1 - pl2

    print(f'{name1} взял {pl1} конфет.')
       
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
