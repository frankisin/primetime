def longestPalindromicSub(s):
    longestSub = []

    def substring(s):
        substrings = []
        for i in range(len(s) + 1):
            for j in range(i):
                sub = s[j:i]
                substrings.append(sub)
        return substrings
    
    def isPalindrome(s):
        if len(s) == 0:
            return False
        mid = int(len(s) // 2)

        for i in range(0,mid):
            if s[i] != s[len(s)-i-1]:
                return False
        return True 
    
    subs = substring(s)

    for sub in subs:
        if isPalindrome(sub):
            if len(sub) > len(longestSub):
                longestSub = sub
    return longestSub




