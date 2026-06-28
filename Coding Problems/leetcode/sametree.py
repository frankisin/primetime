class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
               
class Solution:
    def isSameTree(self, p, q) -> bool:
        #Base Case 1: both nodes are Null
        if not p and not q:
            return True
        
        #Base Case 2: one is empty, the other one isnt...
        if not p or not q:
            return False
        
        if p.val != q.val:
            return False
        
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        
        
        