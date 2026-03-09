def rangeSumBST(root,low:int,high:int):
    output = []
    
    def dfs(node):
        if node is None:
            return 0
        
        if low <= node.val <= high:
            output.append(node.val)
        
        if node.val > low:
            dfs(node.left)
        if node.val < high:
            dfs(node.right)
    dfs(root)
    return sum(output)
        
            
    