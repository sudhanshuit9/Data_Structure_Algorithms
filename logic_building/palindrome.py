# Write a function to check if a given string is a palindrome (reads the same forward and backward)
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]
String = "Madam"
print ("Is palindrome", is_palindrome(String))