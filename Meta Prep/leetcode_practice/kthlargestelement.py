import heapq
def findKthLargest(nums, k) -> int:
    heap = []

    for num in nums:
        heapq.heappush(heap,num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]
