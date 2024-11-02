#write a program to find the function to check if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    # If lengths are not equal, they cannot be anagrams
    if len(str1) != len(str2):
        return False
    
    # Sort both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "listen"
string2 = "silent"
print("Are anagrams:", are_anagrams(string1, string2))  # Output: True
