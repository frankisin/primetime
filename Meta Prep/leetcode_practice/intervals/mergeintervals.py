def merge(intervals):
    if len(intervals) < 2:
        return intervals
    
    res = []
    
    intervals.sort()
    
    res.append(intervals[0])
    
    for start,finish in intervals[1:]:
        if start <= res[-1][1]: #start of new interval comes before the end of curr interval
            res[-1][1] = max(res[-1][1],finish)
        else:
            res.append([start,finish])
    
    return res