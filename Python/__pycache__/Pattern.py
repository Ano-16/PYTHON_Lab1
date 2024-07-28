def alphabet_pyramid(n):
    for i in range(1, n + 1):
        for j in range(i):
            print(chr(65 + j), end="")
        print()

# Number of rows for the pattern
n = 5
alphabet_pyramid(n)

print("\n")

def star_pyramid(n):
    for i in range(1, n + 1):
        print('*' * i)

# Number of rows for the pattern
n = 5
star_pyramid(n)
