#Reverse and string using stack


def reverse_string(s):
    stack = []
    for char in s:
        stack.append(char)
    
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    
    return reversed_str

string = "Python"
print(reverse_string(string))  
