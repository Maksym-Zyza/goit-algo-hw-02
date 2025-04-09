class Stack:
  def __init__(self):
    self.stack = []

  # ADD
  def push(self, item):
    self.stack.append(item)

  # DELETE
  def pop(self):
    if len(self.stack) < 1:
      return None
    return self.stack.pop()

  # IS_EMPTY
  def is_empty(self):
    return len(self.stack) == 0
  
def check_brackets(string):
  stack = Stack()
  for char in string:
    if char in '([{':
      stack.push(char)
    elif char in ')]}':
      if stack.is_empty():
        return False
      top = stack.pop()
      if (
        (char == ')' and top != '(') or
        (char == ']' and top != '[') or
        (char == '}' and top != '{')
         ):
        return False
  return stack.is_empty()

#Test
print(check_brackets("( ){[ 1 ]( 1 + 3 )( ){ }}")) 
print(check_brackets("( 23 ( 2 - 3)")) 
print(check_brackets("( 11 }")) 