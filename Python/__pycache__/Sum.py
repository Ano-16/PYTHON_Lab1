def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

def reverse_number(number):
    return int(str(number)[::-1])

number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:
    digits_sum = sum_of_digits(number)
    print(f"Sum of digits: {digits_sum}")
    
    reversed_number = reverse_number(number)
    print(f"Reversed number: {reversed_number}")
else:
    print("Please enter a valid four-digit number.")
