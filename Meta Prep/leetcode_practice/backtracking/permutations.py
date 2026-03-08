def permutations(nums):
    if not nums:
        return []
    res = []

    n = len(nums)
    used = [False] * (n)

    def backtrack(nums,used,curr):
        if len(curr) == n:
            res.append(curr.copy())
            return 
        else:
            for i in range(n):
                if used[i]:
                    continue
                curr.append(nums[i])
                used[i] = True
                backtrack(nums,used,curr)
                used[i] = False
                curr.pop()
    backtrack(nums,used,[])

