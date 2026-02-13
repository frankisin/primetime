class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def mergeSortedLL(list1,list2):
    l1 = list1
    l2 = list2 

    dummy = Node(0)
    merged = dummy 

    while l1 and l2:
        if l1.val < l2.val:
            merged.next = l1
            l1 = l1.next
        else:
            merged.next = l2
            l2 = l2.next
        merged = merged.next 
    if l1:
        merged.next = l1
    if l2:
        merged.next = l2 
    return dummy.next 

