# Given a string, find the number of palindromic substrings in it.

def countSubstrings(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
    
    result = 0
    for i in range(len(s)):
        # Odd length palindromes (center is at i)
        result += expand_around_center(i, i)
        # Even length palindromes (center is between i and i+1)
        result += expand_around_center(i, i + 1)
    
    return result

s1 = "abc"
print(countSubstrings(s1))