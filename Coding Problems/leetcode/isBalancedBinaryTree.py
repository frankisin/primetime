def isBalanced(root)->bool:
    def height(node):
        if node is None:
            return 0
        
        left = height(node.left)
        if left == -1:
            return -1 
        
        right = height(node.right)
        if right == -1:
            return -1 

        if abs(left-right) > 1:
            return -1 
        
        return 1 + max(left,right)
    
    def height_(node):
        if node is None:
            return 0
        
        left = height(node.left)
        right = height(node.right)

        return 1 + max(left,right)
        