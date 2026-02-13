def sumSubArrayPrefixSum(nums):
    n = len(nums)

    prefixes = [0] * (n + 1)

    for i in range(n):
        prefixes[i+1] = prefixes[i] + nums[i]
    
    total = 0 

    for l in range(n):
        for r in range(l,n):
            total += prefixes[r+1] - prefixes[l]

