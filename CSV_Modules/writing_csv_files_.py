
# How to write CSV Files

"""
            WRITING CSV FILES:
--> This is the reverse of reading and parsing a csv file.
--> Given some data, write it out to a csv file.

--> The data should be an iterable of rows, and each row itself should be an iterable of fields (columns),
i.e, the data should be an iterable containing iterables of fields.
--> Just like when we read a CSV file, we can specify the formatting options for how we want to output the data.
    --> By using individual values (delimiter, quotechar, etc)
    --> or using a dialect (built-in or custom)
--> Unless there are reasons not to, just use the standard excel dialect.

            CVS WRITE: csv.writer
--> The csv.writer method allows use to write csv files.
    --> It has attributes like .writerow() method to write each row in the data
    --> If you want a header row, write it out using writerow and an iterable of headers.


"""
import csv

# data = "test.csv"
#
# with open(data) as f:
#     data = csv.reader(f)
#     result = []
#     for row in data:
#         row[0] = row[0].replace('\\', '').split('|')
#         row[1:] = (field.replace('\\', '') for field in row[1:])
#         result = [each for each in row[0]] + [','.s(row[1:])]
#         print(result)


data = [
    ['First Name', 'Last Name', 'DOB', 'Sketches', ''],
    ['John', 'Cleese', '10/27/39', "The Cheese Shop, \"Ministry of Silly Walks, It\'s the Arts"],
    ['Eric', 'Idle', '3/29/43', 'The Cheese Shop, Nudge Nudge, "Spam"'],
    ['Peter', "O'Toole", '8/2/32', 'Lawrence | of | Arabia']
]


with open('test.csv', 'w') as f:
    writer = csv.writer(f)

    for row in data:
        writer.writerow(row)


with open('test.csv') as f:
    for row in f:
        print(row, end='')


csv.register_dialect(
    'pdv', delimiter='|', quotechar="'", escapechar='\\', doublequote=False
)

with open('test.csv', 'w') as f:
    writer = csv.writer(f, dialect='pdv')

    for row in data:
        writer.writerow(row)

with open('test.csv') as f:
    for row in f:
        print(row, end='')













