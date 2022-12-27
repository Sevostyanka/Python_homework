# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
li = [0,1]

for x in li:
    for y in li:
        for z in li:
            print(f'x = {x}; y = {y}; z = {z}; -> {(not (x or y or z)) == (not x and not y and not z)}')
