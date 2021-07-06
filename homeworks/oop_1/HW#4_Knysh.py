# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Venicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# and will have seating_capacity own method


class Bus(Venicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        print('seating_capacity method')

# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(Bus))
#<class 'type'>

Bus_obj = Bus(100, 100)
print(type(Bus_obj))
#<class '__main__.Bus'>

# 4. Determine if School_bus is also an instance of the Vehicle class

School_bus = Bus(140, 1000)
print(isinstance(School_bus, Venicle))
print(issubclass(Bus, Venicle))

#True
#True

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus
# and will have its own - bus_school_color

class SchoolBus(School, Bus):
    pass

    def bus_school_color(self):
        print('bus_school_color method')

Sch_bus = SchoolBus(12, 400)
Sch_bus.seating_capacity()
Sch_bus.bus_school_color()

# seating_capacity method
# bus_school_color method

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method.

class Bear:
    def __init__(self, name):
        self.name = name

    def make_sound(self, sound=''):
        print(f"{self.name} sound is ")
        if sound == '':
            print('Roaar')
        else:
            print(sound)

class Wolf:
    def __init__(self, name):
        self.name = name


    def make_sound(self, sound=''):
        print(f"{self.name} sound is ")
        if sound == '':
            print('Owooo')
        else:
            print(sound)


# Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

winnie_pooh = Bear('Winnie')
grey_wolf = Wolf('Grey')

for animal in (winnie_pooh, grey_wolf):
    animal.make_sound()
    animal.make_sound('Aaaa')

# Winnie sound is
# Roaar
# Winnie sound is
# Aaaa
# Grey sound is
# Owooo
# Grey sound is
# Aaaa

# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".
#

class City():
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population


A_ins = City('Kovel', 600)
#Your city is too small

# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

class City:
    def __new__(cls, name, population):
        if population > 1500:
            return super().__new__(cls)
        else:
            return print("Your city is too small")

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __str__(self):
        return f"The population of the city {self.name} is {self.population}"

City1 = City('Kovel', 10560)
print(City1)

#The population of the city Kovel is 10560

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value
# which is greater than 10. And perform this add (+) of two instances.

class Add:
    def __init__(self, number):
        self.number = number

    def __add__(self, other):
       if self.number > 10 or other.number > 10:
            return self.number * other.number
       else:
            return self.number + other.number

a = Add(45)
b = Add(2)
print(f"result = {a+b}")
#result = 90
a = Add(5)
b = Add(2)
print(f"result = {a+b}")
#result = 7


# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions
# and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.

class CallSumm:
    def __call__(self, a, b):
        return a + b


call1 = CallSumm()
print("Result = ", call1(12, 13))

#Result =  25

# 12*. Making Your Objects Truthy or Falsey Using __bool__().
# Create class MyOrder with cart and customer instance attributes.
# Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.
# e.g.:
# order_1 = MyOrder(['a', 'b', 'c'], 'd')
# order_2 = MyOrder([], 'a')
# bool(order_1)
# True
# bool(order_2)
# False


class MyOrder:
    def __init__(self, card, customer):
        self.card = card
        self.customer = customer

    def __bool__(self):
        return len(self.card) > 0

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
#True
print(bool(order_2))
#False