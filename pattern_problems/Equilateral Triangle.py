# Print an equilateral triangle of stars.

n = 7

for i in range(1, n + 1):

    print(' ' * (n - i) + '*' * (2 * i - 1))
