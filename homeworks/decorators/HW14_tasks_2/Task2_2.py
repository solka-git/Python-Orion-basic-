# 1. Дану задачу робити через декоратор як функції!
# Написати декоратор який зробить з будь-якої функції строго типізовану. Тобо це декоратор який приймає аргументи.
# Аргументами будуть типи даних, порядок аргументів декоратору відповідає порядку аргументів функції
# Приклад:
# @decor(int, float, int, float)
# def func(1, 1.2, 4)
# Зверніть увагу що декоратор приймає на 1 аргумент більше ніж функція, останній аргумент це строга типізація того, що
# функція повертає
# можете написати власний ексепшин і кидати його тоді коли тип даних не відповідає тому, що очікується
#
# 2. Те ж саме що й в завданні 1, але зробити через функтор

class WrongTypeError(Exception):
    pass


class DecorClass:
    def __init__(self, type1, type2, type3, type4):
        self.type1 = type1
        self.type2 = type2
        self.type3 = type3
        self.type4 = type4

    def __call__(self, func):
        def wrap(a, b, c):
            try:
                if isinstance(a, self.type1) and isinstance(b, self.type2) \
                        and isinstance(c, self.type3) \
                        and isinstance(func(a, b, c), self.type4):
                    return func(a, b, c)
                else:
                    raise WrongTypeError
            except WrongTypeError:
                print("Wrong type.")
        return wrap


@DecorClass(int, float, int, float)
def func_(a, b, c):
    return sum([a, b, c])


print(func_(1, 6.9, 4))
