def maximumSubarray(arr:list[int],k:int)->float:
    if len(arr) < k:
        return 

    window_sum = sum(arr[:k])
    maximum_sum = window_sum

    for i in range(k,len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i-k]
        maximum_sum = max(maximum_sum,window_sum)
    return maximum_sum / 4



print(maximumSubarray([1,12,-5,-6,50,3], 4))  # 12.75


    