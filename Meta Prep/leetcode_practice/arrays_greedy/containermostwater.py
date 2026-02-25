def containerMostWater(nums):
    n = len(nums)
    maxwater = 0
    
    l = 0 
    r = n - 1
    
    while l < r:
        lheight = nums[l]
        rheight = nums[r]
        
        minVolume = min(lheight,rheight) * (r-l)
        
        maxwater = max(maxwater,minVolume)
        
        if lheight < rheight:
            l += 1
        else:
            r -= 1 
    return maxwater