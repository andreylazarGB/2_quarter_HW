

def print_all_phone_book(file_name):
    with open(file_name, 'r', encoding='utf-8') as date_phones:
        date_phones = date_phones.readlines()
        date_phones = list(map(lambda x: x.strip().replace(';', ' '), date_phones))
        print('\n'.join(date_phones))


def add_new_contact(file_name):
    with open(file_name, 'a', encoding='utf-8') as date_phones:
        new_contact = input('введите Имя Фамилию;телефон;комментарий для нового контакта - ')
        date_phones.write('\n'+new_contact)


def edit_contact(file_name):
    date_work = open(file_name, 'r', encoding='utf-8')
    date_phones = date_work.readlines()
    date_work.close()

    line_to_edit = input('введите фамилию контакта, который нужно изменить: ')
    search_line = list(filter(lambda x: line_to_edit in x, date_phones))
    print(search_line)
    date_to_edit = input('введите что поменять - ')
    date_to_update = input('введите на что поменять - ')
    print(f'заменить "{date_to_edit.upper()}" на "{date_to_update.upper()}"')
    for line in range(len(date_phones)):
        if date_to_edit in date_phones[line]:
            date_phones[line] = date_phones[line].replace(date_to_edit, date_to_update)
            #print(date_phones[line])
    date_work = open(book, 'w', encoding='utf-8')
    date_work.writelines(date_phones)
    date_work.close()


def remove_contakt(file_name):
    with open(file_name, 'r', encoding='utf-8') as source, open('out.txt', 'w', encoding='utf-8') as dest:
        line_to_remove = input('введите контакт для удаления - ')
        for line in source:
            if line_to_remove not in line:
                dest.write(line)
    os.remove(file_name)
    os.rename('out.txt', book)

def find_contact(file_name):
    with open(file_name, 'r', encoding='utf-8') as data_phones:
        line_to_find = input('введите контакт для поиска - ')
        for line in data_phones:
            if line_to_find in line:
                print(line)