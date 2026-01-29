def maxNumberOfKSum(k:int,nums)->int:
    nums = sorted(nums)
    n = len(nums)

    left = 0
    right = n - 1
    count = 0 

    while left < right:
        s = nums[left] + nums[right]
        if  s == k: #we've got a match 
            count += 1
            left += 1
            right -= 1
        elif s < k:
            left += 1
        elif s > k:
            right -= 1
    return count