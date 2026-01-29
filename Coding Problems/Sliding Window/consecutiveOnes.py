def consecutiveOnes(nums,k):
    best,left,zero_count = 0,0,0

    for right in range(len(nums)):
        #the right side of our window will traverse entirety of dataset...
        if nums[right] == 0:
            zero_count += 1
        
        #shrink the window from the left until its valid again...
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        #now that window is valid we return the number of indeces inside of window right - left + 1
        best = max(best,right-left+1)
    return best 