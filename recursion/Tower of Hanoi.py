# The Tower of Hanoi is a puzzle where you need to move a set of disks from one peg to another, using a third peg, under the following constraints:

#Only one disk can be moved at a time.
#A disk can only be moved to the top of a peg if it is smaller than the disk already on that peg.

def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Example
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
