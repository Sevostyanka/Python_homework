# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.



# 1) вычленяем многочлены из файлов:
mnog1 = open("mnog1.txt", 'r')
mnogoch1 = ''
for i in mnog1:
    mnogoch1 +=i
mnog1.close()

mnog2 = open("mnog2.txt", "r")
mnogoch2 = ""
for i in mnog2:
    mnogoch2 +=i
mnog2.close
    
print(mnogoch1)
print(mnogoch2)

# 2) создаём списки с коэфициентами многочленов:
def koef(a: str):
    frase = a.replace(' ','').replace('=0','').replace('+', ' ').replace('-', ' -')
    frase = frase.split()
    new_list = []
    for i in frase:
        if i.startswith('x'):
            new_list.append(1)
        elif i.startswith('-x'):
            new_list.append(-1)
        else:
            new_list.append(i.split('*x')[0])

    return new_list
koef1 = koef(mnogoch1)
koef2 = koef(mnogoch2)

# print(koef1)
# print(koef2)

# 3) делаем значения цифровыми:
koef1 = list(map(int, koef1))
koef2 = list(map(int, koef2))
# print(koef1)
# print(koef2)

# 4) создаём словарики с коэфициентами:
def dict_koef(koef):
    turn_koef = []
    i = 1
    while i <= len(koef):
        turn_koef.append(koef[-i])
        i+=1

    dict_koef = {i: turn_koef[i] for i in range(len(turn_koef))}

    return dict_koef

dict_koef1 = dict_koef(koef1)
dict_koef2 = dict_koef(koef2)

# print(dict_koef1)
# print(dict_koef2)

# 5) создаём словарик с суммами коэфициентов:
def dict_summa_koef(dict1, dict2):
    summa_dict = {}
    i = 0
    while i < len(koef2):
        if dict2.get(i) == None:
            summa_dict[i] = dict1.get(i)
        elif dict1.get(i) == None:
            summa_dict[i]= dict2.get(i)
        else:
            summa_dict[i] = (dict1.get(i) + dict2.get(i))
        i+=1
    return summa_dict

summa_koef_dic = dict_summa_koef(dict_koef1, dict_koef2)

# print(summa_koef_dic)

# 6) создаём новый многочлен на основе коэфициентов:

# 6.1) конвертируем словарик в список:
summa_koef_list = list(summa_koef_dic.values())

# 6.2) составляем строку с многочленом:
def new_mnog(koef):
    new_mnog = ""
    i = len(koef)
    while i > 0:
        if i == 1:
            if koef[i-1] > 0:
               new_mnog = new_mnog + '+' + str(koef[i-1]) + ' = 0' 
            else:
                new_mnog = new_mnog + str(koef[i-1]) + ' = 0'
        elif i == 2:
            if koef[i-1] > 0:
                new_mnog = new_mnog + '+' + str(koef[i-1])+'*x**'+ str(i-1) + ' '
            else:
                new_mnog = new_mnog + str(koef[i-1])+'*x**'+ str(i-1) + ' '
        else:
            if i == len(koef):
                new_mnog = new_mnog + str(koef[i-1])+'*x**' + str(i-1) + ' '
            elif i != len(koef) and koef[i-1] > 0:
                new_mnog = new_mnog + '+' + str(koef[i-1])+'*x**' + str(i-1) + ' '
            else:
                new_mnog = new_mnog + str(koef[i-1])+'*x**' + str(i-1) + ' '
           

        i-=1
    return new_mnog

print(new_mnog(summa_koef_list))