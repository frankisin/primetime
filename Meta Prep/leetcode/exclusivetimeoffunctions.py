class Solution:
    #This is a stack based execution simulation 
    #We're tracking time in between executions 
    def exclusiveTime(self,n,logs):
        stack = [] # (id)
        res = [0] * (n)
        prev_time = 0 
        
        for log in logs:
            op = log.split(":") #[id,op,timestamp]
            
            uid = int(op[0])
            otype = op[1]
            time_stamp = int(op[2])
            
            if otype == "start":
                ttl = time_stamp-prev_time
                
                if stack:
                    res[stack[-1]] += ttl
                    
                stack.append(uid)
                prev_time = time_stamp
            elif otype == "end":
                
                fid = stack.pop()
                
                execution_time = time_stamp - prev_time + 1
                
                res[fid] += execution_time
                            
                prev_time = time_stamp + 1
        return res
                
                
                
                
                
            
            
            
            
            
        
        