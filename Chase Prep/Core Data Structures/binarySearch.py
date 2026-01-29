def binarySearch(arr,target):
    left = 0 
    right = len(arr) - 1

    while(left <= right):
        middle = (left + right) // 2 

        if arr[middle] == target:
            return middle
        
        if arr[middle] > target:
            right = middle - 1
        else:
            left = middle  + 1
    return -1

nums = [1,2,3,4]

print(binarySearch(nums,4))