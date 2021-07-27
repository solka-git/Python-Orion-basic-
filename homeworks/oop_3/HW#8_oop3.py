"""  Survival """

from __future__ import annotations
import time
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
from random import randint
import uuid


class Animal(ABC):

    def __init__(self, power: int, speed: int, name):
        self.name = name
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        pass


class Predator(Animal):

    def eat(self, forest: Forest):
        print('*** Hunting ***')
        victim_id = random.choice(list(forest.animals.keys()))
        if self.id == victim_id:
            print(f'{self.name} is unlucky. Animal left without any food')
        else:
            if self.speed > forest.animals[victim_id].speed:
                print(f'{self.name} caught up {forest.animals[victim_id].name}')
                if self.current_power > forest.animals[victim_id].current_power:
                    print(f'The predator killed {forest.animals[victim_id].name}.')
                    forest.remove_animal(forest.animals[victim_id])
                else:
                    self.current_power = int(0.7 * int(self.current_power))
                    forest.animals[victim_id].current_power = int(0.7 * int(forest.animals[victim_id].current_power))
                    print(f'Current power of predator {self.name} = {self.current_power}')
                    print(f'Current power of victim {forest.animals[victim_id].name} = {forest.animals[victim_id].current_power}')

        if victim_id in forest.animals.keys():
            if forest.animals[victim_id].current_power == 0:
                print(f'{forest.animals[victim_id].name} was dead')
                forest.remove_animal(forest.animals[victim_id])

        if self.current_power == 0:
            print(f'{self.name} was dead')
            forest.remove_animal(self)


class Herbivorous(Animal):

    def eat(self, forest: Forest):
        print(f'{self.name} restores its strength')
        self.current_power += int(0.5 * self.current_power)
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        print(f'Current power = {self.current_power}')


AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: AnyAnimal):
        self.animals.pop(animal.id)

    def any_predators(self):
        return all(isinstance(self.animals[key], Herbivorous) for key in self.animals)
        # flag = False
        # for key in self.animals:
        #     if isinstance(self.animals[key], Predator):
        #         flag = True
        # return flag

    def only_predators(self):
        return any(isinstance(self.animals[key], Herbivorous) for key in self.animals)
        # flag = False
        # for key in self.animals:
        #     if isinstance(self.animals[key], Herbivorous):
        #         flag = True
        # return flag




def animal_generator():
    nature = []
    for i in range(randint(2, 3)):
        if randint(0, 1) == 1:
            nature.append(Herbivorous(randint(25, 100), randint(25, 100), name='Herbivorous'+str(i)))
        else:
            nature.append(Predator(randint(25, 100), randint(25, 100), name='Predator'+str(i)))
    return nature


if __name__ == "__main__":
    nature = animal_generator()
    nature_iterator = iter(nature)
    forest = Forest()
    for i in range(len(nature)):
        animal = next(nature_iterator)
        forest.add_animal(animal)

    print('Forest:')
    for animal in forest.animals.values():
        print(f'{animal.name}: power {animal.current_power}')

    print("\n*** *** GAME STARTS *** ***")
    for animal in forest.animals.values():
        print(f'{animal.name}: power {animal.current_power}')

    level = 1
    while True:
        print(f'\n*** LEVEL {level} ***')
        if forest.any_predators():
            print("*** *** Game over! *** *** \n*** There are no predators in the forest ***")
            break
        if not forest.only_predators():
            print("*** *** Game over! *** *** \n*** There are only predators in the forest ***")
            break
        random.choice(list(forest.animals.values())).eat(forest)
        for animal in forest.animals.values():
            print(f'{animal.name}: power {animal.current_power}')
        time.sleep(1)
        level += 1

    print('Forest:')
    for animal in forest.animals.values():
        print(f'{animal.name}: power {animal.current_power}')

#
#
# Forest:
# Predator0: power 98
# Herbivorous1: power 55
#
# *** *** GAME STARTS *** ***
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 1 ***
# Herbivorous1 restores its strength
# Current power = 55
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 2 ***
# Herbivorous1 restores its strength
# Current power = 55
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 3 ***
# Herbivorous1 restores its strength
# Current power = 55
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 4 ***
# *** Hunting ***
# Predator0 is unlucky. Animal left without any food
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 5 ***
# Herbivorous1 restores its strength
# Current power = 55
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 6 ***
# Herbivorous1 restores its strength
# Current power = 55
# Predator0: power 98
# Herbivorous1: power 55
#
# *** LEVEL 7 ***
# *** Hunting ***
# Predator0 caught up Herbivorous1
# The predator killed Herbivorous1.
# Predator0: power 98
#
# *** LEVEL 8 ***
# *** *** Game over! *** ***
# *** There are only predators in the forest ***
# Forest:
# Predator0: power 98
#
# Process finished with exit code 0







