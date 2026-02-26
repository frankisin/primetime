def validPalindrome(string:str):
    def isPalindrome(l,r):
        while l < r:
            if string[l] != string[r]:
                return False
            else:
                l += 1
                r -= 1
        
    l,r = 0,len(string)-1
    
    while l < r:
        if string[l] != string[r]:
            return isPalindrome(l+1,r) or isPalindrome(l,r-1)
        else:
            l += 1
            r -= 1
    return True 
        