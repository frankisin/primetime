def generateParenthesis(n:int):
    res = []

    def backtrack(closed_used,open_used,path):
        if open_used == n and closed_used == n:
            res.append("".join(path))
            return
        
        if open_used < n: 
            path.append("(")
            backtrack(closed_used,open_used+1,path)
            path.pop()
        
        if closed_used < open_used:
            path.append(")")
            backtrack(closed_used + 1,open_used,path)
            path.pop()
    backtrack(0,0,[])
    return res
        

