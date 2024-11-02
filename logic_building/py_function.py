#Write a Python function that takes a positive integer as input and returns the sum of its digits.
def sum_of_digits(number):

    return sum(int(digit) for digit in str(number))

number = 123
print("Sum of digits:", sum_of_digits(number))