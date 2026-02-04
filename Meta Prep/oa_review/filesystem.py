def solution(queries):
    files = {} #path(str):(size(int),owner(str))
    users = {} #userId(str):capacity(int)
    used = {} #userId(str):capacityUsed(int)

    out = []

    def user_exists(userId):
        return userId == "admin" or userId in users
    def path_exists(path):
        return path in files

    for q in queries:
        op = q[0]

        if op == "_ADD_USER": #userId capacity
            userId = q[1]
            capacity = int(q[2])

            if not user_exists(userId):
                out.append("false")
            else:
                users[userId] = capacity
                used[userId] = 0 
                out.append("true")
        elif op == "_ADD_FILE": #userId,path,size
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

            if userId != "admin" and (size + capacityUsed > capacity):
                out.append("false")
                continue

            files[path] = (size,userId)
            if userId != "admin":
                used[userId] += size
            out.append("true")
        elif op == "_DELETE_FILE": #path
            path = q[1] 

            if not path_exists(path):
                out.append("false")
                continue

            (size,owner) = files[path]

            del files[path]
            if owner != "admin":
                used[userId] -= size
            out.append(str(size))
        elif op == "_GET_FILE_SIZE": #path
            path = q[1]

            if not path_exists(path):
                out.append("false")
                continue

            (size,owner) = files[path]

            out.append(str(size))
        elif op == "_MOVE_FILE": #userId sourcePath destPath
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
        elif op == "_UPDATE_CAPACITY": #userId newCapacity 
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
        
        if op == "ADD_USER": #userId capacity
            userId = q[1]
            capacity = int(q[2])

            if user_exists(userId):
                out.append("false")
                continue
            users[userId] = capacity
            used[userId] = 0 

            out.append("true")
        elif op == "ADD_FILE":
            userId = q[1]
            path = q[2]
            size = int(q[3])

            if not user_exists(userId):
                out.append("false")
                continue

            if path_exists(path):
                out.append("false")
                continue
            
            if userId != "admin" and userId in users:
                capacity = users[userId]
                capacity_used = used[userId]

                if size + capacity_used > capacity:
                    out.append("false")
                    continue 

                used[userId] += size

            files[path] = (size,userId)
            out.append("true")
        elif op == "DELETE_FILE":
            path = q[1]

            if not path_exists(path):
                out.append("false")
                continue 
            
            (size,owner) = files[path] # assuming size comes back int
            
            if owner != "admin":
                used[owner] -= size
            
            del files[path] 
            out.append(str(size))
        elif op == "GET_FILE_SIZE":
            path = q[1] 
            
            if not path_exists(path):
                out.append("false")
                continue
            
            (size,owner) = files[path]
            out.append(str(size))

        elif op == "MOVE_FILE":
            userId = q[1]
            sourcePath = q[2]
            destPath = q[3]

            if not user_exists(userId) or not path_exists(sourcePath) or path_exists(destPath):
                out.append("false")
                continue

            (size,owner) = files[srcPath]

            if userId != "admin" and owner != userId:
                out.append("false")
                continue

            files[destPath] = (size,owner)
            del files[sourcePath]

            out.append("true")

        elif op == "UPDATE_CAPACITY":
            userId = q[1]
            new_capacity = int(q[2])

            if not user_exists(userId):
                out.append("false")
                continue

            if userId != "admin":
                capacity_used = used[userId]
                if capacity_used > new_capacity:
                    out.append("false")
                    continue
                users[userId] = new_capacity
            out.append("true")

        elif op == "FIND_FILES": #prefix suffix
            prefix = q[1]
            suffix = q[2]
            res = []
            
            for path in files:
                path_name = str(path)
                (size,owner) = files[path_name]
                if path_name.startswith(prefix) and path_name.endswith(suffix):
                    res.append((path_name,(int(size))))
            if len(res) == 0:
                out.append("")
                continue
            res.sort(key = lambda x:(-x[1],x[0]))
            out.append(",".join(f"{path}({size})" for path,size in res))
        else:
            out.append("")




            

            

                
                
            
            


        

