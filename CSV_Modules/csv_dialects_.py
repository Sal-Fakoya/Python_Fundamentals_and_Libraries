"""
                                CREATING AND USING A DEFINED DIALECT
--> It is tedious to type the same settings often because it is error-prone hence we can bundle up all the settings
    into a custom dialect.

--> The CSV module comes with some pre-defined dialects, like excel whose pre-defined dialect is excel tab

--> We can add a dialect with:
    --> a name for the dialect
    --> values for the delimiter, quotechar, etc

--> csv.register_dialect("<name>", delimeter=, quotechar="")
--> The registered dialect is re-run at the beginning of the program somewhere and re-used.

                        USING A DEFINED DIALECT
--> We can specify dialect instead of default values for csv.reader
    --> e.g csv.reader(f, dialect="excel"), where excel is the default for dialect
    --> e.g csv.reader(f, dialect = "my-custom-dialect")

"""

import csv

print(csv.list_dialects())

source_file = "actors.pdv"

with open(source_file, 'r') as f:
    for row in f:
        print(row.strip())

with open(source_file, 'r') as f:
    reader = csv.reader(f, delimiter="|", quotechar="'", escapechar="\\", skipinitialspace=True)
    for row in reader:
        print(row)


csv.register_dialect('pdv', delimiter="|", quotechar="'", escapechar="\\", skipinitialspace=True)

print(csv.list_dialects())

with open("actors.pdv") as f:
    reader = csv.reader(f, dialect='pdv')
    for row in reader:
        print(row)










