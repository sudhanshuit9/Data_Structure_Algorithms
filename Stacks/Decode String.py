#Decode a string encoded with patterns like 3[a2[b]].
def decode_string(s):
    stack = []
    current_string = ""
    current_number = 0

    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_number))
            current_string, current_number = "", 0
        elif char == ']':
            prev_string, number = stack.pop()
            current_string = prev_string + current_string * number
        else:
            current_string += char

    return current_string


encoded = "3[a2[b]]"
print(decode_string(encoded))  