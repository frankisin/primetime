def validPalindrome(s:str):
    if len(s) < 1:
        return False 
    
    def isValid(s,l,r):
        while l < r:
            if s[l] != s[r]:
                return False 
            l += 1
            r -= 1
        return True 
    
    left = 0 
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return isValid(s,left+1,right) or isValid(s,left,right-1)
        left += 1
        right -= 1 
    return True 
    
