#the goal of this problem is to use a stack to track valid parenthesis 
#and to use a set to track valid indices.
def minRemoveToMakeValid(s):
    stack = [] #valid parathesis 
    remove = set() #removal indices 
    output = []

    for i,char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if len(stack) == 0:
                remove.add(i)
            else:
                stack.pop()
    
    while stack:
        remove.add(stack.pop())

    for i in range(len(s)):
        if i not in remove:
            output.append(s[i])
    
    return "".join(output)

