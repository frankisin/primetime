import heapq

def kthLargestElement(nums,k):
    heap = []

    for num in nums:
        heapq.heappush(heap,num) #if we see any number we append it...

        if len(heap)>k:
            heapq.heappop(heap) #if our heap grows past k then we need to remove the smallest element...

    return heap[0] #return smallest of k largest element... 