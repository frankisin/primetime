from collections import deque
def validParentheses(string):
    stack = deque()

    brackets = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    for char in string:
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        elif char in brackets:
            if len(stack) == 0:
                return False #invalid

            bracket = stack.pop()

            if bracket == brackets[char]:
                continue
            else:
                return False
            
    return len(stack) == 0


        
        
