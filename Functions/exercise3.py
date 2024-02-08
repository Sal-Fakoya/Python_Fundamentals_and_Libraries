data = [
    ('item1', 'manuf-1', 10, 100.0, 0.2),
    ('item2', 'manuf-2', 5, 25.0, 0),
    ('item3', 'manuf-3', 100, 0.25, 0.025)
]

schema = ('widget', 'manufacturer', 'num_sold', 'unit_price', 'discount')

my_dict = {
    row[0]: dict(zip(schema[1:], (each_one for each in data for index, each_one in enumerate(each) if index > 0)))
    for row in data
}
print(my_dict)

my_dict = {
    row[0]: dict(zip(schema[1:], (each_one for index, each_one in enumerate(row) if index > 0)))
    for row in data
}
print(my_dict)

my_dict = {row[0]: dict(zip(schema[1:], row[1:])) for row in data}
print(my_dict)

