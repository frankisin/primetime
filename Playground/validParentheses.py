from collections import deque
def validParentheses(string):
    brackets = {
        '}' : '{',
        ')'  : '(',
        ']' : '['
    }

    stack = deque()

    for char in string:
        if char == '{' or char == '[' or char == '(':
            stack.append(char)
        elif char in brackets:
            if len(stack) == 0:
                return False 

            bracket = stack.pop()

            if bracket == brackets[char]:
                continue
            else:
                return False 
    return len(stack) == 0
            






            
