persons = {'names':[], 'surnames': []}

def add_info(spisok):
    """ Возвращает словарь с информацией о человеке"""
    persons['names'].append(spisok[0])
    persons['surnames'].append(spisok[1])
    return persons

amount_of_users = int(input("Сколько у нас есть пользователей? "))

def full_info():
    name = input("введите имя пользователя")
    surname = input("Введите фамилию пользователя")
    data = [name.strip().title(), surname.strip().title()]
    return data

count = 0
while count < amount_of_users:
    add_info(full_info())
    count += 1

print(persons['names'])
print(persons['surnames'])