name_of_user = input("Введите свое имя")
surname_of_user = input("Введите свою фамилию")


def get_name(name = 'Аноним', surname="Анонимов"):
    print(name.strip().title() + ' ' + surname.strip().title())


get_name(surname=surname_of_user, name = name_of_user)
get_name()