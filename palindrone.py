def JavaIsPalindrome(s): 
  
    for i in range(0, int(len(s)/2)):  
        if s[i] != s[len(s)-i-1]: 
            return False
    return True
  
def python_is_palindrome(s):
    return s == s[::-1]
        
s = "kamilslimak"

if python_is_palindrome(s): 
    print("Yes :)") 
else: 
    print("No :(") 