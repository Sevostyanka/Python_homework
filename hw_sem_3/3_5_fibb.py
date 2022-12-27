# 5) Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

number = int(input('Введите длинну ряда: '))

def fibonacci(n):
    if n == 1 or n == 2: return 1
    return fibonacci(n-1) + fibonacci(n-2)

right_list = [0]
for i in range(1,number+1):
    right_list.append(fibonacci(i))

left_list = [0]
i = 1
while i <= number:
    if i%2 == 0:
        left_list.insert(0, right_list[i]*(-1))
    else:
        left_list.insert(0, right_list[i])
    i+=1

fib_list = left_list + right_list
fib_list.remove(0)
print(f'Для числа {number} список Негафибоначчи будет выглядеть так:  {fib_list}')