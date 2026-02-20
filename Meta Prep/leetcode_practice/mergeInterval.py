#[[1,3],[2,6],[8,10],[15,18]]


def merge(intervals):
    if len(intervals) <= 1:
        return []
    
    intervals.sort()
    
    res = [intervals[0]]
    
    
    
    