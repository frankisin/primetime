class Solution:
    def diameterBinaryTree(self,root):

        self.best = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            self.best = max(self.best,left + right)

            return 1 + max(left,right)
        dfs(root)
        return self.best
        
    


