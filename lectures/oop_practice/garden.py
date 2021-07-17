from abc import abstractmethod


class GardenMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Garden(metaclass=GardenMeta):
    def __init__(self, vegetables, fruits, gardener, pests=0):
        self.vegetables = vegetables
        self.fruits = fruits
        self.pests = pests
        self.gardener = gardener

    def show_the_garden(self):

        print("Garden:")

        print(f'Vegetables: {self.vegetables.review()}')
        print(f'Fruits: {self.fruits.review()}')
        print(f'Gardener: {self.gardener.name}')
        if self.pests.number_of_pests == 0:
            print("Pests: 0")
        else:
            print(f'Pests: {self.pests.pests_type}, {self.pests.number_of_pests}\n')


class Vegetables:
    def __init__(self, vegetable_type):
        self.vegetable_type = vegetable_type

    states = {"0": "None", "1": "Flowering", "2": "Green", "3": "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")

class Fruits:
    def __init__(self, fruits_type):
        self.fruits_type = fruits_type

    states = {0: "None", 1: "Flowering", 2: "Green", 3: "Red"}

    @abstractmethod
    def growth(self):
        raise NotImplementedError('You missed me.')

    @abstractmethod
    def is_ripe(self):
        raise NotImplementedError("You missed me")


class Tomato(Vegetables):
    def __init__(self, vegetable_type, number_of_tomatoes):
        Vegetables.__init__(self, vegetable_type)
        self.number_of_tomatoes = number_of_tomatoes
        self.states = 0
        self.vegetable_type = vegetable_type

    def get_states(self):
        return int(self.states)

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def is_ripe(self):
        return self.states == 3

class Apple(Fruits):
    def __init__(self, fruits_type, number_of_apples):
        Fruits.__init__(self, fruits_type)
        self.number_of_apples = number_of_apples
        self.states = 0
        self.fruits_type = fruits_type

    def print_state(self):
        print(f"{self.fruits_type}, {self.number_of_apples} , {self.states}")

    def get_states(self):
        return int(self.states)

    def growth(self):
        if self.states < 3:
            self.states += 1
        self.print_state()

    def is_ripe(self):
        return self.states == 3

class TomatoBush:
    def __init__(self, number_of_tomatoes):
        self.tomatoes = [Tomato('Cherry', index) for index in range(0, number_of_tomatoes)]
        self.number_of_tomatoes = number_of_tomatoes

    def print_state(self):
        print(f"{self.vegetable_type}, {self.number_of_tomatoes} , {self.states}")

    def growth_all(self):
        for tomato in self.tomatoes:
            tomato.growth()


    def review(self):
        return f'tomato bush, {self.number_of_tomatoes} tomatoes'

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []
        self.number_of_tomatoes = 0

    def work_pests(self, pests):
        num = pests.number_of_pests
        for tomato in self.tomatoes:
            if tomato.get_states() > 1:
                if num > 0:
                    self.number_of_tomatoes -= 1
                    self.tomatoes.pop()
                    num -= 1
                    print("Pest had eaten plant\n")



class AppleTree:
    def __init__(self, number_of_apples):
        self.apples = [Apple('White', index) for index in range(0, number_of_apples)]
        self.number_of_apples = number_of_apples

    def growth_all(self):
        for apple in self.apples:
            apple.growth()

    def review(self):
        return f'apple tree, {self.number_of_apples} apples'

    def all_are_ripe(self):
        return all([apple.is_ripe() for apple in self.apples])

    def give_away_all(self):
        self.apples = []
        self.number_of_apples = 0

    def work_pests(self, pests):
        num = pests.number_of_pests
        for apple in self.apples:
            if apple.get_states() > 1:
                if num > 0:
                    self.number_of_apples -= 1
                    self.apples.pop()
                    num -= 1
                    print("Pest had eaten plant \n")




class Gardener:
    def __init__(self, name, plants):
        self.name = name
        self.plants = plants

    def work(self):
        for plant in self.plants:
            plant.growth_all()

    def harvest(self):
        for plant in self.plants:
            if plant.all_are_ripe():
                plant.give_away_all()
            else:
                print('Too early to harvest')

    def poison_the_pests(self, pests):
        if pests.number_of_pests > 0:
            pests.number_of_pests = 0
        else:
            print("There are no pests in the garden")


class Pests:

    def __init__(self, pests_type, number_of_pests):
        self.pests_type = pests_type
        self.number_of_pests = number_of_pests

    def eat_plant(self, plant):
        plant.work_pests(self)




Apple1 =  AppleTree(4)
Pests1 = Pests('apple_pests', 2)
Tomato_bush1 = TomatoBush(3)
John = Gardener('John', [Tomato_bush1, Apple1])
Garden1 = Garden(Tomato_bush1, Apple1, John, Pests1)
Garden1.show_the_garden()

John.work()
John.work()

Pests1.eat_plant(Apple1)
John.poison_the_pests(Pests1)
John.poison_the_pests(Pests1)

Garden1.show_the_garden()
John.work()
John.harvest()
Garden1.show_the_garden()
#
# Garden:
# Vegetables: tomato bush, 3 tomatoes
# Fruits: apple tree, 4 apples
# Gardener: John
# Pests: apple_pests, 2
#
# Cherry, 0 , 1
# Cherry, 1 , 1
# Cherry, 2 , 1
# White, 0 , 1
# White, 1 , 1
# White, 2 , 1
# White, 3 , 1
# Cherry, 0 , 2
# Cherry, 1 , 2
# Cherry, 2 , 2
# White, 0 , 2
# White, 1 , 2
# White, 2 , 2
# White, 3 , 2
# Pest had eaten plant
#
# Pest had eaten plant
#
# There are no pests in the garden
# Garden:
# Vegetables: tomato bush, 3 tomatoes
# Fruits: apple tree, 2 apples
# Gardener: John
# Pests: 0
# Cherry, 0 , 3
# Cherry, 1 , 3
# Cherry, 2 , 3
# White, 0 , 3
# White, 1 , 3
# Garden:
# Vegetables: tomato bush, 0 tomatoes
# Fruits: apple tree, 0 apples
# Gardener: John
# Pests: 0
#
