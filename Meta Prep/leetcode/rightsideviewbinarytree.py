def rightsideview(root):
    res = []

    def dfs(node,depth):
        if node is None:
            return
        
        if len(res) == depth:
            res.append(node.val)
        
        dfs(node.right,depth+1)
        dfs(node.left,depth+1)
    dfs(root,0)