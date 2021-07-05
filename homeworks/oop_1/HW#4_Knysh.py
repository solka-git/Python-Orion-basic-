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
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, bus_school_color):
        super(School).__init__(get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage)
        self.bus_school_color = bus_school_color

print(SchoolBus.mro())


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
# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}
# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value
# which is greater than 10. And perform this add (+) of two instances.
# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions
# and can be called like a function.
# Create a new class with __call__ method and define this call to return sum.
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