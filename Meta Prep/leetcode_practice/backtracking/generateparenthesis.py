def generateParenthesis(n:int):
    res = []

    def backtrack(open_used,closed_used,curr):
        if open_used == n and closed_used == n:
            res.append("".join(curr))
            return 
        if open_used < n:
            curr.append("(")
            backtrack(open_used+1,closed_used,curr)
            curr.pop()
        if closed_used < n:
            curr.append(")")
            backtrack(open_used,closed_used+1,curr)
            curr.pop()
    
    backtrack(0,0,[])
    return res 