class Solution:
    def cleanRoom(self,robot):
        visited = set()
        
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        
        def goback():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def dfs(x,y,d):
            visited.add((x,y)) #Add current node to visited...
            robot.clean()      #Have the robot clean the curr tile 
            
            #explore other tiles connected to this one for every direction
            
            for i in range(4):
                nd = (d + i) % 4 
                dx,dy = directions[nd]
                nx = x + dx
                ny = y + dy
                
                if(nx,ny) not in visited and robot.move():
                    dfs(nx,ny,nd)
                    goback()
                robot.turnRight()
        dfs(0,0,0)
                
                