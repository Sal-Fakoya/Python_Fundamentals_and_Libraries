"""
                        OBJECTS:
--> An object is a container for variables and functions. For example, a monster object might contain:
    --> Variables for health, energy, stamina, damage.
    --> Functions for attack, movement and animations
--> The variables and functions only exist inside the object.
--> Although they have special names;
    --> Variables in an object are called "attributes".
    --> Functions in an object are called "methods"
--> It is possible to have multiple objects. These multiple objects can have custom attributes but the objects will
all share the sam methods.
--> Each object has its own attributes and methods.
--> Objects can also interact with each other.

                            CLASSES:
--> A class is a blueprint for an object.
--> When creating an object we first need a class.
--> A class can also accept arguments to customise the object being created.
--> A class can inherit from other classes.
    --> The resulting objects will have attributes and methods from both classes.
-->
                        Object-Oriented-Programming (OOP):
--> You code is organised via objects, and allowing the objects to interact with each other.
--> Almost all large projects in any programming language are organised in OOP.


                        WHY USE CLASSES AND OBJECTS:
--> They organise complex code.
--> They help create reusable code.
--> They are used everywhere.
--> Some modules require you to use classes, example, PyQt, Tkinter, matplotlib
--> Classes make it easier to work with scope.
--> However, you can write code without creating classes. But programming is easier and better organised with classes.


                        CREATING AND USING OBJECTS:
--> 1. Create a class using the "class" keyword:
--> 2. Class name are writter in camel case, e.g class Monster.
-->


                        __DUNDER__ METHODS:
--> "Dunder" stands for "double underscore methods".
--> A dunder method is a method that is not called by the user.
--> Instead, it is called by python when something happens
    --> __init__ is called when the object is being created.
    --> __len__ is called when the object is passed into len() function.
    --> __abs__ is called when the object is passed into abs() function.
--> The __init__ method is created in the class by declaring it using 'def' just like any other methods.


                        CLASS DEEP DIVE
--> Everything in python is an object including inbuilt strings, integers etc. Even functions are objects!
--> A function and a method both execute a block of code. The difference is that a method belongs to an object.
    --> e.g len('test') is a function. 'test'.upper() returns upper case for the method of the string 'test'


"""


# class Monster:
#     def __init__(self, health, energy):
#         #
#         self.health = health
#         self.energy = energy
#         # self.health refers to the attribute health of the class Monster.
#         # health refers to the parameter health.
#
#         self.energy = energy
#         print('The monster was created')
#
#     # methods
#     def __len__(self):
#         return 5
#
#     def __abs__(self):
#         return self.energy
#
#     def __call__(self):
#         return 'The monster was called.'
#
#     def __add__(self, other):
#         return self.health + 10
#
#     def __str__(self):
#         return f'A monster with health {self.health} and energy {self.energy}'
#
#     def attack(self, amount=0):
#         print('The monster has attacked!')
#         print(f'The {amount} of damage was dealt')
#         print(self.energy)
#         self.energy -= 20
#         print(self.energy)
#
#     def move(self, speed=0):
#         print('The monster has moved')
#         print(F'Speed of {speed}')
#
#
# monster1 = Monster(health=10, energy=20)
#
#
# print(monster1.health)
# print(len('test'))
# print(len(monster1))
# print(abs(monster1))
#
# print(dir(monster1))
#
# print(monster1.__dict__)
#
# print(monster1())
# print(monster1 + 55)
#
# print(str(monster1))
# print(monster1)


def test():
    pass


a = test
# print(dir(test))

print(dir(a))

a.another_attribute = 10
print(dir(a))
print(a.another_attribute)


def add(a, b):
    return a + b


class Test:
    def __init__(self, add_function):
        self.add_function = add_function


test = Test(add_function=add)

print(test.add_function(1, 2))


# Create a Monster class with a parameter called func, store this func as a parameter
# Create another class, called Attacks, that has 4 methods: bite, slash, kick (each method just prints some text)

# Create a monster object and give it one of the attack methods from the attack class.

class Monster:
    def __init__(self, func):
        self.func = func


class Attacks:
    def __int__(self):
        pass

    def bite(self):
        return f'One bite is 10 energy!'

    def slash(self):
        return '-10 gone'

    def kick(self):
        return 'buy a kick'

monster = 30










