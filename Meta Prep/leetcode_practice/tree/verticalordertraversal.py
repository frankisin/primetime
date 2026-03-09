from collections import defaultdict,deque

def verticalOrderTraversal(root):
    if not root:
        return []
    
    result = []
    
    cols = defaultdict(list) #col : row,node
    queue = deque([(root,0,0)]) # node, row, col

    while queue:
        node,row,col = queue.popleft()

        cols[col].append((row,node))
        
        if node.left:
            queue.append((node.left,row + 1,col-1))
        if node.right:
            queue.append((node.right,row+1,col+1))
    
    for col in sorted(cols):
        nodes = sorted(cols[col])
        result.append([val for row,val in nodes])
    
    return result 

        
    
    
    
    