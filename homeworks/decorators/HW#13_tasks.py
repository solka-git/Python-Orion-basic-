# 1. Написати функцію яка в циклі зчитує з консолі введені користувачем дані і записує їх в список.
# Написати декоратор який видасть час виконання роботи функції
#
import time


def decor_time_check(func):
    def wrap():
        t1 = time.time()
        result = func()
        print('Time = ', time.time() - t1)
        return result
    return wrap


@decor_time_check
def func_list():
    print('Enter data and press \'Enter\'.')
    return [x for x in input().split(' ')]


# print(func_list())


# Enter data and press 'Enter'.
# u i u iu 99
# Time =  5.352323532104492
# ['u', 'i', 'u', 'iu', '99']


# 2. Написати функцію яка приймає два катети і повертає значення гіпотензузи. Написати декоратор на функцію,
# який виводить на екран текст з довжиною катетів і гіпотенузи.
# Важливо! Функція повинно повернути саме значення гіпотенузи як число, а декоратор повинен зробити вивід на екран
# наприклад такого тексту “При катетах 3, 4 – гіпотенуза дорівнює 5”.
#

def decor_text(func):
    def wrap(*args):
        cathetus_1, cathetus_2 = args
        result = func(*args)
        print(f'If cathetus {cathetus_1} and {cathetus_2} then hypotenuse = {result}')
        return result
    return wrap


@decor_text
def hypotenuse(cathetus_1, cathetus_2):
    return pow((cathetus_1 ** 2) + (cathetus_2 ** 2), 0.5)


# hypotenuse(6, 8)


# 3. Написати функцію яка приймає список елементів і знаходить суму, до функції написати декоратор який перед тим як
# запустити функцію видаляє з списку всі не чисельні типи даних, але якщо є строка яку можна перевести в число,
# (наприклад “1”) то строка приводиться до чисельного типу даних
#

def filter_(func):
    def wrap(list_):
        # new_list = []
        # for el in list_:
        #     if isinstance(el, (int, float)):
        #         new_list.append(el)
        #     else:
        #         try:
        #             elm = float(el)
        #             new_list.append(elm)
        #         except (ValueError, TypeError):
        #             continue
        # return func(new_list)
        new_list = []
        for el in list_:
            try:
                new_list.append(float(el)) if type(el) != int else new_list.append(el)
            except (ValueError, TypeError):
                continue
        return func(new_list)
    return wrap



@filter_
def sum_(list_):
    return sum(list_)


print(sum_([1, 2, 3, 'k', '4', '5.5', 4.5, [5], {'9': 8}]))

# 4. Написати функцію яка приймає на вхід ціле число n створює і повертає список цілих чисел від 0 до n.
# Написати до цієї функції декоратор який всі елементи отриманого списку переведе в строковий тип даних


def decor_str(func):
    def wrap(n):
        return [str(el) for el in func(n)]
    return wrap


@decor_str
def func_list(n):
    return [x for x in range(n+1)]


# print(func_list(5))
