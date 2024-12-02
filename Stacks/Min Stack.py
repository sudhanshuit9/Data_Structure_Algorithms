#Design a stack that supports retrieving the minimum element in constant time.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if self.stack:
            if self.stack.pop() == self.min_stack[-1]:
                self.min_stack.pop()
    
    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None


min_stack = MinStack()
min_stack.push(3)
min_stack.push(5)
print(min_stack.get_min())  
min_stack.push(2)
min_stack.push(1)
print(min_stack.get_min())  
min_stack.pop()
print(min_stack.get_min())  
