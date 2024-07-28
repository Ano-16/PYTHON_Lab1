my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# (a) Sum all the items of the list
def sum_of_list(lst):
    return sum(lst)

# (b) Multiply all the items of the list
def multiply_list(lst):
    result = 1
    for item in lst:
        result *= item
    return result

# (c) Get the largest number from the list
def get_max(lst):
    return max(lst)

# (d) Get the smallest number from the list
def get_min(lst):
    return min(lst)

print(f"Sum of all items in the list: {sum_of_list(my_list)}")
print(f"Product of all items in the list: {multiply_list(my_list)}")
print(f"Largest number in the list: {get_max(my_list)}")
print(f"Smallest number in the list: {get_min(my_list)}")
