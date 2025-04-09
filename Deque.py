from collections import deque

def check_palindrome(word):
    cleaned = ''.join(word.lower().split()) 
    d = deque(cleaned)
    
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Test 
print('Madam:', check_palindrome("Madam"))           
print('Python:', check_palindrome("Python"))         
print('A Santa at NASA:', check_palindrome("A Santa at NASA")) 
