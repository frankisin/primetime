def jump(nums):
    jumps = 0 
    current_end = 0 
    farthest = 0
    
    for i in range(len(nums)-1):
        farthest = max(farthest,i + nums[i])
        
        if i == current_end: #we've reached the boundary of allowable jumps, compute next jump 
            jumps+=1
            current_end = farthest
            
    return jumps 