def full_info(name, otchestvo, surname):
    """возвращает имя, фамилию, и, опционально возвращает отчество"""
    if otchestvo:
        full_name = name.strip().title() + " " + otchestvo.strip().title() + surname.strip().title()
    else:
        full_name = name.strip().title() + " " + surname.strip().title()
    return full_name


name_of_user = input("Введите ваше имя")
surname_of_user = input("Введите вашу фамилию")
otchestvo_of_user = input("Введите ваше отчество")

print(full_info(name_of_user, surname_of_user, otchestvo_of_user))