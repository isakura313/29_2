name_of_user = input("Введите свое имя")
surname_of_user = input("Введите свою фамилию")


def get_name(name, surname):
    full_name = name.strip().title() + ' ' + surname.strip().title()
    return full_name


Data_user = get_name(name_of_user, surname_of_user)
print(Data_user)
