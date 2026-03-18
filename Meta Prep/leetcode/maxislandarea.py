class Solution:
    def largestIsland(self,grid):
        self.island_id = -1
        self.island_areas = {}

        self.directions = [(-1,0),(1,0),(0,1),(0,-1)]

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    island_area = self.dfs(grid,m,n)

                    self.island_areas[self.island_id] = island_area

                    self.island_id -= 1
        max_area = 0 

        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 0:
                    area = 1

                    surrounding = set()

                    for dr,dc in self.directions:
                        nr = m + dr
                        nc = n + dc

                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] != 0:
                            surrounding.add(grid[nr][nc])
                    
                    for island_id in surrounding:
                        area += self.island_areas[island_id]
                    max_area = max(max_area,area)
        return max_area if max_area else len(grid) ** 2
    def dfs(self,grid,m,n):
        if 0 <= m < len(grid) and 0 <= n <len(grid[0]) and grid[m][n] == 1:
            grid[m][n] = self.island_id