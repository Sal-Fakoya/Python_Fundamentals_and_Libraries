"""
                            INNER AND NESTED CLASSES
--> A nested class is a class defined inside another class. So the nested class is a
member of another class. This is different from child-parent class.
--> Just like a class can have properties and methods, a class can nest another class.

                            POLYMORPHISM (DUCKTYPING)
--> Polymorphism means one name and different forms.
--> 'poly' meaning more than one.
--> 'morph' meaning forms.
--> Polymorphism basically means one name by different forms.
--> Methods of polymorphism in python:
    --> Duck Typing
    --> Method Overloading
    --> Method Overriding
    --> Operator Overloading
"""


class Customer:

    def __init__(self, cust_id, name, b_door_num, b_street, b_city,
                 b_country, b_pin, ship_door_num, ship_street, ship_city,
                 ship_country, ship_pin):
        self.cust_id = cust_id
        self.name = name
        self.billing_address = self.Address(b_door_num, b_street, b_city, b_country, b_pin, )
        self.shipping_address = self.Address(ship_door_num, ship_street, ship_city, ship_country, ship_pin)

    class Address:
        def __init__(self, door_num, street, city, country, pin):
            self.door_num = door_num
            self.street = street
            self.city = city
            self.country = country
            self.pin = pin

        def display(self):
            print(self.door_num)
            print(self.street)
            print(self.city)
            print(self.country)
            print(self.pin)


c = Customer(10, 'John', 101, 'abc', 'delhi', 'india', 1001, 200, 'ijk', 'mumbai', 'india', 40001)
print(c.billing_address.display())
print(c.shipping_address.display())


def Driver(car):
    print(car.drive())


class Creta:
    def drive(self):
        return f'Creta is driving'


class Mercedes:
    def drive(self):
        return f'Mercedes is driving'


a = Creta()
Driver(a)

a = Mercedes()
Driver(a)


def Pet_Lover(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print('Duck is Talking')

    def walk(self):
        print('Duck is walking')


class Dog:
    def talk(self):
        print('Dog is talking')


d = Duck()
Pet_Lover(d)

d = Dog()
Pet_Lover(d)

