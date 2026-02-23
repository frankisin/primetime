def findPeakElement(self, nums):
    n = len(nums)
    left = 0 
    right = n - 1

    while left < right:
        mid = (left + right) // 2 

        if nums[mid] < nums[mid+1]: # right is increasing...
            left = mid + 1
        else:                       # left is decreasing
            right = mid 
        
    return left
    



