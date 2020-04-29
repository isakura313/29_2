import random


def get_name():
    name = input("Введите ваше имя: ")
    return name.strip().title()


def generate_number(name):
    name_length = len(name)
    rand_str = ''
    for i in range(name_length):
        rand_num = random.randint(1, 9)
        rand_str += str(rand_num)
    return name, rand_str

def get_full_data():
    number = generate_number(get_name())
    return str(number)

print(get_full_data())