from collections import defaultdict
def containsNearbyDuplicate(nums,k)->bool:
    freq = defaultdict(list) # nums[i] : [indices]
    n = len(nums)
    
    for i in range(n):
        freq[nums[i]].append(i) 
        
    for indices in freq.values():
        for j in range(len(indices)-1):
            if indices[j+1] - indices[j] <= k:
                return True 
    return False 
            
    
    