class Solution:
    def insert(self, intervals,newInterval):
        res = []
        
        cur_idx = 0 
        
        if not intervals:
            return [newInterval]
        
        while cur_idx < len(intervals) and intervals[cur_idx][0] < newInterval[0]:
            res.append(intervals[cur_idx])
            cur_idx += 1 
        
        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1],newInterval[1])
        
        while cur_idx < len(intervals):
            cur_interval = intervals[cur_idx]
            
            if cur_interval[0] <= res[-1][1]: # does the new interval start before last merged interval ends? 
                res[-1][1] = max(res[-1][1],cur_interval[1])
            else:
                res.append(cur_interval)
            cur_idx += 1
        return res 
        