from collections import defaultdict
def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    d = defaultdict(list)
    
    for i in range(len(nums)):
        d[nums[i]].append(i)
        
    for indices in d.values():
        for j in range(len(indices) - 1):
            if abs(indices[j] - indices[j+1]) <= k:
                return True 
    
    return False 