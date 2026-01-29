def solution(queries):
    users = {} #userId : capacity
    used = {} #userId : usedBytes
    files = {} #path : (size : int, owner : String)

    out = []

    def user_exists(userId):
        return userId == "admin" or (userId in users)

    def path_exists(path):
        return path in files
    
    for q in queries:
        op = q[0]

        if op == "ADD_USER":
            user = q[1]
            capacity = int(q[2])

            if not user_exists(user):
                users[user] = capacity #create user 
                used[user] = 0 
                out.append("true")
            else:
                out.append("false")
        elif op == "ADD_FILE":
            user = q[1]
            path = q[2]
            size = int(q[3])

            if not user_exists(user):
                out.append("false")
                continue
            else: 
                if not path_exists(path):
                    if user != "admin":
                        user_capacity = used[user]
                        max_user_capacity = users[user]

                        if size + user_capacity > max_user_capacity:
                            out.append("false")
                            continue
                        used[user] += size
                        
                
                    files[path] = (size,user)
                    out.append("true")
                else:
                    out.append("false")
                    

            

            






