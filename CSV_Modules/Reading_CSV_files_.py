"""
                        READING CSV FILES: using the CSV module
--> CSV stands for comma-separated values
--> It is a format for tabular data
    --> Each row in a file is a row of data
    --> Each row in the file are separated by a newline (OS Specific)
    --> Each field in the row is separated by a separator (or delimiter)
--> The separator can be a comma, a pipe, or any character
--> CSV is not a standard format. A variety of csv files exist, called dialects.
--> Examples of CSV files are
    --> Most common one is Excel:
        --> delimiter (field separator) is comma (,)
        --> quotechar (field delimiter) is quotes "
        --> Excel doubles quortechar if found inside a field
        --> It only uses quotechar of delimiter is found inside is field
    -->

                            PARSING CSV DATA: csv.reader(f, delimiter=",", quotechar='"')
--> The default parser dialect is excel
    --> but we can specify custom settings for delimiter, quotechar, etc

--> e.g csv.reader(f, delimiter=",", quotechar='"') where:
        --> f is the file to read from
        --> delimiter is an optional keyword argument that defaults to ,
        --> quotechar = '"' defaults to "

--> csv.reader() returns an iterator of parsed rows over the file
"""

with open("actors.csv") as f:
    for row in f:
        print(row)

with open("actors.csv") as f:
    for row in f:
        row = row.strip()
        fields = row.split(',')
        print(fields)

import csv
with open("actors.csv") as f:
    reader = csv.reader(f, delimiter=",", quotechar='"')
    for row in reader:
        print(row)