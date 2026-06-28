import heapq
class Node():
    def __init__(self,val):
        self.val = val
        self.next = None
def mergeKLists(lists):
    if not lists:
        return None 
    
    heap = [] #(value,uid,node)

    uid = 0 

    for node in lists:
        if node:
            heapq.heappop(heap,(node.val,uid,node))
            uid+=1 
        
    dummy = Node(0)
    merged = dummy 

    while heap:
        val,uid,node = heapq.heappop(heap) # ive sucessful popped the smallest value from the heap 
        merged.next = node
        merged = merged.next

        if node.next:
            heapq.heappop(heap,(node.next.val,uid,node.next))
            uid += 1
    merged.next = None 
    return dummy.next      
            
