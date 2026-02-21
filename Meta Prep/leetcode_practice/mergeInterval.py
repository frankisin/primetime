def mergeInterval(intervals):
    if len(intervals) <= 0:
        return intervals
    
    intervals = sorted(intervals,key=lambda x:(x[0],x[1]))

    res = [intervals[0]]

    for s,e in intervals[1:]:
        if s <= res[-1][1]:
            res[-1][1] = max(res[-1][1],[s,e])
        else:
            res.append([s,e])
    
    return res 

