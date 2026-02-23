def longestBalanced(self, s) -> int:
    n = len(s)
    best = 0 
    
    for i in range(n):
        freq = [0] * 26
        
        for j in range(i,n):
            freq[ord(s[j])-ord('a')] += 1
            
            mn = float('inf')
            mx = 0 
            distinct = 0 
            
            for c in freq:
                if c > 0:
                    distinct += 1
                    if c < mn:
                        mn = c
                    if c > mx:
                        mx = c
            
            if distinct > 0 and mn == mx:
                best = max(best,j-i+1)
    return best 