import model
import view



def input_handler(inp: int):
    match inp:
        case 1: #открыть файл и считать базу данных
            model.read_db()
            view. db_success(model.db_list)
        case 2: #показать все контакты
            view.show_all(model.db_list)
        case 3: 
            view.seach_in_db(model.db_list)
        case 4: 
            if len(model.db_list) != 0:
                model.rewrite_db_in_file()
                print('\nИзменения сохранены в базе.\n')
            else:
                print('База данных не подгружена, сохранить в файл невозможно.')
        case 5: 
            model.db_list.append(view.create_contact())
            print('Новый контакт сохранён')
        case 6: 
            view.change_contact(model.db_list)
        case 7: 
            view.delite_contact(model.db_list)
        case 8: 
            view.clear_db(model.db_list)
            view.exit_program()
            pass

def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)
