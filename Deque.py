from collections import deque

def check_palindrome(word):
    d = deque()
    for letter in word:
        d.append(letter.lower())  

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

# Test 
print('Madam:', check_palindrome("Madam"))
print('Python:', check_palindrome("Python"))    