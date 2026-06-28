def canJump(nums)->bool:
    farthest = 0 
    last = len(nums) - 1
    
    for i,num in nums:
        #base case, determin if we have seen enough jumps to survive this i.
        if i > farthest:
            return False 
        
        farthest = max(farthest,num + i) #[2,3,1,1,4] i = 1 nums[i] = 3 nums[i] + i
        
        if farthest >= last:
            return True 