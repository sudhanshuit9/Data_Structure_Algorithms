#  Given a string s and a pattern p containing '*' (matches any sequence) and '?' (matches any single character), determine if p matches s

def isMatch(s, p):
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    
    # Base cases
    dp[0][0] = True  # Empty pattern matches empty string
    
    # Fill the first row where pattern can be '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == s[i - 1] or p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
    
    return dp[m][n]

s1, p1 = "aa", "a"
print(isMatch(s1, p1))

s2, p2 = "aa", "*"
print(isMatch(s2, p2))

s3, p3 = "cb", "?a"
print(isMatch(s3, p3)) 

s4, p4 = "adceb", "*a*b"
print(isMatch(s4, p4))  

s5, p5 = "acdcb", "a*c?b"
print(isMatch(s5, p5))