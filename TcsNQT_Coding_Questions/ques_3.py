#Check if a string is a palindrome.
def is_palindrome(s):
    return s == s[::-1]
#check if a string is palindrome
print(is_palindrome("radar"))

print(is_palindrome("radar"))



#using two pointer
def is_palindrome(s):
    Left = 0
    Right = len(s)-1
    while Left < Right:
        if s[Left]!= s[Right]:
            return False
        Left += 1
        Right -= 1
        return True
    print(is_palindrome("radar"))
