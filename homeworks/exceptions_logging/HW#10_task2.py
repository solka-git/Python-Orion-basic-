# Task 2
# Напишіть клас робота пилососа
# в ініт приймається заряд батареї, заповненість сміттєбака і кількість води
#
# реалізуйте функцію move() - нескінченний цикл який на кожній ітерації "замерзає" на 1 сек
# окрім цього на кожній ітерації викликаються функції "wash" і "vacuum cleaner"
# (в цих функціях повинні стояти прінти "wash" і "vacuum cleaner" відповідно),
# також на кожній ітерації прінтиться "move"
# + на кожній ітерації цикла заряд батареї і кількість води зменшується на певну кількість
# (задайте в статік аргументах класу як конфіг пилососа, або в окремому конфіг файлі),
# а кількість сміття збільшується на рандомне ціле число в межах від 0 до 10
#
# Напишіть власні ексепшини які кидаються коли заряд батареї менше ніж 20%, заряд батареї 0%, кількість води - 0,
# кількість сміття більша ніж певне число.
# Опрацюйте ваші ексепшини (наприклад якщо заряд батареї менше 20% то цикл робить ще певну кількість ітерацій
# і зупиняється, якщо вода закінчилась то пилосос тепер не миє підлогу а тільки пилососить,
# 0 відсотків заряду - пилосос кричить щоб його занесли на зарядку бо сам доїхати не може)
#
# можете придумати ще свої ексепшини і як їх опрацьовувати

from random import randint
import configparser


class LowWaterError(Exception):
    pass


class EmptyWaterError(Exception):
    pass


class LowBatteryError(Exception):
    pass


class DischargedBattery(Exception):
    pass


class FullTrashError(Exception):
    pass


class VacuumCleaner:
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read("configfile.ini")  # читаем конфиг

    def __init__(self, battery,  garbage, water):
        self.battery = battery
        self.garbage = garbage
        self.water = water

        config = configparser.ConfigParser()
        config.read("configfile.ini")

        self.ENERGY_CONSUMPTION = int(config["VacuumCleaner"]["energy"])
        self.WATER_CONSUMPTION = int(config["VacuumCleaner"]["water"])
        self.BATTERY_LOW_LEVEL = int(config["VacuumCleaner"]["battery"])
        self.FULL_GARBAGE = int(config["VacuumCleaner"]["garbage"])

    def wash(self):
        try:
            if self.water == 0 or self.water < 0:
                raise EmptyWaterError
            print("** Wash **")
        except EmptyWaterError:
            print(" ): Sorry. No water no wash :( ")

    def vacuum_cleaner(self):
        print("-- Vacuum clean --")

    def move(self):
        print('$$$ Start Working $$$')
        time = 0
        while True:
            time += 1
            print(f"\n--- {time} Move ---")
            self.wash()
            self.vacuum_cleaner()
            try:
                if self.battery < self.BATTERY_LOW_LEVEL and self.battery != 0:
                    raise LowBatteryError
                if self.battery == 0:
                    raise DischargedBattery

            except LowBatteryError:
                number_iter = self.battery/2 - 8
                if number_iter < 8:
                    print("...I am going to charge...")
            except DischargedBattery:
                print("~~ Help me please, human. Take me to charge ~~")
                break

            try:
                if self.garbage >= self.FULL_GARBAGE:
                    raise FullTrashError
            except FullTrashError:
                print('): I am cannot clean with full trash. :(')
                break
            self.battery -= self.ENERGY_CONSUMPTION
            self.water -= self.WATER_CONSUMPTION
            self.garbage += randint(0, 10)


philips_robot = VacuumCleaner(25, 10, 10)
philips_robot.move()

# $$$ Start Working $$$
#
# --- 1 Move ---
# ** Wash **
# -- Vacuum clean --
#
# --- 2 Move ---
# ** Wash **
# -- Vacuum clean --
#
# --- 3 Move ---
#  ): Sorry. No water no wash :(
# -- Vacuum clean --
# ...I am going to charge...
#
# --- 4 Move ---
#  ): Sorry. No water no wash :(
# -- Vacuum clean --
# ...I am going to charge...
#
# --- 5 Move ---
#  ): Sorry. No water no wash :(
# -- Vacuum clean --
# ...I am going to charge...
#
# --- 6 Move ---
#  ): Sorry. No water no wash :(
# -- Vacuum clean --
# ~~ Help me please, human. Take me to charge ~~
#
# Process finished with exit code 0
