class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
def threeSum(nums):
    
    if len(nums) < 3:
        return [nums]
    
    nums.sort()
    
    res = []
    
    n = len(nums)
    
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue 
        if nums[i] > 0:
            break 

        l = i + 1
        r = n - 1 

        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                res.append([nums[i],nums[l],nums[r]])
                l += 1
                r -= 1

                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r-=1
    return res 

def diameterBinaryTree(root):
    best = 0 

    def dfs(node):
        if node is None:
            return 0
        
        nonlocal best 
        
        left = dfs(node.left)
        right = dfs(node.right)

        best = max(best,left + right) # say we're at root node, the diameter of the tree is the height of the left subtree plus right subtree...

        return 1 + max(left,right) # the height at any node is 1 plus the height of left/right subtree (which ever is greater)...
    
    dfs(root)
    return best 

def kthMissingPositive(nums,k):

    #nums[i] - (i+1)

    left = 0 
    right = len(nums) - 1

    while left <= right:
        mid = (left+right) // 2
        missing = nums[mid] - (mid+1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    return left + k 





