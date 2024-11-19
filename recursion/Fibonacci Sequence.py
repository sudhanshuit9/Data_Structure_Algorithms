#The Fibonacci sequence is a series where each number is the sum of the two preceding ones, starting from 0 and 1. The sequence is: 0, 1, 1, 2, 3, 5, 8, 13, ...

# Recursive Approaches
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = 10
print(f"Fibonacci sequence (Recursive) up to {n}:", [fibonacci_recursive(i) for i in range(n)])



#iterative recursion
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example
n = 10
print(f"Fibonacci sequence (Recursive) up to {n}:", [fibonacci_recursive(i) for i in range(n)])
