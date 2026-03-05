import heapq
def meetingRooms(intervals):
    max_rooms = 0 
    intervals.sort()

    heap = [] 

    for start,end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap,end)
        max_rooms = max(max_rooms,len(heap))
    return max_rooms




