# 1. Дану задачу робити через декоратор як функції!
# Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
# Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
# Приклад:
# @decor(int, float, int, float)
# def func(1, 1.2, 4)
# Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
# функція повертає
# можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується


class WrongTypeError(Exception):
    pass


def decor(type1, type2, type3, type4):
    def decor_in(func):
        def wrap(a, b, c):
            try:
                if isinstance(a, type1) and isinstance(b, type2) \
                        and isinstance(c, type3) \
                        and isinstance(func(a, b, c), type4):
                    return func(a, b, c)
                else:
                    raise WrongTypeError
            except WrongTypeError:
                print("Wrong type.")
        return wrap
    return decor_in


@decor(int, float, int, float)
def func_(a, b, c):
    return sum([a, b, c])


print(func_(1, 6.9, 4))
