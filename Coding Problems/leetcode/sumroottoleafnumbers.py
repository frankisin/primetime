def sumNumbers(self, root) -> int:
    curr = 0 

    def dfs(node,curr):

        if not node:
            return 0
         
        curr = curr * 10 + node.val

        if node.left == None and node.right == None:
            return curr

        return dfs(node.left,curr) + dfs(node.right,curr)