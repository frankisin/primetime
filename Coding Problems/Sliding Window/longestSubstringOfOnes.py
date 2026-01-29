def longestSubarray(self, nums):
    left = 0
    zero_count = 0 
    best = 0 

    k = 1

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        best = max(best,right - left)
    return best