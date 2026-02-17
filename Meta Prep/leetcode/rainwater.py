def trap(heights):
    n = len(heights)
    l = 0 
    r = n-1
    
    max_left = 0 
    max_right = 0 
    
    res = 0 
    
    
    while l < r:
        if heights[l] < heights[r]:
            if heights[l] > max_left:
                max_left = heights[l]
            else:
                res += max_left - heights[l]
            l += 1 
        else:
            if heights[r] > max_right:
                max_right = heights[r]
            else:
                res += max_right - heights[r]
            r-=1 
    return res 