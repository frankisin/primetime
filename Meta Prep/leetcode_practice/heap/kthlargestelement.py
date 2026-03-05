import heapq
def kthLargest(nums,k):
    heap = []

    for num in nums:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)
    
    return heap[0]
