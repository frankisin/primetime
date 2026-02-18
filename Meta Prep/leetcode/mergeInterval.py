def mergeIntervals(intervals):
    if len(intervals) <= 1: # if there are 1 or 0 intervals then there is nothing to sort
        return intervals

    intervals.sort()

    res = [intervals[0]]

    for start,end in intervals[1:]:
        if start <= res[-1][1]:
            res[-1][1] = max(end,res[-1][1])
        else:
            res.append([start,end])
    return res 


