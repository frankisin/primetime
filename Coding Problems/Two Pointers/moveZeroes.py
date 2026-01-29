#This algorithm works by instantiating a pointer at the start of the array which will be our non zero index.
#When we find a number we will move it to the non zero index and then proceed to increment the non-zero index.
def moveZeroes(nums):
    n = len(nums)
    non_zero_index = 0 

    for i in range(n):
        if nums[i] != 0: 
            nums[non_zero_index],nums[i] = nums[i],nums[non_zero_index]
            non_zero_index += 1
    return nums 


  