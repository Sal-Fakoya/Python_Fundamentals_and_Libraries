"""
                            ACCESSORS AND MUTATORS
--> Accessors are used to read the property of a class or object. It's basically a reading method
--> Mutators are used for writing or updating the properties of a class and its objects. It is basically a writing
method.






"""
class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def getlength(self):
        return self.length

    def setlength(self, l):
        self.length = l

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(10,5)
print(r.getlength())
r.setlength(15)
print(r.area())



