def reverseString(string):
    vowels = set("aeiouAEIOU")
    string = list(string)
    
    left,right = 0,len(string)-1
    
    while(left < right):
        while left < right and string[left] not in vowels:
            left += 1
        while left < right and string[right] not in vowels:
            right -= 1
        
        string[left],string[right] = string[right],string[left]
        left += 1
        right -= 1
        
def moveZeroes(arr): #[l,2,5,6,0,0,0] -> [1,2,5,6,0,0,0] #O(n)
    last_non_zero = 0
    
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[last_non_zero],arr[i] = arr[i],arr[last_non_zero]
            last_non_zero += 1
    return arr

arr = [0,0,1,2,5,6,0,0,0]

print(moveZeroes(arr=arr))
    
    
    
          