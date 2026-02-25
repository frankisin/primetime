from collections import defaultdict
def topKFrequent(nums,k):
    freq = defaultdict(int)
    res = []
    
    for num in nums:
        freq[num] += 1
    
    sort_freq = sorted(freq.items(),key = lambda x:x[1],reverse=True) # sort by values descending
    
    for i in range(k):
        res.append(sort_freq[i][0])
    
    return res
        
        
    
        
    
    