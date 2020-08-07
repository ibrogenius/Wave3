limit = 40
square_numbers = 1
while (square_numbers + 1) ** 2 < limit:
    square_numbers += 1
nearest_square = square_numbers ** 2

print(nearest_square)