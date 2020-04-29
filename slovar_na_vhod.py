import random


persons = {'names':[], 'surnames': []}
greet_spi = []

funny_words = ['прикольный', 'смешной', 'позитивный' , 'ловкий']

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

def speechy_funny(slovar):
    for i in range(0, len(slovar['names'])):
        rand_word = random.choice(funny_words)
        greet = rand_word + " " + slovar['names'][i] + ' '+ slovar['surnames'][i]
        greet_spi.append(greet)
    return  greet_spi

count = 0
while count < amount_of_users:
    add_info(full_info())
    count += 1

print (speechy_funny(persons))
print(persons)