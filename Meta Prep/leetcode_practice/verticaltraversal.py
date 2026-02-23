from collections import deque,defaultdict
class Solution:
    def verticalTraversal(self,root):
        
        if not root:
            return []
        
        tree_map = defaultdict(list) # {col : [1,3,5]}

        min_col = max_col = 0

        queue = deque([(root,0)]) # queue is going to hold the node and column 

        while queue:
            node,col = queue.popleft()

            tree_map[col].append(node.val)

            min_col = min(min_col,col)
            max_col = max(max_col,col)

            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
        
        return[tree_map[c] for c in range(min_col,max_col+1)]



