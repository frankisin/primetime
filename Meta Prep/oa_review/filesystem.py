def solution(queries):
    users = {} #userId : capacity
    used = {}  #userId : capacityUsed
    files = {} #path : (size,owner)

    out = []

    def user_exists(userId):
        return userId == "admin" or userId in users
    def path_exists(path):
        return path in files

    for q in queries:
        op = q[0]

        if op == "ADD_USER":
            userId = q[1]
            capacity = int(q[2])

            if not user_exists(userId):
                out.append("false")
            else:
                users[userId] = capacity
                used[userId] = 0 
                out.append("true")
        elif op == "ADD_FILE": #userId,path,size
            userId = q[1]
            path = q[2]
            size = int(q[3])

            if not user_exists(userId):
                out.append("false")
                continue

            if path_exists(path):
                out.append("false")
                continue

            capacityUsed = used[userId]
            capacity = users[userId]

            if userId != "admin" (size + capacityUsed > capacity):
                out.append("false")
                continue

            files[path] = (size,userId)
            used[userId] += size
            out.append("false")
        elif op == "DELETE_FILE": #path
            path = q[1] 

            if not path_exists(path):
                out.append("false")
                continue

            (size,owner) = files[path]

            del files[path]
            if owner != "admin":
                used[userId] -= size
            out.append(str(size))
        elif op == "GET_FILE_SIZE": #path
            path = q[1]

            if not path_exists(path):
                out.append("false")
                continue

            (size,owner) = files[path]

            out.append(str(size))
        elif op == "MOVE_FILE": #userId sourcePath destPath
            userId = q[1] 
            srcPath = q[2]
            destPath = q[3]

            if srcPath not in files or destPath in files:
                out.append("false")
                continue
            
            if not user_exists(userId):
                out.append("false")
                continue

            (size,owner) = files[srcPath]
            if userId == "admin" or userId == owner:
                files[destPath] = (size,owner)
                del files[srcPath]
                out.append("true")
                continue 
        elif op == "UPDATE_CAPACITY": #userId newCapacity 
            userId = q[1]
            new_capacity = int(q[2])

            capacity_used = used[userId]

            if not user_exists(userId):
                out.append("false")
                continue

            if userId != "admin":
                if capacity_used > new_capacity:
                    out.append("false") 
                    continue
                
                users[userId] = new_capacity
                out.append("true")
       






            

            

                
                
            
            


        

