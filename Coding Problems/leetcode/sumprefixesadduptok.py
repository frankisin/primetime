def sumOfPrefixes(nums,k):
    prefixCount = {}
    prefixCount[0] = 1

    currSum = 0 
    ans = 0 

    for x in nums:
        currSum += x

        ans += prefixCount.get(currSum - k,0)

        prefixCount[currSum] = prefixCount.get(currSum, 0) + 1
    return ans 
