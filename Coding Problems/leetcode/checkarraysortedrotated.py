def check(nums):
    #[1,2,3,0] -> nums[i] > nums[i+1]
    n = len(nums)
    
    drops = 0
    
    for i in range(n):
        if nums[i] > nums[(i+1) % n]:
            drops += 1
            if drops > 1:
                return False 
    return True 