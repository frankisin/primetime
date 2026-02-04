from collections import deque 
def solution(queries):
    cache = {} #key(str) : (value(str) : expiresAt(int))
    writes = {}#userId(str) : deque(int)

    limit = None
    window = None
    
    out = []

    for q in queries:
        op = q[0]

        if op == "_INIT":#limit windowSeconds
            limit = int(q[1])
            window = int(q[2])

            out.append("true")
        elif op == "_SET": #userId time key value ttlSeconds
            userId = q[1]
            time = int(q[2])
            key = q[3]
            value = q[4]
            ttlSeconds = int(q[5])

            expiresAt = time + ttlSeconds

            if userId != "admin":

                if userId not in writes:
                    writes[userId] = deque()
                
                dq = writes[userId]
                cutoff = time - window 

                while dq and dq[0] <= cutoff:
                    dq.popleft()
                
                if len(dq) >= limit:
                    out.append("false")
                    continue 
                dq.append(time)

            cache[key] = (value,expiresAt)
            out.append("true")
        elif op == "_DELETE": #userId time key
            userId = q[1]
            time = int(q[2])
            key = q[3]
            
            if userId != "admin":
                if userId not in writes:
                    writes[userId] = deque()
                
                cutoff = time - window 
                
                dq = writes[userId]
                
                while dq and dq[0] <= cutoff:
                    dq.popleft()
                
                if(len(dq) >= limit):
                    out.append("false")
                    continue 
                dq.append(time)
                
            if key not in cache:
                out.append("false")
                continue
            
            (value,expiresAt) = cache[key]
            
            if expiresAt <= time:
                del cache[key]
                out.append("false")
                continue 
            
            del cache[key]
            out.append("true")
        elif op == "_GET": #time key
            time = int(q[1])
            key = q[2]
            
            if key not in cache:
                out.append("")
                continue 
            
            (value,expiresAt) = cache[key]
            
            if expiresAt <= time:
                out.append("")
                del cache[key]
                continue 
            
            out.append(str(value))
        elif op == "_COUNT": #time
            count = 0 
            delResults = []
            time = int(q[1])
            
            for key in cache:
                (value,expiresAt) = cache[key]
                if expiresAt <= time:
                    delResults.append(key)
                else:
                    count += 1
            
            for key in delResults:
                del cache[key]       
            out.append(str(count))
        
        if op == "__INIT": #limit windowSeconds
            limit = int(q[1])
            window = int(q[2])
            
            out.append("true")
        elif op == "__SET": #userId time key value ttlSeconds
            userId = q[1]
            time = int(q[2])
            key = q[3]
            value = q[4]
            ttlSeconds = int(q[5])
            
            expiresAt = time + ttlSeconds
            
            #if user is not admin, we need to enforce rate limits
            if userId != "admin":
                if userId not in writes:
                    writes[userId] = deque()
                
                dq = writes[userId]
                cutoff = time - window
                
                while dq and dq[0] <= cutoff:
                    dq.popleft()
                
                if len(dq) >= limit:
                    out.append("false")
                    continue 
                
                dq.append(time)
            cache[key] = (value,expiresAt)
            out.append("true")
        elif op == "__DELETE": #userId time key
            userId = q[1]
            time = int(q[2])
            key = str(q[3])
   
            if userId != "admin":
                
                if userId not in writes:
                    writes[userId] = deque()
                         
                cutoff = time - window
                dq = writes[userId]
                
                while dq and dq[0] <= cutoff:
                    dq.popleft()
                    
                if len(dq) >= limit:
                    out.append("false") # limit reached operation cannot be facilitated...
                    continue 
                
                dq.append(time)
            
            if key not in cache:
                out.append("false")
                continue 
            
            (value,expiredAt) = cache[key]
            if time >= expiredAt:
                del cache[key]
                out.append("false")
                continue
                
            del cache[key]
            out.append("true")
        elif op == "__GET": #time key
            time = int(q[1])
            key = str(q[2])
            
            if key not in cache: 
                out.append("")
                continue
            
            (value,expiredAt) = cache[key]
            
            if expiredAt <= time:
                out.append("")
                del cache[key]
                continue
            
            out.append(str(value))
        elif op == "__COUNT": #time
            time = int(q[1])
            count = 0
            deleted_key = []
            
            for key in cache:
                (value,expiredAt) = cache[key]
                
                if expiredAt <= time:
                    deleted_key.append(key)
                else:
                    count += 1
            
            for key in deleted_key:
                del cache[key]
            
            out.append(str(count))
        
        if op == "INIT":#limit windowSeconds:
            limit = int(q[1])
            window = int(q[2])

            out.append("true")

        elif op == "SET": #userId time key value ttlSeconds
            userId = q[1]
            time = int(q[2])
            key = q[3]
            value = q[4]
            ttlSeconds = int(q[5])

            expiresAt = time + ttlSeconds
            if userId != "admin":

                if userId not in writes:
                    writes[userId] = deque()

                dq = writes[userId]

                cutoff = time - window 

                #purge writes 
                while dq and dq[0] <= cutoff:
                    dq.popleft()
                #enforce limit 
                if len(dq) >= limit:
                    out.append("false")
                    continue 
                dq.append(time)
            
            cache[key] = (value,expiresAt)
            out.append("true")
        elif op == "DELETE": #userId time key
            userId = q[1]
            time = int(q[2])
            key = q[3]

            if userId != "admin":
                if userId not in writes:
                    writes[userId] = deque()
                
                dq = writes[userId]

                cutoff = time - window

                while dq and dq[0] <= cutoff:
                    dq.popleft()

                if len(dq) >= limit:
                    out.append("false")
                    continue

                dq.append(time)

            if key not in cache:
                out.append("false")
                continue 

            (value,expiresAt) = cache[key]

            if expiresAt <= time:
                out.append("false")
                del cache[key]
                continue

            del cache[key]
            out.append("true")
        elif op == "GET": #time key
            time = int(q[1])
            key = q[2]

            if key not in cache:
                out.append("false")
                continue 

            (value,expiredAt) = cache[key]
            if expiredAt <= time:
                out.append("false")
                del cache[key]
                continue
            out.append(str(value))
        elif op == "COUNT": #time
            pass
                    
                    
                    
                    
                    
            
            
            
            
                    
                    
                           
                 
            
            
            
            
                             
            
               
            
                
                
            





        

