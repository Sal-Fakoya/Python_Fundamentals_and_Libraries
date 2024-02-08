# for row in range(1, 5):
#     for col in range(0, row):
#         print('* ', end='')
#     print()

count = 6
for row in range(1,10,2):
    count -= 1
    print('\t' * count, end='')
    for col in range(0,row):
        print(f'*'*col, end='')
    print()



