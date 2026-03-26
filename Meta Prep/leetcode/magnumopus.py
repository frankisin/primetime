import enum
import heapq
from collections import defaultdict,deque
class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.prev = None
        self.next = None
        self.left = None
        self.right = None 
class Solution:
    def minMeetingRooms(self, intervals):
        heap = []
        maxrooms = 0 

        intervals.sort(key = lambda x:x[0])

        for start,end in intervals:
            if heap and start <= heap[0]:
                heapq.heappop(heap)
            
            heapq.heappush(heap,end)
            maxrooms = max(maxrooms,len(heap))
        return maxrooms
    def canJump(self,nums):
        #nums = [1,3,1,2,2]
        
        end = len(nums)-1
        farthest = 0

        for i,jump in enumerate(nums):
            if i > farthest: 
                return False 
            
            farthest = max(farthest,jump + i)

            if farthest >= end:
                return True 
    def minDeletions(self,string:str):
        
        b_count = 0 
        deletions = 0

        for ch in string:
            if ch == "b":
                b_count += 1
            else:
                deletions = min(deletions + 1,b_count)
        
        return deletions 
    def compress(self,string):
        read = 0 
        write = 0 
        n = len(string)

        while read < n:
            start = read
            ch = string[start]

            while read < n and string[read] == ch:
                read += 1
            
            count = read-start

            string[write] = ch
            write += 1
            if count > 1:
                for digit in str(count):
                    string[write] = digit
                    write += 1
        return write # returning the length of the new compressed string
    def validPalindrome(self,string):
        def isValid(left,right):
            while left < right:
                if string[left] != string[right]:
                    return False
                else:
                    left += 1
                    right -= 1
            return True

        l = 0
        r = len(string)-1

        while l < r:
            if string[l] != string[r]:
                return isValid(l+1,r) or isValid(l,r-1)
            else:
                l += 1
                r -= 1
        return True 
    def merge(self,intervals):
        pass
    def longestSubstringWithoutRepeats(s:str):
        best = 0
        left = 0
        seen = set()
        

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            best = max(best,right-left+1)
        return best
    def calculate(s:str): #4 + 24 * 2 
        stack = []
        sign = "+"
        num = 0 
        n = len(s)

        for i,char in enumerate(s):
            if char.isdigit():
                num = int(char) + num * 10 

            if char in "x-+/" or i == n-1:
                if sign == "+":
                    stack.append(num)

                elif sign == "-":
                    stack.append(-num)

                elif sign == "*":
                    stack.append(int(stack.pop() * num))

                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                sign = char
                num = 0 
        return sum(stack)
def simplifyPath(s:str):
    stack = []

    path_items = s.split("/")

    for item in path_items:
        if item == "." or not item:
            continue 
        elif item == "..":
            if stack:
                stack.pop()
        else:
            stack.append(item)
    
    return "/"+"/".join(stack)

def mergeIntervals(intervals):

    intervals.sort()

    merged = [intervals[0]]

    for start,end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1],end)
        else:
            merged.append([start,end])
    return merged 

def minMeetingRooms(intervals):
    max_rooms = 0 

    heap = []

    intervals.sort()

    for start,end in intervals:
        if heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap,end)
        max_rooms = max(max_rooms,len(heap))
    return max_rooms
def findKthPositive(self, arr, k):
    left = 0 
    right = len(arr)-1

    while left < right:
        mid = (left + right) // 2
        missing = arr[mid] - (mid + 1)

        if missing < k:
            left += 1
        else:
            right -= 1
    return left + k 

def searchRange(nums, target):
    def searchLeft():
        left = 0 
        right = len(nums) - 1
        res = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid - 1
                res = mid 
        return res 
    def searchRight():
        left = 0 
        right = len(nums)-1
        res = -1 

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1 
                res = mid 
        return res 
    return[searchLeft(),searchRight()]


def diameter(self,root):
    self.best = 0 

    def dfs(node):
        if node is None:
            return 0 
        left = dfs(node.left)
        right = dfs(node.right)

        self.best = max(self.best,left+right)

        return 1 + max(left,right)
    dfs(root)
    return self.best 

def subArraySumEqualsK(nums,k):
    freq = defaultdict(int)
    count = 0 
    freq[0] = 1 #base case 
    curr_sum = 0 

    
    #P[j+1]-P[i] = k <--
    #P[i] = P[j+1] - k

    for num in nums:
        curr_sum += num
        need = curr_sum - k 
        count += freq[need]
        freq[curr_sum] += 1
    return count 
def minimumRemoveValidParenthesis(s:str):
    stack = []
    remove = set()
    cleaned = []

    for i,char in enumerate(s):
        if char == '(':
            stack.append(i)
        elif char == ')':
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

def meetRooms(intervals): #[[1,10],[5,15]]

    heap = []

    sorted_intervals = sorted(intervals,key = lambda x:x[0]) # sort by start time 

    intervals = sorted_intervals

    max_room = 0

    for start,end in intervals:
        while heap and heap[0] <= start:
            heapq.heappop(heap)
        heapq.heappush(heap,end)
        max_room = max(max_room,len(heap))

    return max_room #max_room  = 2

def rightSideBinaryTree(root):
    res = []

    def dfs(node,depth):
        if node is None:
            return None 
        
        if len(res) == depth:
            res.append(node.val)
        
        dfs(node.right,depth+1)
        dfs(node.left,depth+1) #if right subtree is empty we still include the left subtree which satisfies edge cases
    
    dfs(root,0) #call dfs initially with root node and depth = 0 
    return res 

def verticalOrderTraversal(root):

    cols = defaultdict(list) #col : node, row 

    queue = deque([(root,0,0)])

    while queue:
        node,x,y = queue.popleft()

        cols[x].append((node,y))

        if node.left:
            queue.append((node.left,x-1,y+1))
        if node.right:
            queue.append((node.right,x+1,y+1))
    
    #for col in sorted(cols):

        
def rightSidedBinaryTree(root):
    res = []

    def dfs(node,depth):
        if node is None:
            return None
        
        if len(res) == depth:
            res.append(node.val)

        dfs(node.roght,depth+1)
        dfs(node.left,depth+1)
    
    dfs(root,0)
    return res

def longSubNoRepeatingChars(s):
    seen = set()

    left = 0 

    best = 0 

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left+=1
        seen.add(s[right])
        best = max(best,right-left+1)

    return best 

def sumRootToleaf(root):

    num = 0 

    def dfs(node,num):
        if node is None:
            return 0
        
        num = num * 10 + node.val

        if node.left is None and node.right is None:
            return num 
        
        return dfs(node.left,num) + dfs(node.right,num)

    return dfs(root,num)

def verticalOrderTraversal(root):
    graph = defaultdict(list)

    min_col = max_col = 0 

    queue = deque([(root,0)]) #(val,col)

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

def lca(root,p,q):


    def dfs(node,p,q):

        if node is None:
            return None 
        
        if node is p or node is q:
            return node 
        
        left = dfs(node.left,p,q)
        right = dfs(node.right,p,q)

        if left and right:
            return node #we've found the lca
        
        return left or right 
    
    return dfs(root,p,q)
def nodesDistanceK(root,target,k):
    if k == 0:
        return [target.val] #target is k = 0 distance away from target...
    
    graph = defaultdict(list)

    queue = deque([(root)])

    while queue:
        node = queue.popleft()

        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append((node.left))
        if node.right:
            graph[node].append(node.right)
            graph[node.right].append(node)
            queue.append((node.right))
        
    visited = set([target])

    res = []

    queue = deque([(target,0)])

    while queue:
        node,distance = queue.popleft()

        if distance == k:
            res.append(node.val)
        
        for neighbor in graph[node]: #search the neighbors...
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor,distance+1))
    return res 

def _boundaryBinaryTree(root):

    res = []

    def isleaf(node):
        return node.left is None and node.right is None

    if not isleaf(root):
        res.append(root.val)

    curr = root.left

    while curr:
        if not isleaf(curr):
            res.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
        
    def addLeaves(node):
        if node is None:
            return None 
        if isleaf(node):
            res.append(node.val)
        addLeaves(node.left)
        addLeaves(node.right)
    
    addLeaves(root)

    stack = []

    curr = root.right

    while curr:
        if not isleaf(curr):
            stack.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    while stack:
        res.append(stack.pop())
    
    return res 

def boundaryBinaryTree(root):

    if root is None:
        return []

    res = []

    def isLeaf(node):
        return node.left is None and node.right is None
    
    def addLeaves(node):
        if node is None:
            return None
        if isLeaf(node):
            res.append(node.val)
        addLeaves(node.left)
        addLeaves(node.right)

    if not isLeaf(root):
        res.append(root.val)
    
    curr = root.left

    while curr:
        if not isLeaf(curr):
            res.append(curr.val)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right
    
    addLeaves(root)

    curr = root.right

    stack = []

    while curr:
        if not isLeaf(curr):
            stack.append(curr.val)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    
    while stack:
        res.append(stack.pop())
    
    return res 

def numberOfIslands(grid):
    num_islands = 0 

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def setIslandsZero(grid,row,col):
        if 0 <= col < len(grid[0]) and 0 <= row < len(grid) and grid[row][col] == "1":
            grid[row][col] = "0"

            for dr,dc in directions:
                setIslandsZero(grid,row+dr,col+dc)
    
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                num_islands+=1
                setIslandsZero(grid,row,col)
    return num_islands

def canFinish(numCourses, prerequisites):
    
    visited = set()
    cycle = set()

    graph = defaultdict(list)

    for course,prereq in prerequisites:
        graph[course].append(prereq)
    
    def dfs(crs):
        if crs in cycle:
            return False
        if crs in visited:
            return True 
        
        cycle.add(crs)

        for prereq in graph[crs]:
            if dfs(prereq) == False:
                return False 
        
        visited.add(crs)
        cycle.remove(crs)
        return True
    
    for crs in range(numCourses):
        if dfs(crs) == False:
            return False
    return True 

def rangeSumBinaryTree(root,low,high):
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

def shortestPathBianryMatrix(grid):
    n = len(grid)

    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1 

    directions = [
        (-1,-1),(-1,0),(-1,1),
        (0,-1),        (0,1),   
        (1,-1),(1,0),  (1,1)
    ]

    queue = deque([(0,0,1)])

    grid[0][0] = 1 #set starting node as visited...

    while queue:
        r,c,dist = queue.popleft()

        if r == n - 1 and c == n - 1:
            return dist #return the distance we had to travel to reach grid[n-1][n-1]
        
        for dr,dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                queue.append((nr,nc,dist+1))
                grid[nr][nc] = 1
    return -1 

def permutation(nums):
    n = len(nums)

    used = [False] * (n)

    res = []

    def backtrack(nums,used,path):
        if len(path) == n:
            res.append(path.copy())
            return 
        
        for i in range(n):
            if used[i]:
                continue
            
            used[i] = True
            path.append(nums[i])
            backtrack(nums,used,path)
            used[i] = False
            path.pop()
    
    backtrack(nums,used,[])
    return res 

def combinations(n,k):
    res = []

    def backtrack(n,k,idx,path):
        if len(path) == k:
            res.append(path.copy())
            return 
        
        for i in range(idx,n+1):
            path.append(i)
            backtrack(n,k,i+1,path)
            path.pop()
    
    backtrack(n,k,1,[])
    return res 

def mergeSortedLists(list1,list2):
    l1 = list1
    l2 = list2 

    dummy = Node(0)
    merged = dummy 

    while l1 and l2:
        if l1.val < l2.val:
            merged.next = l1
            l1=l1.next
        else:
            merged.next = l2
            l2 = l2.next 
        merged = merged.next
    
    if l1:
        merged.next = l1
    if l2:
        merged.next = l2
    
    return dummy.next

def longestSubstringWithoutRepeats(s:str):
    left = 0
    seen = set()
    longest = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        longest = max(longest,right-left+1)
    
    return longest 

def courseSchedule(numCourses,prerequisites:list[list]):
    #numCourses => 0...n-1

    graph = defaultdict(list)

    visited = set()
    cycle = set()

    for course,prereq in prerequisites:
        graph[course].append(prereq)
    
    def dfs(crs):
        if crs in visited:
            return True 
        if crs in cycle:
            return False  
        
        cycle.add(crs)
        for neighbor in graph[crs]:
            if dfs(neighbor) == False:
                return False 
        visited.add(crs)
        cycle.remove(crs)
        return True 
    
    for i in range(numCourses):
        if dfs(i) == False:
            return False 
    return True 
def productArrayExceptSelf(nums):
    n = len(nums)
    prefix = [1] * n
    left = 1

    for i in range(n):
        prefix[i] = left
        left *= nums[i]
    
    right = 1
    for i in range(n-1,-1,-1):
        prefix[i] *= right
        right *= nums[i]
    
    return prefix 
def numIslands(grid):
    num_islands = 0 

    n = len(grid)

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    def dfs(r,c):
        if 0 <= r < n and 0 <= c < len(grid[0]) and grid[r][c] == "1":
            grid[r][c] = "0"
            
            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr,nc)
    
    for i in range(n):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                num_islands += 1
                dfs(i,j)
    return num_islands

def topFrequentK(nums,k):
    freq = defaultdict(int)
    res = []
    for num in nums:
        freq[num] += 1
    
    sorted_freq = sorted(freq.items(),key=lambda x:x[1],reverse=True)

    for i in range(k):
        res.append(sorted_freq[i])
    return res 
def kthSmalestBST(root):

    heap = []

    def dfs(node):
        if node is None:
            return 
        
        if node.left:
            dfs(node.left)
        
        heapq.heappush(heap,-node.val)

        if node.right:
            dfs(node.right)
def cleanRoom(self, robot):

    directions = [(-1,0),(0,1),(1,0),(0,-1)]
    visited = set() #(x,y)

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

             nx,ny = x + dx,y + dy

             if (nx,ny) not in visited and robot.move():
                dfs(nx,ny,nd)
                robot.goback()
             robot.turnRight()
def wordAbbreviation(word,abbr):

    i = 0 
    j = 0 
    
    m = len(abbr)
    n = len(word)

    
    while j < m:
        if abbr[j].isalpha(): # if the char is alaphabet
            if i >= n or word[i] != abbr[j]:
                return False
            i += 1
            j += 1
        else:
            if abbr[j] == '0':
                return False # cant have leading zeros...
            
            num = 0 
            while j < m and abbr[j].isdigit():
                num = num * 10 + (ord(abbr[j])-ord('0'))
                j += 1
            i += num 
            if i > n:
                return False
    return i == n 

def wordAbbrev(word,abbr):
    i = j = 0
    m = len(abbr)
    n = len(word)

    while j < m:
        if abbr[j].isalpha():
            if i >=n or abbr[j] != word[i]:
                return False
            i += 1
            j += 1
        else:
            if abbr[j] == "0":
                return False
            
            num = 0

            while j < m and abbr[j].isdigit():
                num = num * 10 + (ord(abbr[j])-ord('0'))
                j+=1
            
            i += num

            if i > n:
                return False 
    return i == n
    #after you're done traversing, check if the pointer is at the end of the word index...

def minimumRemovalValidParenthesis(s:str):
    clean = []

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
            clean.append(s[i])
    
    return "".join(clean)
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0 

    for price in prices:
        min_price = min(min_price,price)
        max_profit = max(max_profit,price-min_price)
    
    return max_profit

def binaryTreeRightSide(root):
    res = []

    def dfs(node,depth):
        if node is None:
            return None 
        
        if len(res) == depth:
            res.append(node.val)
        
        dfs(node.right,depth+1)
        dfs(node.left,depth+1)
    
    dfs(root,0)
    return res 

def binaryTreeVertical(root):
    if root is None:
        return []

    graph = defaultdict(list) # cols : node.val

    min_col = max_col = 0 

    queue = deque([(root,0)]) #root,col

    while queue:
        node,col = queue.popleft()

        min_col = min(min_col,col)
        max_col = max(max_col,col)

        graph[col].append(node.val)

        if node.left:
            queue.append((node.left,col-1))
        if node.right:
            queue.append((node.right,col+1))
        
    
    return [[graph[col] for col in range(min_col,max_col+1)]]

def mergeInterval(intervals):
    res = []

    intervals.sort() # sort intervals by starting

    res.append(intervals[0])

    for start,end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(res[-1][1],end)
        else:
            res.append([start,end])
    return res 
        
def validParenthesis(s:str):
    stack = []
    #for this problem we map the close brackets to their open bracket values 
    mapping = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for i,char in enumerate(s):
        if char in mapping.values(): #if its open brackets...
            stack.append(char)
        elif char in mapping: #if its closing brackets...
            if len(stack) == 0 or mapping[char] != char:
                return False 
            stack.pop()


    
    return True if len(stack) == 0 else False 

def _validparenthesis(s:str):
    mapping = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    stack = []

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or mapping[char] != char:
                return False

def basicCalculator(s:str):
    sign = "+"
    num = 0 
    stack = []

    n = len(s)

    for i,char in enumerate(s):
        if char.isdigit():
            num = num * 10 + int(char)
        if char in "+-/*" or i == n - 1:
            if sign == "+":
                stack.append(num)
            elif sign == "-":
                stack.append(-num)
            elif sign == "*":
                stack.append(int(stack.pop() * num))
            elif sign == "/":
                stack.append(int(stack.pop() / num))
            sign = char
            num = 0 
    return sum(stack)

def findRange(nums,target): #O(log(N))
    def searchleft():
        res = - 1
        left = 0 
        right = len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                right = mid - 1
        return res

    def searchright():
        res = - 1
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left+right)//2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                res = mid
                left = mid + 1
        return res 
    
    return[searchleft(),searchright()]


def sumArraysEqualK(nums,k): #O(N)
    curr_sum = 0
    count = 0 
    freq = defaultdict(int)

    freq[0] = 1

    #P[j+1] - P[i] = k

    for num in nums:
        curr_sum += num
        count += freq[curr_sum-k]
        freq[curr_sum] += 1

    return count

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

def validWordAbbrev(word,abbr):
    m = len(abbr)
    n = len(word)
    i = 0
    j = 0 

    while j < m:
        if abbr[j].isalpha():
            if i >= n or abbr[j] != word[i]:
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

def validPalindrom(s:str):
    left = 0 
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True 

def validWordAbbre(word,abbr)->bool:
    i = 0 
    j = 0 
    n = len(word)
    m = len(abbr)

    while j < m :
        if abbr[j].isalpha():
            if i >= n or abbr[j] != word[i]:
                return False
            i += 1
            j += 1
        else:
            if abbr[j] == "0":
                return False #no starting zeros...
            
            num = 0 

            while j < m and abbr[j].isdigit():

                num = num * 10 + (ord(abbr[j])-ord('0'))
                j += 1
            i += num
            if i > n:
                return False
    return i == n 

def subarraySumEqualK(nums,k):
    count = 0 
    freq = defaultdict(int)
    freq[0] = 1
    curr_sum = 0 

    #P[j+1] - P[i] = k
    #P[i] = P[j+1] - k 

    for num in nums:
        curr_sum += num
        count += freq[curr_sum-k]
        freq[curr_sum] += 1
    
    return count 

def validParenthesis(s:str)->str:
    clean = []
    stack = []
    remove = set()

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
            clean.append(s[i])
    
    return "".join(clean)

def kclosestpoints(points,k):
    #points = [[x,y],[x1,y2]

    heap = [] #(dist,x,y) # size k

    def distance(x,y):
        return x ** 2 + y ** 2
    
    for x,y in points:
        dist = distance(x,y)

        heapq.heappush(heap,(-dist,x,y))

        if len(heap) > k:
            heapq.heappop(heap)
    
    return [[x,y] for _,x,y in heap]

def binaryTreeRightSided(root):
    res = []

    def dfs(node,depth):
        if node is None:
            return 
        
        if depth == len(res):
            res.append(node.val)
        
        dfs(node.right,depth+1)
        dfs(node.left,depth+1)
    
    dfs(root,0)
def buildingsWithOceanView(buildings):

    n = len(buildings)
    res = []
    max_height = 0

    for i in range(n-1,-1,-1):
        if buildings[i] >= max_height:
            res.append(i)
        max_height = max(max_height,buildings[i])
    
    return res[::-1]
    
def bestTimeBuyAndSellStock(prices):
    min_price = float('inf')
    max_profit = 0 

    for price in prices:
        min_price = max(min_price,price)

        max_profit = max(max_profit,price-min_price)

    return max_profit 

def binaryTreeRightSide(root):

    res = []

    def dfs(node,depth):
        if node is None:
            return 
        
        if len(res) == depth:
            res.append(node.val)
        
        dfs(node.right,depth+1)
        dfs(node.left,depth+1)
    
    return dfs(root,0)

def mergeSortedArray(nums1,m,nums2,n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -=1

def palindromicSubstrings(s:str)->int:
    count = 0 

    def expand(l,r):
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    for i in range(len(s)):
        expand(i,i)
        expand(i,i+1)


    return count
def findPeakElement(nums):
    left = 0 
    right = len(nums) - 1

    while left < right:
        mid = (left+right) // 2

        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid 
    return left     

def numberOfIslands(grid):
    count = 0 

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    def setIslandsZero(grid,r,c):
        while 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1":
            grid[r][c] = "0"

            for dr,dc in directions:
                nr = r + dr
                nc = c + dc

                setIslandsZero(grid,nr,nc)
    
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                count += 1
                setIslandsZero(grid,r,c)
    
    return count 

import random
import bisect

class Solution:
    def __init__(self,w) -> None:
        self.curr_sum = 0 
        self.prefix = []

        for weight in w:
            self.curr_sum += weight
            self.prefix.append(self.curr_sum)
        self.total = self.curr_sum
    
    def pickIndex(self):
        target = random.randint(1,self.total) # select random int in total

        return bisect.bisect_left(self.prefix,target)

def diameterBinaryTree(root):

    diameter = 0 

    def dfs(node):
        nonlocal diameter

        if node is None:
            return 0 
        
        left = dfs(node.left)
        right = dfs(node.right)

        diameter = max(diameter,left+right)    

        return 1 + max(left,right)
    dfs(root)
    return diameter

def buildingsOceanview(heights):
    max_height = 0 
    res = []

    for i in range(len(heights)-1,-1,-1):
        curr_height = heights[i]
        if curr_height > max_height:
            max_height = curr_height
            res.append(i)
    
    return res[::-1]
def longestSubWithoutRepeat(s:str)->int:
    count = 0 
    seen = set()

    left = 0 
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        count = max(count,right-left+1)

    return count
def mergeSorted(list1,list2):
    l1 = list1
    l2 = list2

    dummy = Node(0)
    merged = dummy 

    while l1 and l2:
        if l1.val < l2.val:
            merged.next = l1
            l1 = l1.next
        else:
            merged.next = l2
            l2 = l2.next
        merged = merged.next
    
    if l1:
        merged.next = l1
    if l2:
        merged.next = l2 
    
    return dummy.next 

def nextPermutation(nums):
    n = len(nums)

    i = n - 2

    #find pivot
    while i >= 0 and nums[i] <= nums[i+1]:
        i -= 1
    
    #if pivot exists, find next smallest number...
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]

    #reverse suffix
    left = i + 1
    right = n - 1

    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
def combine(n,k):
    #1.....N in k tuples k = 2 [1,2],[1,3],[2,1]
    res = []

    def backtrack(n,k,idx,path):
        if len(path) == k:
            res.append(path.copy())
            return 
        
        for i in range(idx,n+1):
            path.append(i)
            backtrack(n,k,i+1,path)
            path.pop()
    
    backtrack(n,k,1,[])
    return res 
def simplifypath(s:str)->str:
    stack = []

    path_items = s.split("/")

    for item in path_items:
        if item == "." or not item:
            continue 
        elif item == "..":
            stack.pop()
        else:
            stack.append(item)
    return "/"+"/".join(stack) 


#balance binary search tree
def balanceBST(root):
    vals = []

    def inorder(node):
        if node is None:
            return 
        
        inorder(node.left)
        vals.append(node.val)
        inorder(node.right)
    
    def build(l,r):
        if l > r:
            return None 

        mid = (l+r) // 2
        node = Node(vals[mid])
        node.left = build(l,mid-1)
        node.right = build(mid+1,r)

        return node 
    inorder(root)
    return build(0,len(vals)-1)
class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right 
def balancebst(root):
    vals = []
    def inorder(node):
        if node is None:
            return 
        inorder(node.left)
        vals.append(node.val)
        inorder(node.right)
    
    def build(l,r):
        if l > r:
            return 
        
        mid = (l+r) // 2
        node = TreeNode(vals[mid])
        node.left = build(l,mid-1)
        node.right = build(mid+1,r)

        return node 
    inorder(root)
    build(0,len(vals)-1)



def sumRootToLeafNumbers(root):

    def dfs(node,curr):

        if node is None:
            return 0
        
        curr = curr * 10 + node.val

        if node.left is None and node.right is None:
            return curr
        
        left = dfs(node.left,curr)
        right = dfs(node.right,curr)

        return left + right 
    return dfs(root,0)
        
def customSorted(s,order):
    rank = defaultdict(int)

    def getrank(ch):
        if ch in rank:
            return rank[ch]
        return len(order)

    for i,ch in enumerate(order):
        rank[ch] = i 
    
    custom_sorted = sorted(s,key=getrank)

    return "".join(custom_sorted)

def goatlatin(words):
    vowels = set("aeiouAEIOU")
    output = []

    words_nospace = words.split(" ")

    for i,word in enumerate(words_nospace,start=1):
        new_word = ""
        if word[0] in vowels:
            new_word = word+"ma"
        else:
            new_word = word[1:] + word[0] + "ma"
        new_word += "a" * i
        output.append(new_word)
    
    return " ".join(output)

def nodesDistanceKBinaryTree(root,target,k):
    graph = defaultdict(list)
    res = []
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
    
    queue = deque([(target,0)])
    visited = set([target])
    while queue:
        node,dist = queue.popleft()

        if dist == k:
            res.append(node.val)
        
        for neigh in graph[node]:
            if neigh not in visited:
                visited.add(neigh)
                queue.append((neigh,dist+1))
    
    return res 
        
def removeAdjacentDupes(s:str):
    stack = []

    for ch in s:
        if stack and ch == stack[-1]:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)
from collections import deque 
def shortestPathInBinaryMatrix(grid):
    n = len(grid) #assuming nxn
    if grid[0][0] != "0" or grid[n-1][n-1] != "0":
        return -1
    
    directions = [
            (-1,-1), (-1,0),(-1,1),
            (0,-1),         (0,1),
            (1,-1),  (1,0), (1,1)
    ]
    queue = deque([(0,0,1)]) # count initial dist as 1 

    grid[0][0] = "1"

    while queue:
        r,c,dist = queue.popleft()

        if r == n-1 and c == n-1:
            return dist
        
        for dr,dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc <n and grid[nr][nc] == "0":
                grid[nr][nc] = "1"
                queue.append((nr,nc,dist+1))
    return -1 
def rangeSumBinaryTree(root,low,high):
    output = []

    def dfs(node):
        if node is None:
            return 
        
        if low <= node.val <= high:
            output.append(node.val)
        
        if node.val > low:
            dfs(node.left)
        if node.val < high:
            dfs(node.right)
    dfs(root)
    return sum(output)

def validParen(s:str)->bool:
    mapping = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    stack = []

    for ch in s:
        if ch in "({[":
            stack.append(ch)
        elif ch in mapping:
  
            if not stack or stack[-1] != mapping[ch]:
                return False 
    
    return len(stack) == 0 
            
def validpalindrome(s:str):
    stack = []
    mapping = {
        ")":"(",
        "}":"{",
        "]":"["
    }

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in mapping:
            if not stack or stack[-1] != mapping[ch]:
                return False 
    
    return len(stack) == 0 

def rangesumbinarytree(root,low,high):
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

def rangeSum(root,low,high):

    output = []

    def dfs(node):
        if node is None:
            return 
        
        if low <= node.val <= high:
            output.append(node.val)
        
        if node.val > low:
            dfs(node.left)
        if node.val < high:
            dfs(node.right)
    dfs(root)
    return sum(output)
        
def mergeSortedArr(nums1,nums2,m,n):
    #we know that the len of nums1 = m + N

    i = m - 1 #nums1
    j = n - 1 #nums2
    k = m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

def mergesortedarr(nums1,nums2,m,n):
    i = m - 1 #nums1
    j = n - 1 #nums2
    k = m + n -1

    while j >= 0:
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -=1
        else:
            nums1[k] = nums2[j]
            j -=1
        k -=1 
class Node:
    def __init__(self,val,next=None,prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev 
def mergesortedlists(list1,list2):
    l1 = list1
    l2 = list2

    dummy = Node(0)
    merged = dummy 

    while l1 and l2:
        if l1.val < l2.val:
            node = Node(l1.val)
            merged.next = node
            l1 = l1.next
        else:
            node = Node(l2.val)
            merged.next = node
            l2=l2.next
        merged = merged.next 
    
    if l1:
        merged.next = l1
    if l2:
        merged.next = l2 

    return dummy.next 

def nextpermutation(nums):
    n = len(nums)

    i = n - 2

    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    #by this point we should have the pivot for our set.
    #if the pivot exists you find the next smallest number 
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]
    
    left = i + 1
    right = n - 1

    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1

def nextperm(nums):
    n = len(nums)

    i = n - 2

    while i >= 0 and nums[i] >= nums[i+1]:
        i += 1
    
    if i >= 0:
        j = n - 1
        while nums[j] >= nums[i]:
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]
    
    left = i + 1
    right = n - 1

    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1 
        
#Course Schedule (207)
#Merge Two Sorted Lists (21)

def courseSchedule(numCourses,prerequisites):
    graph = defaultdict(list)
    visited = set()
    cycle = set()
    
    for course,prereq in prerequisites:
        graph[course].append(prereq)
    
    def dfs(crs):
        if crs in visited:
            return True
        if crs in cycle:
            return False 
        
        cycle.add(crs)
        for neighbor in graph[crs]:
            if dfs(neighbor) == False:
                return False 
        cycle.remove(crs)
        visited.add(crs)
        return True 
    
    for i in range(numCourses):
        if dfs(i) == False:
            return False 
    return True 

def mergeSorted(nums1,nums2,m,n):
    i = m - 1 # nums1
    j = n - 1 # nums2
    k = m + n - 1 # nums1 true index

    while j >= 0:
        if i >= 0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1 
def simplify(s:str)->str: #O(N)
    stack = []

    path_items = s.split("/")

    for item in path_items:
        if item == "." or not item:
            continue 
        elif item == "..":
            if stack:
                stack.pop()
        else:
            stack.append(item)
    return "/"+"/".join(stack)

def allNodesDistanceK(root,target,k):
    if k == 0:
        return [target.val]
    res = []
    
    graph = defaultdict(list)
    
    queue = deque([(root)])

    while queue:
        node = queue.popleft()

        if node.left:
            graph[node].append(node.left)
            graph[node.left].append(node)
            queue.append(node.left)
        if node.right:
            graph[node].append(node)
            graph[node.right].append(node)
            queue.append(node.right)
    visited = set([(target)])
    queue = deque([(target,0)])
    while queue:
        node,dist = queue.popleft()
        visited.add(node)
        if dist == k:
            res.append(node.val)
            continue 
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor,dist+1))
    return res 
        
def peakElement(nums):
    left = 0 
    right = len(nums)-2

    while left < right:
        mid = (left+right) // 2

        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid 
    return left 

def palindromicSubs(s:str)->int:
    count = 0 

    def expand(l,r):
        nonlocal count
        while l >= 0 and r < len(s) and s[l] == s[r]:
            count += 1
            l-=1
            r+=1
    
    for i in range(len(s)):
        expand(i,i)
        expand(i,i+1)
    
    return count 

def mergesortedarray(nums1,nums2,m,n):
    i = m - 1 # list1
    j = n - 1 # list2
    k = m + n - 1 #list3 

    while j >= 0:
        if i >=0 and nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

def kthmissing(nums,k):
    #missing = nums[i] - (i+1)
    left = 0 
    right = len(nums)-1

    while left <= right:
        mid = (left+right)//2

        missing = nums[mid] - (mid+1)

        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    return left + k 

def setZeroesMatrix(grid):
    rows = len(grid)
    cols = len(grid[0])

    first_row_zeroes = any(grid[0][j] == 0 for j in range(cols))
    first_col_zeroes = any(grid[i][0] == 0 for i in range(rows))

    #in the first pass, if we observe a zero we set edge cell to zero 
    for i in range(1,rows):
        for j in range(1,cols):
            if grid[i][j] == 0:
                grid[0][j] = 0
                grid[i][0] = 0 
    
    #in second pass if we obsere that a cell's edge is zero we set that cell to zero 
    for i in range(1,rows):
        for j in range(1,cols):
            if grid[0][j] == 0 or grid[i][0] == 0:
                grid[i][j] = 0 
    
    if first_row_zeroes:
        for j in range(cols):
            grid[0][j] = 0 
    if first_col_zeroes:
        for i in range(rows):
            grid[i][0] = 0 

def nextpermutate(nums):
    n = len(nums)
    i = n-2

    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1
    
    if i >= 0:
        j = n - 1
        while nums[j] >= nums[i]:
            j -= 1
        nums[i],nums[j] = nums[j],nums[i]
    
    left = i + 1
    right = n - 1

    while left < right:
        nums[left],nums[right] = nums[right],nums[left]
        left += 1
        right -= 1
    
def setMatrixZeros(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_zeroes = any(matrix[0][i] == 0 for i in range(cols))
    first_col_zeros = any(matrix[j][0] == 0 for j in range(rows))

    #marked for deletion
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][j] == 0:
                matrix[0][j] = 0
                matrix[i][0] = 0 
    #based off edge cells we zero the cells..
    for i in range(1,rows):
        for j in range(1,cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0 
    if first_row_zeroes:
        for i in range(cols):
            matrix[0][i] = 0
    if first_col_zeros:
        for i in range(rows):
            matrix[i][0] = 0 

def longestsequencenumbers(nums):
    longest = 0 

    num_sets = set(nums)

    for num in num_sets:
        if num-1 not in num_sets:
            length = 1
            while (num + length) in num_sets:
                length += 1
            longest = max(longest,length)
    
    return longest 

def groupStrings(strings):
    group_dictionary = defaultdict(list)

    for string in strings:
        if len(string) == 1:
            group_dictionary[(-1,)].append(string)
        else:
            i = 1 
            char_diffs = []

            while i < len(string):
                char_diffs.append(
                    (ord(string[i])-ord(string[i-1])) % 26
                )
                i += 1
            group_dictionary[tuple(char_diffs)].append(string)
    return list(group_dictionary.values())

def countShips(board):
    rows = len(board)
    cols = len(board[0])

    if not board or not board[0]:
        return 0

    count = 0 

    for r in range(rows):
        for c in range(cols):
            if board[r][c] != "X":
                continue
            
            if r > 0 and board[r-1][c] == "X":
                continue
            if c > 0 and board[r][c-1] == "X":
                continue 
            
            count += 1
    return count 

def groupStrings(strings):
    group_dict = defaultdict(list)

    for string in strings:
        if len(string) == 1:
            group_dict[(-1,)].append(string)
        else:
            i = 1
            char_diffs = []

            while i < len(string):
                char_diffs.append(
                    (ord(string[i])-ord(string[i-1])) % 26
                )
                i += 1
            group_dict[tuple(char_diffs)].append(string)
    return list(group_dict.values())

def longestSequence(nums):
    num_set = set(nums)
    longest = 0 

    for num in nums:
        if nums-1 not in num_set:
            length = 1

            while (num + length) in num_set:
                length += 1
            longest = max(longest,length)
    return longest 

def makingLargeIsland(self,grid):
    self.island_map = defaultdict(int)
    self.island_id = - 1
    self.directions = [(-1,0),(0,1),(1,0),(0,-1)]

    #depth first search that turns the island land into island ids and returns area
    def dfs(self,grid,r,c):
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1:
            grid[r][c] = self.island_id

            area = 1

            for dr,dc in self.directions:
                nr = r + dr
                nc = c + dc

                area += self.dfs(grid,nr,nc)
            
            return area 
        else:
            return 0 

    #main outer loop
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                island_area = self.dfs(grid,r,c)
                self.island_map[self.island_id] = island_area
                self.island_id -= 1
    max_area = 0
    #flip every zero
    for r in range(grid):
        for c in range(grid[0]):
            if grid[r][c] == 0:
                area = 1
                neighbors = set()

                for dr,dc in self.directions:
                    nr = r + dr
                    nc = c + dc

                    if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 0:
                        neighbors.add(grid[nr][nc])
                
                for island_id in neighbors:
                    area += self.island_area[island_id]
                
                max_area = max(max_area,area)
    return max_area if max_area else len(grid) ** 2


    

    
