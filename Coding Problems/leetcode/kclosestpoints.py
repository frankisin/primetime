import heapq
import math 

def kClosest(points, k: int):
    heap = [] # (distance,x,y)
    
    def distance(x,y):
        return (x**2) + (y**2)
    
    for point in points:
        heapq.heappush(heap,(-distance(point[0],point[1]),point[0],point[1]))
        
        if len(heap) > k:
            heapq.heappop(heap)
    return [[x,y] for _,x,y in heap]
    