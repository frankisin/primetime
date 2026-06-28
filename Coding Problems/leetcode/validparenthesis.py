from collections import deque

def isValid(s):
    brackets = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    
    q = deque()
    
    for char in s:
        if char == '{' or char == '[' or char == '(':
            q.append(char)
        else:
            if len(q) == 0:
                return False 
            
            bracket = q.pop()
            
            if brackets[bracket] == char:
                continue
            else:
                return False
    return len(q) == 0
            