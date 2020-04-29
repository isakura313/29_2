name_of_user = input("Введите свое имя")
surname_of_user = input("Введите свою фамилию")


def get_name(name, surname):
    print(name.strip().title() + ' ' + surname.strip().title())

# здесь у нас стоит с ошибкой, вообще нужно перевернуть
get_name(surname_of_user, name_of_user)
