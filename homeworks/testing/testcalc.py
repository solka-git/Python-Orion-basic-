# Task1
# В клас калькулятора написаного на лекції, добавити функції пошук відсотку від числа, піднесення в степінь,
# взяття з під квадратного кореня
# В кожний метод добавити доктести
# Дописати юніттести для всіх методів калькулятора

class Calc:
    @staticmethod
    def sum(a, b):
        """
        >>> Calc.sum(3, 5)
        8
        >>> Calc.sum(3.9, 7.1)
        11.0
        >>> Calc.sum(9, 8.0)
        17.0

        operation a+b
        :param a: number 1, int or float
        :param b: number 2, int or float
        :return: int or float
        """
        return a + b

    @staticmethod
    def minus(a, b):
        """
        >>> Calc.minus(-3, 0)
        -3
        >>> Calc.minus(3, -3.0)
        6.0

        operation a - b
        :param a: number 1, int or float
        :param b: number 2, int or float
        :return: int or float
        """
        return a - b

    @staticmethod
    def mul(a, b):
        """
        >>> Calc.mul(4, 4)
        16

        operation a * b
        :param a: number 1, int or float
        :param b: number 2, int or float
        :return: int or float
        """
        return a * b

    @staticmethod
    def div(a, b) -> float:
        """
        >>> Calc.div(-9, 3)
        -3.0

        operation a / b
        :param a: number 1, int or float
        :param b: number 2, int or float, != 0
        :return: int or float
        """
        return a / b

    @staticmethod
    def percent(a, b) -> float:
        """
        >>> Calc.percent(100, 10)
        10.0

        :param a: number, int or float
        :param b: percent, int or float
        :return: percent of number, float
        """
        return (a * b) / 100

    @staticmethod
    def pow(a, b):
        """
        >>> Calc.pow(3, 2)
        9
        >>> Calc.pow(-3, 3)
        -27
        >>> Calc.pow(4, 1/2)
        2.0
        >>> Calc.pow(4, 0.5)
        2.0
        >>> Calc.pow(4, -2)
        0.0625

        operation a ** b
        :param a: number, int or float
        :param b: degree, int or float
        :return:  degree of number, int or float
        """
        return a ** b

    @staticmethod
    def sqrt(a) -> float:
        """
        >>> Calc.sqrt(9)
        3.0
        >>> Calc.sqrt(0.0625)
        0.25

        operation a ** 0.5
        :param a: number, >0, int or float
        :return: float
        """
        return a ** 0.5
