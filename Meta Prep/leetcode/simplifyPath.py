def simplifyPath(path:str)->str:
    stack = []
    
    path_items = path.split("/")
    
    for item in path_items:
        if item == "." or not item:
            continue 
        elif item == "..":
            stack.pop()
        else:
            stack.append(item)
    
    return "/" + "/".join(stack)