
def twoSum(nums,target):
    hash = {} #nums[i],i
    n = len(nums)
    # x,y -> nums : x + y = k
    # x = k - y 
    
    for i in range(n):
        complement = target - nums[i]
        
        if complement in hash:
            return [i,hash[complement]]
        else:
            hash[nums[i]] = i
    return [-1,-1]