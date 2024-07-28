# Given list
A = ['abc', 'xyz', 'aba', '1221']

# Function to find and print strings with identical first and last characters
def print_identical_first_last(lst):
    for index, string in enumerate(lst):
        if string[0] == string[-1]:
            print(f"String: '{string}' at Index: {index}")

print_identical_first_last(A)
