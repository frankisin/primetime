class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class sumRootLeafNode:
    def __init__(self):
        self.curr = 0 
    
    def dfs(self,node,curr):
        if not node:
            return 0 
        
        curr = curr * 10 + node.val 

        if node.left is None and node.right is None:
            return curr 
        
        return self.dfs(node.left,curr) + self.dfs(node.right,curr)