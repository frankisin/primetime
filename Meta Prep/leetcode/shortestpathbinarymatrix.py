from collections import deque

def shortestPathBinaryMatrix(grid):
    n = len(grid)

    if grid[0][0] != 0 or grid[n-1][n-1] != 0:
        return -1
    
    directions = [
        (-1,-1), (-1,0),(-1,1),
        (0,-1),         (0,1),
        (1,-1),  (1,0), (1,1)
    ]

    queue = deque([(0,0,1)])

    grid[0][0] = 1

    while queue:
        r,c,dist = queue.popleft()

        if r == n-1 and c == n-1:
            return dist 
        
        for dr,dc in directions:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 0:
                queue.append((nr,nc,dist+1))
                grid[nr][nc] = 1 #set it as visited...
    return -1 





   
