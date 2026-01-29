from collections import deque 

def removeStars(string:str):
    stack = deque()
    ans = []

    for ch in string:
        if ch == "*":
            stack.pop()
        else:
            stack.append(ch)
    while stack:
        char = stack.popleft()
        ans.append(char)
    return "".join(ans) 
    
string = "aannnddd**"

print(removeStars(string))
