class Node:
    def __init__(self,val,):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self,p:'Node',q:'Node'):
        ancestors = set()
        while p:
            ancestors.add(p.parent)
            p = p.parent
        
        while q:
            if q in ancestors:
                return q
            q = q.parent
        
        
    