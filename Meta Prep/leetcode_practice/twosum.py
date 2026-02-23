from collections import defaultdict
def twosum(nums,target):
    d = {} # int : index

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in d:
            return [d[complement],i]
        
        d[nums[i]] = i 

    return [-1,-1]
    
