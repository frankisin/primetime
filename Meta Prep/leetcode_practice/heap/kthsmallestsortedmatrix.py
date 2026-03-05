import heapq
def kthsmallestarray(matrix,k):
    heap = [] # (val,x,y)
    n = len(matrix) #row
    m = len(matrix[0]) # col

    for r in range(n):
        heapq.heappush(heap,(matrix[r][0],r,0))

    for _ in range(k-1):
        _,r,c = heapq.heappop(heap)
        if c + 1 < m : 
            heapq.heappush(heap,(matrix[r][c+1],r,c+1))
    return heap[0][0]