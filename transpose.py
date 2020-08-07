data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))
data_transpose = map(tuple, zip(*data))
for item in data_transpose:
    print(list(item))
print(data_transpose)