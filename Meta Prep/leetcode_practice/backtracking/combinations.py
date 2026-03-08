def combinations(n,k):
    if n == 0 or k > n:
        return []
    if k == 0:
        return [[]]
    
    res = []
    
    def backtrack(n,k,idx,curr):
        if len(curr) == k:
            res.append(curr.copy())
        else:
            for i in range(idx,n+1):
                curr.append(i)
                backtrack(n,k,i+1,curr)
                curr.pop()
    
    backtrack(n,k,1,[])
    return res

