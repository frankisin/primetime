def lca(node,p,q):
    #this is one of those problems that screams dfs 
    #in particular we'll execute a post order traversal...
    #we'll try and reach the leaf nodes and that evaluate them in their parent nodes.
    if node == None:
        return None 
    if node == p or node == q:
        return node 
    
    left = lca(node.left,p,q)
    right = lca(node.rigt,p,q)

    if left and right:
        return node
    
    return left or right 


