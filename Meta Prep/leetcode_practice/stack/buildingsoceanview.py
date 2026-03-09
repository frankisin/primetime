def findBuildings(heights):
    res = []
    
    max_height = float('-inf')
    
    for i in range(len(heights)-1,-1,-1):
        height = heights[i]
        
        if height > max_height:
            res.append(i)
            max_height = height 
    return res[::-1]


        
        
        
    
    