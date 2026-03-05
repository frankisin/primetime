class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def __init__(self):
        self.isBalanced = True
    
    def balanced(self,node):
        if not node:
            return 0 
        
        left = self.balanced(node.left)
        right = self.balanced(node.right)

        if abs(left-right) > 1:
            self.isBalanced = False 
        
        return 1 + max(left,right)
    
     
          