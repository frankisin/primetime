import heapq
def prefixes(nums):
    n = len(nums)

    prefix = [0] * (n+1)

    print('prefix sum',0)

    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
        print('prefix sum',prefix[i+1])
    
    

    i = 1
    j = 4

    sum = prefix[j+1]-prefix[i]

    print(f'Sum between indices {i},{j} is ', sum)



nums = [1,4,5,6,7,8] 
#prefix sum = [0,1,5,10,16]

#say we want to find the sum of the subarray [i,j] -> [2,3]
#sum => prefix[j+1]-prefix[i] = 

prefixes(nums)

def totalSubarrayEqualsK(nums,k):

    n = len(nums)

    total = 0 

    prefix = [0] * (n+1)

    for i in range(n):
        prefix[i+1] = prefix[i] + nums[i]
    
    for l in range(n):
        for r in range(l,n):
            sum = prefix[r+1] - prefix[l]
            if sum == k:
                total += 1 
    return total 

def kclosestPoints(points,k):
    heap = [] #(distance,x,y)
    closest = []

    def distance(x,y):
        return x ** 2 + y ** 2
    
    for x,y in points:
        dist = distance(x,y)
        heapq.heappush(heap,(-dist,x,y))

        if len(heap) > k:
            heapq.heappop(heap)
    
    while heap:
        dist,x,y = heap[-1]
        closest.append([x,y])
        heapq.heappop(heap)
    
    return closest

def firstLastIndexes(arr,target):
    def searchLeft():
        left = 0 
        right = len(arr)

        res = -1

        while left < right:
            mid = (left+right) // 2

            if arr[mid] < target:
                left = mid+1
            elif arr[mid] > target:
                right = mid - 1
            else:
                right = mid-1
                res = mid
        return res

    def searchRight():
        left = 0 
        right = len(arr)

        res = - 1

        while left < right:
            mid = (left+right) // 2

            if arr[mid] < target:
                left=mid+1
            elif arr[mid] > target:
                right=mid-1
            else:
                right = mid - 1
                res = mid
        return res 

    return [searchLeft(),searchRight()]


        
    








