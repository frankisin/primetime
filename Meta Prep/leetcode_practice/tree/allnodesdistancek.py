from collections import deque,defaultdict
def nodesDistanceK(root,target,k):
    graph = defaultdict(list)
    queue = deque([root])

    if k == 0:
        return [target.val]

    while queue:
        node = queue.popleft()

        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append(node.left)
        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)
            queue.append(node.right)
    
    res = []
    queue = deque([(target,0)])
    visited = set([target])

    while queue:
        node,distance = queue.popleft()

        if distance == k:
            res.append(node.val)
            continue 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))
    return res 



    
