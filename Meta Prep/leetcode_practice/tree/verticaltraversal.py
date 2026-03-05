from collections import defaultdict,deque
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def verticalTraversal(root):
        tree_map = defaultdict(list) # columns,[values]
        queue = deque([(root,0)]) #root is in the middle so column is 0 

        min_column = max_column = 0 

        while queue:
            node,col = queue.popleft()

            tree_map[col].append(node.val)

            min_column = min(min_column,col)
            max_column = max(max_column,col)

            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
            
        return [tree_map[col] for col in range(min_column,max_column+1)]
          