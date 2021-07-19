from __future__ import annotations
from typing import Dict, Any
from abc import ABC, abstractmethod
import random
from random import randint
import uuid

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




#
# class Animal(ABC):
#
#     def __init__(self, power: int, speed: int):
#         self.id = None
#         self.max_power = power
#         self.current_power = power
#         self.speed = speed
#
#     @abstractmethod
#     def eat(self, forest: Forest):
#         raise NotImplementedError

class Animal:

    def __init__(self, power: int, speed: int):
        self.id = uuid.uuid4()
        self.max_power = power
        self.current_power = power
        self.speed = speed

    def eat(self, forest: Forest):
        pass


class Predator(Animal):


    # def __init__(self):
    #     self.strength = randint(25, 100)
    #     self.speed = randint(25, 100)
    #     BIRTH_STRENGTH = self.strength

    def eat(self, forest: Forest):
        lst1 = list(forest.animals.keys())
        victim_id = random.choice(lst1)
        if self.id == victim_id:
            print(f'Animal {self.id} is unlucky')
        if self.speed > forest.animals[victim_id].speed:
            if self.current_power > forest.animals[victim_id].current_power:
                forest.remove_animal(forest.animals[victim_id])
                print(f'{forest.animals[victim_id]} dead')
        else:
            self.current_power = 0.7 * int(self.current_power)
            forest.animals[victim_id].current_power = 0.7 * int(forest.animals[victim_id].current_power)
            print(f'Current power of {self.id} = {self.current_power}')
            print(f'Current power of {forest.animals[victim_id]} = {forest.animals[victim_id].current_power}')
        if self.current_power < 0:
            forest.remove_animal(self.id)
        if forest.animals[victim_id].current_power < 0:
            forest.remove_animal(forest.animals[victim_id])




class Herbivorous(Animal):


    def eat(self, forest: Forest):
        self.current_power += 0.5 * self.current_power
        if self.current_power > self.max_power:
            self.current_power = self.max_power
        print(f'Current power of {self.id} = {self.current_power}')

AnyAnimal: Any[Herbivorous, Predator]


class Forest:

    def __init__(self):
        self.animals: Dict[str, AnyAnimal] = dict()

    def add_animal(self, animal: AnyAnimal):
        self.animals[f'{animal.id}'] = animal
        print(f'Added a {animal}')

    def remove_animal(self, animal: AnyAnimal):
        del self.animals[animal.id]

    def any_predators(self):
        flag = False
        for key in self.animals:
            if isinstance(self.animals[key], Predator):
                flag = True
        return flag



def animal_generator():
    nature = []
    for i in range(randint(3, 5)):
        if randint(0, 1) == 1:
            nature.append(Herbivorous(randint(25, 100), randint(25, 100)))
        else:
            nature.append(Predator(randint(25, 100), randint(25, 100)))
    return nature






if __name__ == "__main__":
    nature = animal_generator()
    print(nature)
    nature_iterator = iter(nature)
    forest = Forest()
    for i in range(len(nature)):
        animal = next(nature_iterator)
        forest.add_animal(animal)
    print(forest.animals)

    print("game starts")
    for animal in forest.animals.values():
        animal.eat(forest=forest)
    # while True:
    #     if forest.any_predators():
    #         print("Game over! There are no predators in the forest.")
    #     for animal in forest:
    #



    # Create forest
    # Create few animals
    # Add animals to forest
    # Iterate throw forest and force animals to eat until no predators left
    # animal_generator to create a random animal







