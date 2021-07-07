# 1.
"""
Make the class with composition.
"""

class Laptop:
    def __init__(self):
        battery_1 = Battery('Lithium-Ion', 12, 5200)
        self.batteries = [battery_1]


class Battery:
    def __init__(self, type_battery, voltage, capacity):
        self.type_battery = type_battery
        self.voltage = voltage
        self.capacity = capacity

# 2.
    """
    Make the class with aggregation
    """
class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string

class GuitarString:
    def __init__(self):
        pass

guitar_str = GuitarString()
guitar = Guitar(guitar_str)

# 3
"""
    Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
    Note: this method should be static
    """
class Calc:

    @staticmethod
    def add_num(a, b, c):
        return a + b + c

print(Calc.add_num(3,4,5))
# 4 .
"""
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """

class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])


pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingredients)
# ['tomato', 'cucumber']
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingredients)
# ['bacon', 'parmesan', 'eggs']
pasta_3 = Pasta.carbonara()
print(pasta_3.ingredients)
# ['forcemeat', 'tomatoes']

# 5*.
"""
  Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
  In case of setting visitors_count - max_visitors_num should be checked,
  if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
  Example:
      Concert.max_visitor_num = 50
      concert = Concert()
      concert.visitors_count = 1000
      print(concert.visitors_count)  # 50
  """

class Concert:
    @classmethod
    def max_visitor_num(cls, num):
        return cls(num)

    @classmethod
    def visitors_count(cls, count):
        if count < Concert.max_visitor_num:
            print(count, Concert.max_visitor_num)
            return cls(count)
        else:
            print(count, Concert.max_visitor_num)
            return cls(Concert.max_visitor_num)



Concert.max_visitor_num = 50
Con = Concert.max_visitor_num
print(Con)
concert = Concert()
concert.visitors_count = 1000
print(concert.visitors_count)  # 50


#6.
class AddressBookDataClass:
    """
    Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
    """

# 7. Create the same class (6) but using NamedTuple
# 8.
class AddressBook:
    """
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
# 9.
class Person:
    """
    Change the value of the age property of the person object
    """
    name = "John"
    age = 36
    country = "USA"

# 10.
class Student:
    """
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

# 11*.
class Celsius:
    """
    By using @property convert the celsius to fahrenheit
    Hint: (temperature * 1.8) + 32)
    """
    def __init__(self, temperature=0):
        self._temperature = temperature


# create an object
# {obj} = ...
#
# print({obj}.temperature)v