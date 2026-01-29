def searchBST(root,val):
    if root == None:
        return None
    
    if root.val == val:
        return root
    
    left = searchBST(root.left,val)
    if left:
        return left
    
    return searchBST(root.right,val)

def searchBST_(root,val):
    if root == None:
        return None 
    
    if root.val == val:
        return root
    
    if root.val < val:
        return searchBST_(root.right,val)
    else:
        return searchBST_(root.left,val)
