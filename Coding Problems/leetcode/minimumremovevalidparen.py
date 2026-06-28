def minRemoveToMakeValid(s: str) -> str:
    stack = [] #
    remove = set() # store indices of chars to be removed...
    clean = []
    
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i) # append index to the stack
        elif s[i] == ')':
            if len(stack) == 0:
                remove.add(i)
            else:
                stack.pop()
    while stack:
        remove.add(stack.pop())
    
    for i in range(len(s)):
        if i not in remove:
            clean.append(s[i])
    return "".join(clean)
    
        

