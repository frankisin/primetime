import heapq
def kthlargestelement(nums,k):

    heap = []
    for i in range(len(nums)):
        heapq.heappush(heap,nums[i])

        if len(heap) > k:
            heapq.heappop(heap) # get rid of smallest
            
    return heap[0]
            
