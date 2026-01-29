from typing import Optional
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def deleteMiddleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    slow = head
    fast = head

    if head is None or head.next is None:
        return None

    while(fast and fast.next):
        prev = slow
        slow = slow.next
        fast = fast.next.next 
    
    #when the while loop above is done then slow is at the middle 
    #and prev is at the node prior to the middle.
    #we need to change prev's pointer to slow.next to exlcude the middle node...
    if(prev):
        prev.next = slow.next
    

    return head 