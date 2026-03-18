def removeDuplicatesSortedArray(nums):
    k = 1

    for i in range(1,len(nums)):
        if nums[i] != nums[k]:
            nums[k] = nums[i]
            k += 1
    return k 