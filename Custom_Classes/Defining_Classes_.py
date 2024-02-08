"""
                                    OBJECT
--> Everything in Python is an object. As object:
    --> It has a type (or class)
    --> It has state
    --> It has functionality
--> A list is a list object. It is an instance of a list class/list type.
    --> It's state are the 'elements' in the list
    --> It also has functionality, such as .append()


                                    CUSTOM CLASSES
--> We can define our own custom types (classes)
--> Instances of a class will have:
    --> a type (the custom type we created)
    --> some state (we can store values specific to the instance)
    --> functionality (methods that are functions bound to the instance)

                                INITIALIZERS
--> When we create a new instance of a class, we often want to create some initial state
    --> usually by passing arguments to the "creation" phase. This is called the initialization phase.
--> Step 1: Create an instance of a class (type) by calling it
--> Step 2: Pass some arguments used for initialization
--> Step 3: Call returns an initialized new instance of the class type.
    --> e.g reader = csv.reader(f, dialect= custom dialect)
        --> We create an instance of csv.reader class by calling it
        --> We pass some arguments used for initialization: file and dialect
        --> The call returns an initialized new instance of reader
    --> e.g d = Decimal('1.2345'):
        --> We create a new instance of Decimal class (type) by calling it
        --> We pass some argument '1.2345' used for initialization
        --> The call returns an initialized new instance of Decimal
    --> a = tuple([1,2,3,4]):
        --> We create a new instance by calling the tuple class [using ()]
        --> We pass an argument [1,2,3]
        --> The call returns a new tuple instance, initialized with elements [1,2,3]

                                    CLASSES AS BLUEPRINTS
--> Classes are often referred to as blueprints for creating objects.
--> A single class can be used to create multiple instances of that class.
    --> Each instance will have its own state
    --> The functions defined in the class become methods bound to the instance
    --> Because the functions are bound to the instance, they can access the state of the instance.

                                    CREATING CUSTOM CLASSES IN PYTHON
--> Use the "class" keyword, then the class name in title form.
--> The class then becomes callable, using the class_name with parenthesis, i.e Class_name()
--> When the callable class is assigned to a variable, the variable becomes a new instance of the class created.
--> The class and the variable will have some state python defined for us:
    --> For example, Class_name.__doc__ gives information about the class
    --> Class_name.__name__ returns a string that corresponds to the class_name
    --> The type(Class_name) of the instance can also return the class type
    --> and so on

                                DEFINING CUSTOM CLASSES
--> Classes are like templates for creating objects
    --> Objects have state and functionality.
    --> We can define what the state and functionality is using a class.
        --> Every instance of that class will have the functionality.
        --> The functions/methods must be able to access the instance value of the argument
    --> A python class needs at least 1 statement in the body, so, a string alone in the class body can make the
    class valid.
--> We can set/create attributes directly on the instances.
    --> Creating new attributes on an instance does not create the attribute for other instances of the same class.
--> We create instances of a class by calling the class.
--> We can set/get attributes directly on the instances using the dot notation.
    --> To create and initialize a circle instance
    --> These attributes exist in the instance namespace, normally a dictionary. To access the instance's namespace,
    use circle_instance_name.__dict__, the dunder dict method which sometimes returns the state in the dictionary.



"""
l1 = [1, 2, 3]
l2 = ['a', 'b', 'c']

from math import pi


class Circle:
    """
    This class can be used to represent a circle and calculate area
    and perimeter.
    """

    def __init__(self, radius):
        self.radius = radius

    # methods must be able to access radius by using self.radius
    def area(self):
        return round(pi * self.radius * self.radius, 2)

    def perimeter(self):
        return round(2 * pi * self.radius, 2)


circle_1 = Circle(radius=10)  # An instance
print(circle_1.area())
print(circle_1.perimeter())

print(Circle.__name__)
print(Circle.__doc__)
print(Circle.__class__ is type(Circle))

circle_2 = Circle(radius=5)

print(circle_1 is circle_2)  # Returns False because they are two different instances of Circle
print(type(circle_1) is Circle)

print(isinstance(circle_1, Circle))

circle_1.arc_length = 5
print(circle_1.arc_length)

circle_2.arc_length = 10
print(circle_2.arc_length)


class Person:
    """
    This string can be used to document this class - called a 'docstring'
    """


p1 = Person() # Instance of the class
print(p1)
print(Person.__doc__)

help(Person)

print(Person.__name__)

print(p1.__class__)

print(p1.__class__ is Person)

print(type(p1))

print(type([1, 2, 3]) is list)

a = 1
isinstance(a, int)

print(isinstance(p1, Person))
print(type(a) is int)

p1.name = 'John'

print(p1.name)

def hello():
    pass

hello.name = 'says hello'

print(hello.name)

del hello.name

del p1.name

print(globals())

print(p1.__dict__)

p1.name = 'John'

print(p1.__dict__)

p2 = Person()

print(p2.__dict__)
p2.first_name = 'John'
p2.last_name = 'Cleese'

print(p2.__dict__)

l = tuple([1,2,3])

print(type(l), l)








