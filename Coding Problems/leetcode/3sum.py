def threeSum(nums):
    nums.sort()
    res = []
    n = len(nums)
    
    for i in range(n-2): #n-2 since theres always two numbers ahead of i...
        #base cases
        if i > 0 and nums[i] == nums[i-1]: #only allow the first occurence of a value to behave as anchor...
            continue 
        
        if nums[i] > 0: # if value at anchor is positive, the proceeding values canot possibly be zero (sorted array)
            break 
        
        l = i + 1
        r = n - 1
        
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else: 
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1
            
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1
    return res 
        
    
    