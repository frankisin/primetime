import collections


class Solution:
    def distanceK(self, root, target, k):
        if k == 0:
            return [target.val]
        
        graph = collections.defaultdict(list)

        queue = collections.deque([root])

        #were doing bfs to traverse the tree in order and to build out our graph...


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
        visited = set([target])

        while queue:
            node,distance = queue.popleft()

            if distance == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge,distance+1))
        return res 



