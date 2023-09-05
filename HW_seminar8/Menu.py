import Methods
book = 'Homework\HW_seminar8\phones.txt'

def open_phone_book_menu():
    selected_operation = ''
    while selected_operation != 6:
        selected_operation =int(input('\n Введите желаемую операцию:\n'
          '1 - вывести все контакты на экран;\n'
          '2 - добавить новый контакт\n'
          '3 - изменить существующий контакт\n'
          '4 - удалить контакт\n'
          '5 - найти контакт\n'
          '6 - закончить работу со справочником\n'
          'ваш выбор - '))
        if selected_operation == 1: Methods.print_all_phone_book(book)
        if selected_operation == 2: Methods.add_new_contact(book)
        if selected_operation == 3: Methods.edit_contact(book)
        if selected_operation == 4: Methods.remove_contakt(book)
        if selected_operation == 5: Methods.find_contact(book)