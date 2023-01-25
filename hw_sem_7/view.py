def main_menu() -> int:
    print('Главное меню:')
    menu_list = ['Открыть файл',
    'Показать все контакты+',
    'Найти контакт+',
    'Сохранить изменения в файл+',
    'Создать контакт+',
    'Изменить контакт',
    'Удалить контакт+',
    'Выход+']
    for i in range(len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')
    print()
    
    user_input = int(input('Введите команду:> '))
    print()
    # TODO: сделать валидацию (проверку на дурака)
    return user_input

def show_all(db: list):
    print(db)
    if db_success(db):
        for i in range(len(db)):
            user_id = i+1
            print(user_id, end=". ")
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()
    print()

def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        print()
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        print()
        return False

def exit_program():
    print('Завершение программы.')
    print()
    exit

def create_contact():
    print('Создание нового контакта:')
    new_contact = dict()
    new_contact['lastname'] = input('   Введите фамилию: ')
    new_contact['firstname'] = input('   Введите имя: ') 
    new_contact['phone'] = input('   Введите телефон: ')
    new_contact['comment'] = input('   Введите комментарий: ')

    return new_contact

def seach_in_db(db: list):
    inp = input("Введите данные для поиска: ")
    count = 0
    for i in range(len(db)):
        if inp in db[i].values():
            for k, v in db[i].items():
                count +=1
                print(f'{k}: {v}')  
    print()            
             
    if count == 0:
        print("\nТакого контакта нет в базе\n")
        
def delite_contact(db: list):
    inp = input('Впишите данные контакта, который нужно удалить\n(имя или фамилия или телефон): ')
    ind = 0
    check = 0
    for i in range(len(db)):
        if inp in db[i].values():
            check +=1
            ind = i

    if check == 0:
        print('\nТаких данных нет в базе\n') 
    else:
        db.pop(ind)
        print("\nКонтакт удалён.\n")

def change_contact(db: list):
    int1 = input('\nКакой контакт нужно изменить?\n(впишите фамилию или имя или телефон для поиска): ')
    index_contact = 0
    check = 0
    for i in range(len(db)):
        for k,v in db[i].items():
            if int1 in db[i].values():
                index_contact = i
                check += 1
                print(f'- {k}')
    if check == 0: print('\nТакого контакта нет.\n')    
       
    for i in range(4):
        inp2 = input('\nКакую позицию редактируете?\nl(фамилия), f(имя), p(номер), c(коментарий), q(выход)\n Впишите букву: ') 
        match inp2:
            case 'l':
                try:
                    inp3 = input('Введите новую фамилию: ')
                    db[index_contact]['lastname'] = inp3
                    print('\nФамилия изменена.\nНе забудьте сохранить изменения в файл.\n')
                except Exception:
                    print('Попробуйте еще раз')
            case 'f':
                try:
                    inp3 = input('Введите новое имя: ')
                    db[index_contact]['firstname'] = inp3
                    print('\nИмя изменено.\nНе забудьте сохранить изменения в файл.\n')
                except Exception:
                    print('Попробуйте еще раз')
            case 'p':
                try:
                    inp3 = input('Введите новый телефон: ')
                    db[index_contact]['phone'] = inp3
                    print('\nНомер телефона изменён.\nНе забудьте сохранить изменения в файл.\n')
                except Exception:
                    print('Попробуйте еще раз')
            case 'c':
                try:
                    inp3 = input('Введите новую фамилию: ')
                    db[index_contact]['lastname'] = inp3
                    print('\nКоментарий изменён.\nНе забудьте сохранить изменения в файл.\n')
                except Exception:
                    print('Попробуйте еще раз')
            case 'q':
                try:
                    print("\nИзменения завершены. Выход.\n")
                    break
                except Exception:
                    print('Попробуйте еще раз')

def clear_db(db: list):
    db = db.clear()
    print('База данных очищена')