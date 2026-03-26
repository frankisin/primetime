from collections import deque,defaultdict
import heapq
class blind:
    def validwordabbrev(word,abbr)->bool:
        j = 0 
        i = 0 
        m = len(abbr)
        n = len(word)
        
        while j < m:
            if i >= n and abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == "0":
                    return False
                
                num = 0 
                while j < m and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j])-ord('0'))
                    j += 1
                i += num 
                if i > n:
                    return False 
        return i == n
    def validpalindrome(s:str)->bool:
        left = 0 
        right = len(s) - 1
        
        def isPal(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True 
                
        
        while left < right:
            if s[left] != s[right]:
                return isPal(left+1,right) or isPal(left,right-1)
            left += 1
            right -= 1
        return True             
    def minimumRemoveValidParen(s:str)->str:
        cleaned = []
        remove = set()
        stack = []
        
        for i,char in enumerate(s):
            if char == "(":
                stack.append(i)
            elif char == ")":
                if len(stack) == 0:
                    remove.add(i)
                else:
                    stack.pop()
        
        while stack:
            remove.add(stack.pop())
        
        for i in range(len(s)):
            if i not in remove:
                cleaned.append(s[i])
        
        return "".join(cleaned)
    def binarytreerightside(root):
        if not root:
            return []
        result = []
        
        def dfs(node,depth):
            if node is None:
                return 
            
            if len(result) == depth:
                result.append(node.val)
            
            dfs(node.right,depth+1)
            dfs(node.left,depth+1)
        
        dfs(root,0)
        return result
    def maxprofit(prices)->int:
        min_val = float('inf')
        max_profit = 0 
        
        for price in prices:
            min_val = min(min_val,price)
            
            max_profit = max(max_profit,price-min_val)
        
        return max_profit     
    def binarytreeverticaltraversal(root):
        min_col = max_col = 0 
        
        queue = deque([(root,0)]) # node,col
        
        graph = defaultdict(list) #cols : nodes
        
        while queue:
            node,col = queue.popleft()
            
            graph[col].append(node.val)
            
            min_col = min(min_col,col)
            max_col = max(max_col,col)
            
            if node.left:
                queue.append((node.left,col-1))
            if node.right:
                queue.append((node.right,col+1))
        
        return [graph[col] for col in range(min_col,max_col+1)]
    def subarraysumequalsk(nums,k)-> int:
        curr_sum = 0 
        freq = defaultdict(int)
        freq[0] = 1
        count = 0 
        
        #P[j+1]-P[i] = k 
        #P[i] = P[j+1]-k
        
        for num in nums:
            curr_sum += num #P[j+1]
            count += freq[curr_sum-k]
            freq[curr_sum] += 1
        
        return count 
    def rangesumbst(root,low,high):
        res = []
        
        def dfs(node):
            if node is None:
                return 
            
            if low <= node.val <= high:
                res.append(node.val)
            
            if node.val > low:
                dfs(node.left)
            if node.val < high:
                dfs(node.right)
        
        dfs(root)
        return sum(res)
    def kclosestpointsorigin(points,k):
        heap = []
        res = []
        
        def distance(x,y):
            return x ** 2 + y ** 2
        
        for x,y in points:
            dist = distance(x,y)
            
            heapq.heappush(heap,(-dist,x,y))
            if len(heap) > k:
                heapq.heappop(heap)
        
        while heap:
            _,x,y = heapq.heappop(heap)
            res.append([x,y])
        
        return res 
    def twoSum(nums,k):
        dict = defaultdict(int)
        #num1 + num2 = k
        #num2 = k - num1
        
        for i,num in enumerate(nums):
            target = k - num  
            
            if target in dict:
                return [dict[target],i]
            
            dict[num] = i 
        
        return [-1,-1]
    def threeSum(nums):
        res = []
        n = len(nums)
        nums.sort()
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            if nums[i] > 0:
                break
            
            left = i + 1      
            right = n - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
        return res 
    def validparenthesis(s:str)->bool:
        stack = []
        
        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            elif ch in mapping.values():
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
        
        if stack:
            return False
        return True 
    def findfirstlastindexsortedarray(nums,target):
        def searchLeft():
            res = -1
            left = 0 
            right = len(nums)-1
            
            while left <= right:
                mid = (left+right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    right = mid - 1
                    res = mid
            return res
        
        def searchRight():
            res = -1
            left = 0 
            right = len(nums)-1
            
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    res = mid
                    left = mid + 1
            return res 
            
        return [searchLeft(),searchRight()]               
    def mergeintervals(intervals):
        merged = []
        
        intervals.sort()
        
        merged.append(intervals[0])
        
        for start,finish in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1],finish)
            else:
                merged.append([start,finish])
        
        return merged 
    def mergesortedarray(nums1,nums2,m,n):
        i = m - 1 #nums1
        j = n - 1 #nums2
        k = m + n - 1
        
        while j >= 0:
            if i >= 0 and nums2[j] >= nums1[i]:
                nums1[k] = nums2[j]
                j -= 1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
    def palindromicsubs(s:str)->int:
        count = 0 
        
        def expand(l,r):
            nonlocal count
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                i -= 1
                r += 1
        
        for i in range(len(s)):
            expand(i,i)
            expand(i,i+1)
        
        return count 
    def kthmissingnumber(nums,k)->int:
        left = 0 
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            missing = nums[mid] - (mid+1)
            
            if missing < k:
                left = mid + 1
            else:
                right = mid - 1041
            
        return left + k 
    def lowestcommonancestor3(p,q):
        ancestors = set()
        
        while p:
            ancestors.add(p)
            p = p.parent
        
        while q:
            if q in ancestors:
                return q
            q = q.parent
    def containerwithmostwater(heights):
        left = 0 
        right = len(heights)-1
        
        best = 0 
        
        while left < right:
            area = min(heights[left],heights[right]) * abs(right-left)
            
            best = max(best,area)
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return best         
    def longestcommonprefix(strings):
        if not strings:
            return ''
        
        s1 = min(strings)
        s2 = max(strings)
        
        for i,char in enumerate(s2):
            if s2[i] != s1[i]:
                return s1[:i]
        
        return s1 
    def setmatrixzeros(matrix):
        m = len(matrix)
        n = len(matrix[0])
        
        zeros_first_row = any(matrix[0][i] == 0 for i in range(n))
        zeros_fist_col = any(matrix[i][0] == 0 for i in range(m))
        
        #mark zeroes 
        for r in range(1,m):
            for c in range(1,n):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0 
        #flip to zero
        for r in range(1,m):
            for c in range(1,n):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0 
        if zeros_first_row:
            for i in range(n):
                matrix[0][i] = 0 
        if zeros_fist_col:
            for i in range(m):
                matrix[i][0] = 0 
    def longestconsecutiveseq(nums):
        longest = 0 
        
        num_set = set(nums)
        
        for num in nums:
            if num-1 not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(longest,length)
        return longest
    def findpeakelement(nums):
        left = 0 
        right = len(nums)-1
        
        while left < right:
            mid = (left+right)//2
            
            if nums[mid] < nums[mid+1]:
                left = mid + 1
            else:
                right = mid
        
        return left             
    def numberIslands(grid):
        m = len(grid)
        n = len(grid[0])
        
        count = 0 
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def setislandzeros(r,c):
            if 0 <= r < m and 0 <= c < n and grid[r][c] == "1":
                grid[r][c] = "0"
                
                for dr,dc in directions:
                    nr = r + dr
                    nc = c + dc
                    
                    setislandzeros(nr,nc)
                
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":

                    count += 1
                    setislandzeros(r,c)
        return count
    def kthlargestelement(nums,k):
        heap = []
        
        for num in nums:
            heapq.heappush(heap,num)
            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]
    def calculate(s:str):
        sign = "+"
        stack = []
        n = len(s)
        
        num = 0 
        
        for i,ch in enumerate(s):
            if ch.isdigit():
                num = num * 10 + int(ch)
            
            if ch in "+-/*" or i == n - 1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(int(stack.pop() * num))
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                num = 0 
                sign = ch
        
        return sum(stack)
    def lca(root,p,q):
        
        def dfs(node,p,q):
            if node is None:
                return 
            
            if node is p or node is q:
                return node
            
            left = dfs(node.left,p,q)
            right = dfs(node.right,p,q)
            
            if left and right:
                return node
            
            return left or right                     
        
        return dfs(root,p,q)
    def groupshiftedstrings(strings):
        group_dict = defaultdict(list)
        
        for string in strings:
            if len(string) == 1:
                group_dict[(-1,)].append(string)
                continue
            
            curr_diffs = []
            
            i = 1 
            while i < len(string):
                curr_diffs.append(
                    (ord(string[i])-ord(string[i-1])) % 26
                )
                i+=1
            group_dict[tuple(curr_diffs)].append(string)
        
        return list(group_dict.values())
    def topkfrequentelements(nums,k):
        freq = defaultdict(int)
        res = []
        
        for num in nums:
            freq[num] += 1
        #sort by frequencies
        sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)
        
        for i in range(k):
            res.append(
                sorted_freq[i][0] # append by the numbers
            )
        
        return res 
    def battleships(board):
        m = len(board)
        n = len(board[0])
        
        count = 0
        
        for row in range(m):
            for col in range(n):
                if board[row][col] != "X":
                    continue 
                
                if board[row-1][col] == "X":
                    continue
                    
                if board[row][col-1] == "X":
                    continue 
                
                count += 1
        return count 
    def robotclean(robot):
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        visited = set()
        
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(x,y,d):
            visited.add((x,y))
            robot.clean()
            
            for i in range(4):
                nd = (d + i) % 4
                
                dx,dy = directions[nd]
                
                nx = dx + x
                ny = dy + y 
                
                if (nx,ny) not in visited and robot.move():
                    dfs(nx,ny,nd)
                    goback()
                robot.turnRight()
        dfs(0,0,0)
    def diameter(root):
        longest = 0
        
        def dfs(node):
            nonlocal longest
            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            
            longest = max(longest,left+right)
            
            return 1 + max(left,right)
        dfs(root)
        return longest
    def buildingsoceanview(heights):
        res = []
        n = len(heights)
        max_height = 0 
        for i in range(n-1,-1,-1):
            if heights[i] > max_height:
                max_height = heights[i]
                res.append(i)
        return res[::-1]
    def longestsubnorepeats(s:str):
        left = 0
        longest = 0 
        n = len(s)
        seen = set()
        
        for right in range(n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            longest = max(longest,right-left+1)
            seen.add(s[right])
        
        return longest  
                
         
           
            
            
                  
                
        
            
            
            
            
                
                    
        
        
           
                
        
                    
                
        
        
        
        
                          
                
        
         
        
                    
                    
                       
            
        
                   
            
        
                   
        
            
            
                           
        