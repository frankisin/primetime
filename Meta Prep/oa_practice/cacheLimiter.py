from collections import deque

def solution(queries):
    out = []

    cache = {} # key : (value,expiresAt)
    writes = {} # userId : dequeue/list of write timestamps 
    limit = None #int (from Init)
    window = None #int (from Init)

    for q in queries:
        op = q[0]

        if op == "INIT":
            limit = int(q[1])
            window = int(q[2])
            out.append("true")
        elif op == "SET": 
            #SET userId time key value ttlSeconds
            #Sets cache[key] = value and expiration:
            #expiresAt = time + ttlSeconds
            userId = q[1]
            time = int(q[2])
            key = q[3]
            value = q[4]
            ttlSeconds = int(q[5])
            expiresAt = time + ttlSeconds

            #rate limiting (admin excempt)
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
        elif op == "DELETE":
            userId = q[1]
            time = int(q[2])
            key = q[3]
            
            if userId != "admin":
                if userId not in writes:
                    writes[userId] = deque()
                
                dq = writes[userId]
                cutoff = time - window

                #prune write list
                while dq and dq[0] <= cutoff:
                    dq.popleft()
                
                if len(dq) >= limit:
                    out.append("false")
                    continue

                dq.append(time)
            
            if key not in cache:
                out.append("false")
                continue

            value,expiresAt = cache[key]

            if time >= expiresAt:
                out.append("false")
                del cache[key]
                continue
            
            del cache[key]
            out.append("true")
        elif op == "GET": #(time,key)
            time = int(q[1])
            key = q[2]

            if key not in cache:
                out.append("")
            else:
                (value,expiresAt) = cache[key]
                if expiresAt <= time:
                    out.append("")
                else:
                    out.append(str(value))
        elif op == "COUNT": #(time)
            count = 0 
            time = int(q[1])
            for key in cache:
                value,expiresAt = cache[key]
                if time < expiresAt:
                    count += 1
            out.append(str(count))


                
            
                


    return out 

