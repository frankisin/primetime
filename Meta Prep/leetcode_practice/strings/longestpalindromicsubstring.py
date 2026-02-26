def longestPalindromicSub(s:str):
    best_left = best_right = 0 
    
    def expand(l,r):
        nonlocal best_left,best_right
        
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l > best_right - best_left:
                best_right = r
                best_left = l
                
            l -= 1
            r += 1
        
    for i in range(len(s)):
        expand(i,i)
        expand(i,i+1)
        
    return s[best_left:best_right+1]
    
        
        
    