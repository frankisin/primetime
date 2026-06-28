def longestPalindromicSub(s):
    best_left = best_right = 0 

    def expand(left,right):
        nonlocal best_left,best_right

        while left >= 0 and right < len(s) and s[left] == s[right]:
            #update best before moving 
            if right - left > best_right - best_left:
                best_right = right
                best_left = left
            left -= 1
            right += 1
    
    for i in range(len(s)):
        expand(i,i)
        expand(i,i+1)
    return [s[best_left:best_right+1]]