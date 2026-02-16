from collections import defaultdict
def twosum(nums,target):
    d = defaultdict(int)

    for i,num in enumerate(nums):
        complement = target - num

        if complement in d:
            return [d[complement],i]
        else:
            d[num] = i 
    return []
    


