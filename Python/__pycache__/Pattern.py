def alphabet_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces to center the row
        for k in range(n - i):
            print(" ", end="")
        # Print alphabets
        for j in range(i):
            print(chr(65 + j), end=" ")
        print()

n = 5
alphabet_pyramid(n)

print("\n")

def star_pyramid(n):
    for i in range(1, n + 1):
        
        for k in range(n - i):
            print(" ", end="")
        
        print('*' * (2 * i - 1))


n = 5
star_pyramid(n)
