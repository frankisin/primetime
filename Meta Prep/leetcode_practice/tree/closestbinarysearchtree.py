
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
         
         closest = root.val
         curr = root
         
         while curr:
             if abs(curr.val-target) < abs(closest-target):
                 closest = curr.val
             if target < curr.val:
                 curr = curr.left
             elif target > curr.val:
                 curr = curr.right
             else:
                 return curr.val
             
         return closest
