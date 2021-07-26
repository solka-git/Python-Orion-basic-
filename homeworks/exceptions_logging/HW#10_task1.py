# Task 1
# Напишіть калькулятор в якого будуть реалізовані операції додавання, віднімання, множення, ділення,
# піднесення в степінь, взяття з під кореня, пошук відсотку від числа
# калькулятор працює в нескінченному циклі. На кожній ітерації запитує перше число, операцію,
# друге число, після чого робить певну операцію з цими числами
#
# Огорніть в конструкцію try... except... потенційно "небезпечні" місця, наприклад отримання числа і приведення
# до типу даних або інструкції математичних операцій (ділення на нуль, наприклад)
#
# заповніть ваш скрипт логами
# Логи здебільшого інформаційні (викликали таку функцію з такими аргументами)
# + логи з помилками
# причому логи повинні записуватись у файл, тому що в консолі ви будете взаємодіяти з калькулятором,
# лог файл завжди відкривається в режимі дозапису.
# так як ви працюєте з файлом не забудьте про те що це потенційне місце поломки

import logging

template = "%(levelname)s: %(filename)s: %(asctime)s - %(message)s"
logging.basicConfig(level=logging.INFO, filename="Calculator.log", filemode="a", format=template)


def add(x, y):
    return f'{x} + {y} = {x+y}'


def subtract(x, y):
    return f'{x} - {y} = {x-y}'


def multiply(x, y):
    return f'{x} * {y} = {round(x*y, 3)}'


def divide(x, y):
    return f'{x} / {y} = {round(x/y, 3)}'


def pow_(x, y):
    return f'{x} ** {y} = {round(x**y, 3)}'


def root(x, y):
    return f'Корінь за основою {y} числа {x} = {round(pow(x, 1/y), 3)}'


def percent(x, y):
    return f'{y} percent of {x} = {round((x * y) / 100, 3)}'


def input_calc(msg):
    while True:
        try:
            num = float(input(msg))
        except ValueError:
            logging.error("Invalid input")
            print("Неправильний ввід. Операції проводяться тільки над числами.")
        else:
            break
    return num


print("*** КАЛЬКУЛЯТОР ****")
print("1.Додавання")
print("2.Віднімання")
print("3.Множення")
print("4.Ділення")
print("5.Піднесення до степеня(число, степінь")
print("6.Взяття з під кореня(число, основа кореня)")
print("7.Пошук відсотку від числа(число, відсоток)")
print("8.Вихід з програми")

while True:
    # Take input from the user
    choice = input("Введіть номер операції >> ")
    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
        if choice == '1':
            num1 = input_calc("Введіть перше число >> ")
            num2 = input_calc("Введіть друге число >> ")
            logging.info("func add()")
            print(add(num1, num2))

        elif choice == '2':
            num1 = input_calc("Введіть перше число >> ")
            num2 = input_calc("Введіть друге число >> ")
            logging.info("func substract()")
            print(subtract(num1, num2))

        elif choice == '3':
            num1 = input_calc("Введіть перше число >> ")
            num2 = input_calc("Введіть друге число >> ")
            logging.info("func multiply()")
            print(multiply(num1, num2))

        elif choice == '4':
            try:
                num1 = input_calc("Введіть перше число >> ")
                num2 = input_calc("Введіть друге число >> ")
                logging.info("func divide()")
                print(divide(num1, num2))

            except ZeroDivisionError:
                print("Помилка. Ділення на нуль.")
                logging.error("ZeroDivisionError")

        elif choice == '5':
            num1 = input_calc("Введіть перше число >> ")
            num2 = input_calc("Введіть степінь >> ")
            logging.info("func pow_()")
            print(pow_(num1, num2))

        elif choice == '6':
            try:
                num1 = input_calc("Введіть перше число >> ")
                num2 = input_calc("Введіть основу кореня >> ")
                logging.info("func root()")
                print(root(num1, num2))

            except ZeroDivisionError:
                print("Помилка. Ділення на нуль.")
                logging.error("ZeroDivisionError")

        elif choice == '7':
            num1 = input_calc("Введіть перше число >> ")
            num2 = input_calc("Введіть відсоток >> ")
            logging.info("func root()")
            print(percent(num1, num2))

        elif choice == '8':
            logging.info("func exit()")
            break
    else:
        print("Неправильний ввід. Такої операції не існує.")
        logging.error("Invalid input")

# *** КАЛЬКУЛЯТОР ****
# 1.Додавання
# 2.Віднімання
# 3.Множення
# 4.Ділення
# 5.Піднесення до степеня(число, степінь
# 6.Взяття з під кореня(число, основа кореня)
# 7.Пошук відсотку від числа(число, відсоток)
# 8.Вихід з програми
# Введіть номер операції >> hh
# Неправильний ввід. Такої операції не існує.
# Введіть номер операції >> 4
# Введіть перше число >> 0
# Введіть друге число >> 0
# Помилка. Ділення на нуль.
# Введіть номер операції >> 5
# Введіть перше число >> -56
# Введіть степінь >> -5
# -56.0 ** -5.0 = -0.0
# Введіть номер операції >> 7
# Введіть перше число >> 78.12345
# Введіть відсоток >> 99
# 99.0 percent of 78.12345 = 77.342
# Введіть номер операції >> 8
