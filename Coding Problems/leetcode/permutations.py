class Solution:
    def permute(self,nums:list[int])->list[list[int]]:
        if not nums:
            return []
        
        self.res = []
        n = len(nums)
        used = [False] * (n) # generate array of size n, initialize as False
        self.backtrack(nums,used,[])
        
        return self.res
        
       
    def backtrack(self,nums,used,curr):
        if len(curr) == len(nums):
            self.res.append(curr.copy())
            return 
        
        for i in range(len(nums)):
            if used[i]:
                continue
            
            used[i] = True
            
            curr.append(nums[i])
            
            self.backtrack(nums,used,curr)
            
            curr.pop()
            
            used[i] = False
            
                                      
nums = [1,2,3]

sol = Solution()

print(sol.permute(nums))

      
        
        
        
        