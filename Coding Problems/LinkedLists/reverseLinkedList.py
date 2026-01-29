class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def reverseLinkedList(head:ListNode):
     if head is None or head.next is None:
          return head
     
     curr = head 
     prev = None 

     while(curr is not None):
          next = curr.next # save next pointer 
          curr.next = prev # swap pointers 
          prev = curr      # save prev 
          curr = next      # move curr forward 
     return prev 
