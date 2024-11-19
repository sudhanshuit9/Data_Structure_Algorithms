#The factorial of a non-negative integer n is the product of all positive integers less than or equal to n. It is denoted as n!

def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

# Example
n = 5
print(f"Factorial of {n} (Recursive):", factorial_recursive(n))
