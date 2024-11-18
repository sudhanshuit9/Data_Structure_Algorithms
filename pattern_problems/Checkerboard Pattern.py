# Print a checkerboard pattern of size n x n.

n = 4
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print('*', end=" ")
        else:
            print(' ', end=" ")
    print() 
