# Permutations
#The number of permutations of n items taken r at a time is given by:
import math

def permutations(n, r):
    return math.perm(n, r)

# Example
n = 5
r = 3
print(f"Permutations of {n} taken {r} at a time:", permutations(n, r))


#The number of combinations of n items taken r at a time is given by:
import math

def combinations(n, r):
    return math.comb(n, r)

# Example
n = 5
r = 3
print(f"Combinations of {n} taken {r} at a time:", combinations(n, r))
