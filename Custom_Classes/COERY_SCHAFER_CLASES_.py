"""
--> Instance variables contain data that is unique to each instance.
--> Class variables are variables that are shared among all instances of a class. While instance variables can be
unique for each instance, class variables should be the same for each instance. We can access class variables using
classname_variable in the class. We can also access by using self.class_variable in the class or obj.class_variable
because when trying to access an attribute on an instance, python will first check if the instance contains the
attribute, and if it doesn't, python will check if the class or any class that it inherits from contains that
attribute.

                    Regular methods, Class Methods and Static Methods
--> Regular methods take in self and/OR other parameters
--> Class methods take the class as the parameter when defined in the class using @classmethod first.
--> Class methods are used as alternative constructors

--> STATIC METHODS: are methods that don't pass anything when defined. They don't pass the instance(self) or the
class(cls) like regular methods and class methods. They behave just like regular functions, except, they are included
in classes because they have some sort of logical connections with the class. Usually in static methods,
we do not access the instance or the class anywhere with the scope of the static method.

"""
import datetime
from datetime import datetime

from dateutil import parser
import dateutil, pytz

#
# def employee_number():
#     return Employee.num_of_emps
#

class Employee:
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{self.first}.{self.last}@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first}{self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_data_str(cls, emp_data):
        for value in emp_data:
            first_val, last_val, pay_val = value.split('-')
            yield cls(first_val, last_val, float(pay_val))

    @classmethod
    def from_string(cls, emp_str):
        first_, last_, pay_val_ = emp_str.split('-')
        return cls(first_, last_, pay_val_)

    @staticmethod
    def is_workday(dt):
        dt_datetime = parser.parse(dt, fuzzy_with_tokens=False, dayfirst=True).isoweekday()
        print(dt_datetime)
        if dt_datetime == 5 or dt_datetime == 6:
            return False
        return True


dev_1 = Employee('Corey', 'Schafer', 50000)
dev_2 = Employee('Test', 'User', 60000)
print(dev_1.email)
print(dev_2.email)

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)

# my_data = [emp_str_1, emp_str_2, emp_str_3]

# Employee.from_string(my_data)
#
# for item in Employee.from_data_str(my_data):
#     print(item.first, item.last, item.pay, item.email)
#
# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)

# print(Employee.is_workday('2016, 7, 11'))
