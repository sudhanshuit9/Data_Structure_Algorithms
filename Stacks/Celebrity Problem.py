#In a party, a "celebrity" is a person who is known by everyone but knows no one. Identify the celebrity using a stack.

def find_celebrity(matrix):
    n = len(matrix)
    stack = [i for i in range(n)]

    # Step 1: Find a potential celebrity
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if matrix[a][b]:
            stack.append(b)
        else:
            stack.append(a)

    # Step 2: Verify the potential celebrity
    if not stack:
        return -1
    celeb = stack.pop()
    if all(matrix[i][celeb] for i in range(n) if i != celeb) and all(not matrix[celeb][i] for i in range(n)):
        return celeb
    return -1

# Example Usage
matrix = [
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
]
print(find_celebrity(matrix))  # Output: 2 (Celebrity index)
