import module_ListFunction as mlf

# List of the first 10 natural numbers
list1 = [i for i in range(1, 11)]

# List of the first 10 even numbers
list2 = [i for i in range(2, 21, 2)]

# List of the first 10 odd numbers
list3 = [i for i in range(1, 20, 2)]

# List of squares of the first 10 natural numbers
list4 = [i**2 for i in range(1, 11)]

# List of cubes of the first 10 natural numbers
list5 = [i**3 for i in range(1, 11)]

lists = [list1, list2, list3, list4, list5]
list_names = ['list1', 'list2', 'list3', 'list4', 'list5']

for name, lst in zip(list_names, lists):
    print(f"{name} = {lst}")
    print(f"Maximum value in {name}: {mlf.find_max(lst)}")
    print(f"Minimum value in {name}: {mlf.find_min(lst)}")
    print(f"Sum of elements in {name}: {mlf.calculate_sum(lst)}")
    print(f"Average of {name}: {mlf.compute_average(lst)}")
    print(f"Median of {name}: {mlf.determine_median(lst)}")
    print("-" * 40)
