from collections import defaultdict
def topKFrequent(nums,k):
    freq = defaultdict(int)
    res = []

    for num in nums:
        freq[num] += 1
    
    sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)

    for i in range(k):
        res.append(sorted_freq[i][0])
    
    return res 
