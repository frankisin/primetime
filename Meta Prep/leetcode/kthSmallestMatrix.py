import heapq
def kthSmallest(matrix,k):
    
    heap = []
    j = k 
    for row in matrix:
        for col in row:
            heapq.heappush(heap,-col)
            if len(heap) > k:
                heapq.heappop(heap)
    return -heap[0]


matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8

print(kthSmallest(matrix,k))