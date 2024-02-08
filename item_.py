import csv


class Item:
    pay_rate = 0.8  # pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity: float = 0):
        # Run validations to received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        # Assign to self object
        self._name = name
        self.__price = price
        self.__quantity = quantity

        # Actions to execute:
        Item.all.append(self)

        # with open('items.csv', 'w', newline='') as csv_file:
        #     csv_writer = csv.writer(csv_file)
        #     csv_writer.writerow(['name', 'price', 'quantity'])
        #
        #     for item in Item.all:
        #         csv_writer.writerow([item.name, item.price, item.quantity])

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self._name

    @name.setter
    def set_name(self, value):
        self._name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price *= self.pay_rate
        # Item.pay_rate because pay_rate is a class level attribute
        # self.pay_rate allows you to access pay_rate from the instance level
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        # cls stands for class since this is a class method.
        with open('items.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            header = next(reader)
            items = list(reader)
        #
        # for item in items:
        #     yield item
        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                quantity=float(item['quantity'])
            )

    @staticmethod
    def is_int_value(num):
        #     We will count out float thay are point zeroe.g 5.0, 10.0
        if isinstance(num, float):
            # count out floats that are point zero
            return num.is_integer()
        # is_integer() is a method is a built-in method of the float class in Python. It returns True
        # if the float object has an integral value, that is, if it has no fractional part.
        # For example, 5.0.is_integer() returns True, but 5.5.is_integer() returns False.

        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.__class__.__name__}:'{self.name}', price:{self.price}, quantity:{self.quantity})"

    @name.setter
    def name(self, value):
        self._name = value

