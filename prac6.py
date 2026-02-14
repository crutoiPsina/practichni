class Thing:
    pass

print(Thing)
example = Thing()
print(Thing)

class Thing2:
    letters = 'abc'

print(Thing2.letters)


class Thing3:
    pass

obj = Thing3()
obj.letters = 'xyz'

print(obj.letters)


class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

hydrogen = Element('Hydrogen', 'H', 1)


data = {
    'name': 'Hydrogen',
    'symbol': 'H',
    'number': 1
}

hydrogen = Element(**data)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()

print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f"{self.name} {self.symbol} {self.number}"


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)

class Element:
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

class Bear:
    def eats(self):
        return 'berries'

class Rabbit:
    def eats(self):
        return 'clover'

class Octothorpe:
    def eats(self):
        return 'campers'

bear = Bear()
rabbit = Rabbit()
octo = Octothorpe()

print(bear.eats())
print(rabbit.eats())
print(octo.eats())

class Laser:
    def does(self):
        return 'disintegrate'

class Claw:
    def does(self):
        return 'crush'

class SmartPhone:
    def does(self):
        return 'ring'

class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.phone = SmartPhone()

    def does(self):
        print(self.laser.does())
        print(self.claw.does())
        print(self.phone.does())

robot = Robot()
robot.does()

