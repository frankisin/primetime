def jumpGame(nums):
    n = len(nums)
    
    best = 0 
    
    for i in range(n):
        if best < i:
            return False 
        
        best = max(best,i + nums[i]) 
        
        if best >= n - 1:
            return True 
    return True 
    
    