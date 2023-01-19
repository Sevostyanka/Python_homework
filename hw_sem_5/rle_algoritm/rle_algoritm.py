'''
Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
Входные и выходные данные хранятся в отдельных текстовых файлах.
aaaaabbbcccc -> 5a3b4c
5a3b4c -> aaaaabbbcccc
'''
# c = '5a3b4c'
# d = 'aaaaaaaabbbbbcccg'

data = open('file_1.txt', 'r')
c = data.read()
data.close()

data = open('file_2.txt', 'r')
d = data.read()
data.close()

# Ф-ЦИЯ АРХИВАЦИИ ТЕКСТА:
def make_arch(a):
    spis_a = list(a) #приводим строку к списку элементов
    # print(spis_a)

    unic_list = [] #создаём список уникальных элементов
    for i in spis_a:
        if i not in unic_list:
            unic_list += i

    zip_spis = [] #формируем заархивированный список
    for item in unic_list:
        zip_spis.append(str(spis_a.count(item)) + item)
        
    zip_spis = ''.join(zip_spis)
    return zip_spis

# Ф-ЦИЯ РАЗОРХИВАЦИИ ТЕКСТА:
def out_of_arch(b):
    spis_b = list(b) #приводим строку к списку элементов
    
    new_b = []
    for i in range(len(spis_b)):
        if i%2 == 0:
            for j in range(int(spis_b[i])):
                new_b.append(spis_b[i+1])
    new_b = ''.join(new_b)
    return new_b

# Ф-ЦИЯ АРХИВАТОРА:
def arch(text):
    if text[0].isdigit(): 
        return out_of_arch(text)
    else:
        return make_arch(text)
    
print(f'{c} => {arch(c)}')
print(f'{d} => {arch(d)}')