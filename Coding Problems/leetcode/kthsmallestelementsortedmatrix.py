import heapq
class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        heap = [] # val,row,col
        
        n = len(matrix)
        
        for r in range(n):
            heapq.heappush(heap,(matrix[r][0],r,0))
        
        for _ in range(k-1):
            val,r,c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap,(matrix[r][c+1],r,c+1))
        
        return heap[0][0]
            