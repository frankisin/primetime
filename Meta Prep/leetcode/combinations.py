class Solution:
    def combine(self, n: int, k: int):
        if not n or not k:
            return
        
        self.res = []
        
        self.backtrack(n,k,1,[])
        
        return self.res
        
    def backtrack(self,n,k,idx,curr):
        if len(curr) == k:
            self.res.append(curr.copy())
            return 
        
        
        for i in range(idx,n+1):
            curr.append(i)
            self.backtrack(n,k,i+1,curr)
            curr.pop()
            
        