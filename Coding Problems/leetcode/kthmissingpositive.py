class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        left = 0
        right = len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2 
            missing = arr[mid] - (mid+1) # a zero index array is (i + 1), difference is the number of missing numbers.
            
            if missing < k :
                left = mid + 1
            else:
                right = mid - 1
        return left + k 
    
    
                
        