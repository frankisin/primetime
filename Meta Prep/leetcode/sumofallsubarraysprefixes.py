def sumSubArrayPrefixSum(nums,k):
    n = len(nums)

    res = []

    prefixes = [0] * (n + 1)

    for i in range(n):
        prefixes[i+1] = prefixes[i] + nums[i]
    
    total = 0 

    for l in range(n):
        for r in range(l,n):
            if prefixes[r+1] - prefixes[l] == k:
                total += 1
    return total 


