def minimumRemovalValidParenthesis(s:str)->str:
    res = []
    remove = set()
    stack = []

    for i,char in enumerate(s):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if len(stack) == 0:
                remove.add(i)
            else:
                stack.pop()
    
    while stack:
        remove.add(stack.pop())
    
    for i,char in enumerate(s):
        if i not in remove:
            res.append(char)
    
    return "".join(res)