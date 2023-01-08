# НАПИСАТЬ СВОЙ РАНДОМАЙЗЕР (НЕ ИСПОЛЬЗОВАТЬ БИБЛИОТЕКУ RANDOM)

# делаем рандом 3х-значного числа:

def my_random():
    import time
    a = int(10000000 * time.perf_counter() % 1000)
    return a

number = my_random()
print(number)