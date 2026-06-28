# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0):
         self.val = val
         self.next = None
def addTwoNumbers(self, l1, l2):
    p1 = l1
    p2 = l2

    carry = 0 

    dummy = ListNode(0)
    curr = dummy

    while p1 != None or p2 != None or carry:
        num1 = p1.val if p1 != None else 0
        num2 = p2.val if p2 != None else 0 

        total = num1 + num2 + carry

        curr.next = ListNode(total%10)
        carry = total // 10 

        curr = curr.next 
        if p1: p1 = p1.next
        if p2: p2 = p2.next 
    return dummy.next 



