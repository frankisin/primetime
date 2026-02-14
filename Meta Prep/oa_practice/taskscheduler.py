import heapq
def solution(queries):
    pq = []
    tasks = set()    
    out = []

    
    for q in queries:
        op = q[0]
        
        if op == "SCHEDULE": #taskId runAt priority
            taskId = q[1]
            runAt = int(q[2])
            priority = int(q[3])
            
            if taskId in tasks:
                out.append("false") #already been scheduled
                continue
            
            heapq.heappush(pq,(-priority,runAt,taskId))
            tasks.add(taskId)
            out.append("true")
            
        elif op == "CANCEL": #taskId
            taskId = q[1]
            
            if taskId not in tasks:
                out.append("false")
                continue
    
            out.append("true")
             
        elif op == "RUN": #time
            time = int(q[1])
            executed_tasks = []
            
            while pq:
                (-priority,runAt,taskId) = pq[0]
                
                if taskId not in tasks:
                    heapq.heappop(pq)
                    continue
                
                if runAt > time : 
                    break 
                
                executed_tasks.append(taskId)
                tasks.remove(taskId)
                heapq.heappop(pq)
                
            if len(executed_tasks) == 0:
                out.append("")
                continue
            
            out.append(",".join(executed_tasks))
        elif op == "NEXT_TASK": #time
            time = int(q[1])
            
            while pq:
                (-priority,runAt,taskId) = pq[0]
                
                if taskId not in tasks:
                    heapq.heappop(pq)
                    continue
                    
                if runAt > time:
                    out.append("")
                else:
                    out.append(taskId)
                break
            else:
                out.append("")
        else:
            out.append("")