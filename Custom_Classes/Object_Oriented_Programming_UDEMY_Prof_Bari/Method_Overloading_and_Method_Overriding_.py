"""
                METHOD OVERLOADING
--> Overloading is used for polymorphism.
--> Overloading is when a single class method is used on various data types and gives different results.

                METHOD OVERRIDING
--> Method overriding means redefining a method of a parent class in the child class.
--> The method being overwritten becomes overshadowed by the redefined method
"""


class Arith:
    # Method Overloading
    def _sum(self, a, b, c=None):
        s = a + b
        if c == None:
            return s
        return s + c


a = Arith()
print(a._sum(10, 5))
print(a._sum('hello', 'world'))
print(a._sum(8.5, 5))

print(a._sum(5, 10, 3))
print(a._sum(8, 9))


# Method Overriding
class iPhone6:
    def home(self):
        print('Home button is pressed.')


class iPhoneX(iPhone6):
    def home(self):
        print('Home is touched')
        super().home()


i6 = iPhone6()
i6.home()

iX = iPhoneX()
iX.home()

