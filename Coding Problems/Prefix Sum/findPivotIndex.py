def pivotIndex(nums):
    total = sum(nums)
    left_sum = 0 
    right_sum = 0 

    for i in range(len(nums)):
        
        right_sum = total - nums[i] - left_sum

        if left_sum == right_sum:
            return i 
        left_sum += nums[i]
    
    return -1

    