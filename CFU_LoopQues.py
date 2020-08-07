check_prime = [26, 39, 51, 53, 57, 79, 85]
for number in check_prime:
    for num in range(2, number):
        if number % num == 0:
            print(f"{number} is NOT a PRIME NUMBER, and a factor of that number, other than 1 and the number itself is: {num} is a factor of {number}")
            break
        if num == number - 1:
            print(f"{number} is a Prime Number")