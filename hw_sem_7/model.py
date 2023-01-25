db_list = []
path = '/Users/Mikki/Desktop/1 Quater/HomeWork/hw_sem_7/database.txt'
def read_db() -> list:
    global db_list
    global path
    if len(db_list) == 0:
        with open (path, 'r', encoding='UTF-8') as file:
            my_list = file.readlines()
            for line in my_list:
                id_dict = dict()
                line = line.strip().split(';')
                id_dict['lastname'] = line[0]
                id_dict['firstname'] = line[1]
                id_dict['phone'] = line[2]
                id_dict['comment'] = line[3]
                db_list.append(id_dict)
    
    
def rewrite_db_in_file():
    global db_list
    global path
    my_list = []
    # создаю список из значений словарей с разделителем \n
    for i in range(len(db_list)):
        for v in db_list[i].values():
            my_list.append(f'{v};')
        my_list.append('\n')
    # перевожу всё в строку, чтоб writelines смог добавить в файл
    my_str = ''
    for i in range(len(my_list)):
        my_str += str(my_list[i])
    
    with open (path, 'w', encoding='UTF-8') as file:
        file.writelines(my_str)
    