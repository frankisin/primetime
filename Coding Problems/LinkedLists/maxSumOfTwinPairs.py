class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def pairSum(head:ListNode):
    slow = head
    fast = head
    maxSum = 0 

    if not head or not head.next:
        return 0

    while fast and fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    # we've traversed the list once, slow pointer is at the middle...
    curr = slow
    prev = None 

    while curr:
        next = slow.next 
        slow.next = prev #swap pointers
        prev = curr 
        curr = next # move slow forward
    #second half of linked list has been reversed...

    p1 = head
    p2 = prev 

    while(p2):
        maxSum = max(maxSum,p1.val + p2.val)
        p2 = p2.next
        p1 = p1.next

    return maxSum











