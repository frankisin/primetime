import heapq
class Solution:
    def minMeetingRooms(self, intervals)->int:
        if not intervals:
            return 0 
        
        maxRooms = 0 
        
        intervals.sort(key = lambda x:x[0]) #sort by start time
        
        heap = [] # min-heap of end times of meetings currently in progress
        
        for start,end in intervals:
        
            if heap and heap[0] <= start:
                heapq.heappop(heap) # room is available, no overlap 
           
            heapq.heappush(heap,end) # push current meetings end time into heap
            maxRooms(maxRooms,len(heap))
            
        return maxRooms
                
            
        
    
        
        
        
        
        
         