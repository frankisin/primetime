from collections import deque 
def solution(queries):
    cache = {} #key(str) : (val(str): expiresAt(int) )
    writes = {} #userId : time (int)
    limit = None
    window = None 

    out = []

    for q in queries:
        op = q[0]

        if op == "INIT":#limit windowSeconds
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

                while dq and dq[0] <= cutoff:
                    dq.popleft()
                
                if len(dq) >= limit:
                    out.append("false")
                    continue 
                dq.append(time)

            cache[key] = (value,expiresAt)
            out.append("true")






        

