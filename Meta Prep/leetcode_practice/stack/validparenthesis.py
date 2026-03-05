def validParenthesis(string:str)->bool:
    stack = []

    for ch in string:
        if ch == "(":
            stack.append(ch)
        elif ch == ")":
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0 