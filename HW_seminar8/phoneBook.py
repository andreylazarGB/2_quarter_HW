# написать телефонный справочник Имя Фамилия; телефон; комментарий
# 0. открыть справочнок
# def open_phone_book_menu(file_name)
# 1. вывести все записи на экран
# def print_all_phone_book(file_name)
# 2. добавить контакт
# def add_new_contact(file_name)
# 3. изменить контакт
# def edit_contact(file_name)
# 4. удалить контакт
# def remote_contakt(file_name)
# 5. найти контакт
# def find_contact(file_name)


# Андрей Ширяков;5568654;заместитель
# Сергей Рабчун;7653819;связист
# Александр Еремейчик;8303044;диспетчер
# Андрей Лазарь; 5567865;инженер
# Сергей Сновалов;5678754;водитель
# Алексей Свирид;09823478;диспетчер
#______________________________________________________________________

import os
import Menu

book = 'Homework\HW_seminar8\phones.txt'
Menu.open_phone_book_menu()