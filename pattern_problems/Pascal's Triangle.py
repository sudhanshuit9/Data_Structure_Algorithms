# print pascal's triangle

n = 5  # Number of rows
for i in range(n):
    # Print spaces for alignment
    print(' ' * (n - i - 1), end="")
    # Compute coefficients
    num = 1
    for j in range(i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j + 1)
    print()
