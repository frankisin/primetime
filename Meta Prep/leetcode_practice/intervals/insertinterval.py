def insert_interval(intervals,newInterval):
    if not intervals:
        return [newInterval]
    
    res = []
    i = 0 
    #intervals prior to new intervals...
    while i < len(intervals) and intervals[i][1] < newInterval[0]:
        res.append(intervals[i])
        i += 1
    #interval at the edge of merge 
    if not res or res[-1][1] < newInterval[0]:
        res.append(newInterval)
    else:
        res[-1][1] = max(res[-1][1],newInterval[1])
    #intervals after the merge 
    while i < len(intervals):
        curr = intervals[i]

        if curr[0] <= res[-1][1]:
            res[-1][1] = max(res[-1][1],curr[1])
        else:
            res.append(curr)
        i += 1
    return res 