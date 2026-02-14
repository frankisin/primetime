from collections import deque,defaultdict

def verticalTraversal(root):
    if not root:
        return []
    
    tree_map = defaultdict(list)
    
    queue = deque([(root,0)]) # node, col...
    
    min_col = max_col = 0 
    
    while queue:
        node,col = queue.popleft()
        
        tree_map[col].append((node.val))
        min_col = min(min_col,col)
        max_col = max(max_col,col)
        
        if node.left:
            queue.append((node.left,col-1))
        if node.right:
            queue.append((node.right,col+1))
    
    #build result
    return [tree_map[c] for c in range(min_col,max_col+1)]
    
    