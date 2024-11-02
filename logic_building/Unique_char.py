#w
def has_unique_characters(s):
    
    seen_chars = set()
    
    for char in s:
     
        if char in seen_chars:
            return False
        seen_chars.add(char)
    
    return True

string = "hello"
print("Has all unique characters:", has_unique_characters(string))  

string = "world"
print("Has all unique characters:", has_unique_characters(string))