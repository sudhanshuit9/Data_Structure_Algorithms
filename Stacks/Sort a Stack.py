#Sort a stack in ascending order using recursion (without additional data structures).

def sorted_insert(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        sorted_insert(stack, element)
        stack.append(temp)

def sort_stack(stack):
    if stack:
        temp = stack.pop()
        sort_stack(stack)
        sorted_insert(stack, temp)


stack = [30, -5, 18, 14, -3]
sort_stack(stack)
print(stack) 