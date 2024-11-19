# A Fibonacci Heap is an advanced heap that supports efficient decrease-key and merge operations. Its implementation is more complex, but here’s a simplified version for demonstration.
class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.total_nodes = 0

    def insert(self, key):
        node = FibonacciHeapNode(key)
        if not self.min:
            self.min = node
        else:
            self._merge_nodes(self.min, node)
            if key < self.min.key:
                self.min = node
        self.total_nodes += 1
        return node

    def get_min(self):
        return self.min.key if self.min else None

    def _merge_nodes(self, a, b):
        # Merge two nodes into a circular doubly linked list
        a.right.left = b.left
        b.left.right = a.right
        a.right = b
        b.left = a

# Example usage
fib_heap = FibonacciHeap()
fib_heap.insert(10)
fib_heap.insert(5)
fib_heap.insert(20)
print("Minimum Element:", fib_heap.get_min())
