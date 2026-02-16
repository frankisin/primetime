def lowestCommonAncestor(root,p,q):
    if root == None or root == p or root == q:
        return root 
    
    left = lowestCommonAncestor(root.left,p,q)
    right = lowestCommonAncestor(root.right,p,q)

    if left and right:
        return root 
    return left or right 
    


    

