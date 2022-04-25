"""
Упражнения главы 6
"""

# 1. 
class Thing():
    pass

example = Thing()

# 2.
class Thing2():
    letters = 'abc'

# 3.
class Thing3():
    def __init__(self):
        self.letters = 'xyz'

example3 = Thing3()

# 4.
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

element = Element('Hydrogen', 'H', 1)

# 5.
el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**el_dict)

# 6.
class Element2():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print("name is %s, symbol is %s, number is %s" % (self.name, self.symbol, self.number))

hydrogen2 = Element2(**el_dict)

# 7.
class Element3():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return "name is %s, symbol is %s, number is %s" % (self.name, self.symbol, self.number)

hydrogen3 = Element3(**el_dict)

# 8.
class Element4():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return "name is %s, symbol is %s, number is %s" % (self.name, self.symbol, self.number)

element4 = Element4(name='Helium', symbol='He', number=2)

# 9.
class Bear():
    def eats(self):
        return 'berries'

    @staticmethod
    def eats():
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'

class Octothorpe():
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octo = Octothorpe()

# 10.
class Laser():
    def does(self):
        return 'desintergrate'

class Claw():
    def does(self):
        return 'crush'

class SmartPhone():
    def does(self):
        return 'ring'

class Robot():
    def __init__(self, name):
        self.name = name
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()

    def does(self):
        return f"""My laser can {self.laser.does()}.
My claw can {self.claw.does()}.
My smartphone can {self.smartphone.does()}"""


robbie = Robot('Robbie')

if __name__ == '__main__':
    print("# 1")
    print("Thing is :" , Thing)
    # Выводится <class '__main__.Thing'>
    print("example is : ", example)
    # Выводится <__main__.Thing object at _____>
    print("# 2")
    print("Thing2 letters is : ", Thing2.letters)
    print("# 3")
    try:
        print("Thing3 letters is : ", Thing3.letters)
    except Exception as err: 
        print(err)
        print("Нужно создать объект класса Thing3")
    print("example3 letters of Thing3 is : ", example3.letters)
    print("# 4")
    print("element is : ", element)
    print("element name is: ", element.name)
    print("element symbol is: ", element.symbol)
    print("element number is: ", element.number)
    print("# 5")
    print("hydrogen is : ", hydrogen)
    print("hydrogen name is: ", hydrogen.name)
    print("hydrogen symbol is: ", hydrogen.symbol)
    print("hydrogen number is: ", hydrogen.number)
    print("# 6")
    print("hydrogen2 dump is: ")
    hydrogen2.dump()
    print("# 7")
    print("hydrogen3 is: ", hydrogen3)
    print("# 8")
    print("element4 is: ", element4)
    print("element4 name is: ", element4.name)
    print("element4 symbol is: ", element4.symbol)
    print("element4 number is: ", element4.number)
    try:
        print(element4.__name)
    except AttributeError as err:
        print(err)
        print("Name is hidden")
    print("Hidden name is: ", element4._Element4__name)
    print("# 9")
    print("bear eats ", bear.eats())
    print("Bear eats ", Bear.eats())
    print("rabbit eats ", rabbit.eats())
    print("octo eats ", octo.eats())
    print("# 10")
    print(f"{robbie.name} does: ")
    print(robbie.does())

