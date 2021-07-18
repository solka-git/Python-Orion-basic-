# Survival
#
# 1. In the Forest (Iterable) lives Predators and Herbivores (abstract class of animal and two offspring).
# Each animal is born with the following parameters (by using random):
# - strength (from 25 to 100 points)
# - speed (from 25 to 100 points)
# The force cannot be greater than it was at birth (initialization).

#  У лісі (Ітерабельний) живе Хижаки та рослиноїдні тварини (абстрактний клас тварин і двоє потомків).
# Кожна тварина народжується з наступними параметрами (за допомогою випадкових випадків):
# - міцність (від 25 до 100 балів)
# - швидкість (від 25 до 100 балів)
# Сила не може бути більшою, ніж була при народженні (ініціалізація).

from abc import ABC, abstractmethod
from random import random, randint


class Animal(ABC):
    @abstractmethod
    def __init__(self):
        raise NotImplementedError


class Predator(Animal):
    def __init__(self):
        self.strength = randint(25, 100)
        self.speed = randint(25, 100)
        BIRTH_STRENGTH = self.strength

class Herbivores(Animal):
    def __init__(self):
        self.strength = randint(25, 100)
        self.speed = randint(25, 100)

    # def get_strength(self):
    #      return

    def eat(self):
        self.strength = 50
        print(self.strength)
        print(self.BIRTH_STRENGTH)




# На кожному кроці гри беремо по 1 тварині з лісу (ітерація):
# - Якщо вона рослиноїдна, то їсть (відновлює свою силу на 50%).
# - Якщо це хижак, він полює - навмання вибирає тварину з лісу і:
#     - витягнувся, йому не пощастило і він залишився без обіду;
#     - витягнув іншу тварину, потім намагається наздогнати;
#     - якщо він може наздогнати, він наздоганяє і атакує;
#     - якщо атакований і сильніший, тоді з’їдає і відновлює 50% сили;
#     - не наздогнав або не вистачило сили, тоді він і щаслива здобич втрачають 30% сили (бо обидва або бігли, або билися, або всі разом)
#
# Тварина, термін дії якої закінчився, вмирає. (Ви можете перевірити міцність під час пошуку їжі)
#
# Гра триває до тих пір, поки хижаки знаходяться в лісі.



