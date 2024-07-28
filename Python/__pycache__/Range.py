def print_even_and_squares(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            print(f"Number: {num}, Square: {num**2}")

# (a) Range 1 to 50
print("Even numbers and their squares within the range 1 to 50:")
print_even_and_squares(1, 50)
print("\n")

# (b) Range 1 to 100
print("Even numbers and their squares within the range 1 to 100:")
print_even_and_squares(1, 100)
