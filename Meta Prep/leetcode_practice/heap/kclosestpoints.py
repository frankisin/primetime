import heapq
def kclosestpoints(points,k):
    heap = [] #(-distance,x,y)
    output = []
    
    def distance(x,y):
        return x ** 2 + y ** 2

    for x,y in points:
        heapq.heappush(heap,(-distance(x,y),x,y))

        if len(heap) > k:
            heapq.heappop(heap)
    
    for _,x,y in heap:
        output.append([x,y])
    return output