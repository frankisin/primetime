def palindromicSubstring(s):
    
    count = 0

    def expand(left,right):
        nonlocal count 

        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1 
            count += 1
        
    for i in range(len(s)):
        expand(i,i) #odd length
        expand(i,i+1) #even length


    def substring(string):
        subs = []

        for i in range(len(string) + 1):
            for j in range(i):
                subs.append(string[j:i])
        return subs 
    
    def isPalindrome(substring):
        left = 0 
        right = len(substring) -1

        if len(substring) < 2:
            return True 
        
        while left < right:
            if substring[left] != substring[right]:
                return False
            
            left += 1
            right -= 1
        return True

    substrings = substring(s) # returns an array of subs

    for sub in substrings:
        if isPalindrome(sub):
            count += 1
    return count 

