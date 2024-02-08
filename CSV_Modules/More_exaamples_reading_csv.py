"""


"""
import csv

nasdaq = "nasdaq.csv"

with open(nasdaq) as f:
    for _ in range(5):
        row = next(f)
        print(row)

with open(nasdaq) as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


def parse_nasdaq(f_name):
    result = []

    with open(f_name) as f:
        reader = csv.reader(f)

        headers = next(reader)
        result.append(headers)

        for row in reader:
            row[-1] = float(row[-1])
            result.append(row)

    return result


print(parse_nasdaq(nasdaq))

census = "st-2001est-01.csv"

with open(census) as f:
    for _ in range(10):
        print(next(f))

with open(census) as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

def parse_census_data(file_name):
    results = []

    with open(census) as f:
        reader = csv.reader(f)

        headers = next(reader)
        results.append(headers)

        for row in reader:
            area = row[0]
            data = row[1:]
            data = [area] + [int(field.replace(',', '')) for field in data]
            results.append(data)

    return results


print(parse_census_data(census))








# with open(nasdaq) as f:
#     for _ in range(5):
#         row = next(f)
#         print(row)
#
# import csv
#
# print(csv.list_dialects())
# with open(nasdaq) as f:
#     reader = csv.reader(f, dialect="excel")
#     for row in reader:
#         print(row)
#
# def parse_nasdaq(f_name):
#     result = []
#
#     with open(f_name) as f:
#         read_er = csv.reader(f, dialect='excel')
#         headers = next(read_er)
#         result.append(headers)
#
#         for each_row in read_er:
#             each_row[-1] = float(each_row[-1])
#             result.append(each_row)
#         return result
#
#
# print(parse_nasdaq(nasdaq))
#
# census = 'st-2001est-01.csv'
#
# with open(census) as f:
#     for _ in range(10):
#         print(next(f))
#
#
# #
# # def parse_reader(f_name):
# #     with open(census) as f:
# #         new_f = []
# #         for n_row in f:
# #             head_er = next(f)
# #             new_f = n_row.strip()
# #
# #         for n_row in f[1:]:
# #             n_row = float()
# #         read_er = csv.reader(new_f, dialect='excel')
# #
