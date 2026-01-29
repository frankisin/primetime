class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def oddEvenLinkedList(head:ListNode):
    if head is None or head.next is None:
        return head 
     
    odd = head 
    even = head.next 
    even_head = even 

    while even and even.next:
        odd.next = even.next # set odd.next pointer to even.next(odd node)
        odd = odd.next       # move odd forward... 

        even.next = odd.next # set even.next to odd.next(even node)
        even = even.next     # move even forward...

    odd.next = even_head # When the loop above is done executing, odd is only populated by odd nodes, 

    return head 



  