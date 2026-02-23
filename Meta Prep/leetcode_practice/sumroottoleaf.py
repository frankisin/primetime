#For this problem we're building up the number from the root to the leaf node 
class Solution(object):
    def sumNumbers(self, root): #dfs : root -> leaf
        curr = 0

        def dfs(node,curr):
            if node is None:
                return 0 
            
            curr = curr * 10 + node.val

            if node.left is None and node.right is None:
                return curr

            return dfs(node.left,curr) + dfs(node.right,curr)

        return dfs(root,curr)

        
    
