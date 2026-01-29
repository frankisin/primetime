def twoSum(nums,target): #[5,5,1,2],target = 10
    mydict = {} # [nums[i],i]

    for i in range(len(nums)): #O(N) -> O(N^2) if we use nested for loop
        required = target - nums[i]

        if required in mydict:
            return [mydict[required],i]
        else:
            mydict[nums[i]] = i
    
    return []
