def numIslands(grid):
    num_islands = 0 

    directions = [(1,0),(-1,0),(0,1),(0,-1)]

    def setIslandZeros(grid,r,c):
        if(0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1"):
            grid[r][c] = "0"

            for row_inc,col_inc in directions:
                setIslandZeros(grid,r + row_inc,c + col_inc)


    for row in range(len(grid)): 
        for col in range(len(grid[0])):
            if grid[row][col] == "1":
                num_islands+= 1

                setIslandZeros(grid,row,col)
    return num_islands