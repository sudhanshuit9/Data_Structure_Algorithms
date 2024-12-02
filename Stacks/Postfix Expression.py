#Evaluate a postfix (Reverse Polish) expression.

def evaluate_postfix(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for char in expression.split():
        if char not in operators:
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(int(a / b))  # Ensure integer division

    return stack[-1]

# Example Usage
expression = "5 1 2 + 4 * + 3 -"
print(evaluate_postfix(expression))  # Output: 14
