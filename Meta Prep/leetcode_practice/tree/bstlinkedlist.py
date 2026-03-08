def bstDoublySortedLinkedList(root):
    head = None 
    prev = None 

    def dfs(node):
        nonlocal head,prev

        if node is None:
            return None 

        dfs(node.left)

        if prev is None:
            head = node
        else:
            prev.right = node
            node.left = prev
        prev = node 
        dfs(node.right)
    
    #make the list circular
    head.left = prev
    prev.right = head

    dfs(root)

    return head 
