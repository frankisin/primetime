def validPalindrome(nums):
    def isPal(l,r):
        while l < r:
            if nums[l] == nums[r]:
                l += 1
                r -= 1
            else:
                return False
        return True 
    
    l = 0 
    r = len(nums) - 1
    
    while l < r:
        if nums[l] == nums[r]:
            l+= 1
            r-=1
        else:
            return isPal(l+1,r) or isPal(l,r-1)
        
    return True 