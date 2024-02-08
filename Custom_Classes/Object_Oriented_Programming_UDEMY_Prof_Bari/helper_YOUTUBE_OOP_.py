# When to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_int_value(num):
        """
        This should do something that has a relationship with the class,
        but not something that must be unique per
        instance. They do not pass the class or instance as parameter.
        """

    @classmethod
    def instantiate_from_something(cls):
        """
        This should do something that has a relationship with the class,
        but usually, those are used to manipulate
        different structures of data to instantiate objects,
        like we have done with CSV. You can also use it to instantiate
        from JSON file, yaml file, or other data.
        """


#  Class methods and static methods can be called from class
#  levels and from instance levels.

item1 = Item()
print(item1.is_int_value(5))
print(item1.instantiate_from_something())

Item.is_int_value(10)
Item.instantiate_from_something()
