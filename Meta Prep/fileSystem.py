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
        elif op == "FIND_FILES":
            matches = []
            prefix = q[1]
            suffix = q[2]
            
            for path,(size,owner) in files.items():
                pathname = str(path)
                if(pathname.startswith(prefix) and pathname.endswith(suffix)):
                    matches.append((size,path))
                
                #sort by descending size then path...
            matches.sort(key=lambda x: (-x[0],x[1]))
            out.append(",".join(f"{path}({size})" for size,path in matches))
        elif op == "UPDATE_CAPACITY":
            user = q[1]
            new_capacity = int(q[2])
            
            if not user_exists(user):
                out.append("false")
            else:
                if user != "admin":
                    used_space = used[user]
                    if used_space > new_capacity:
                        out.append("false")
                    else:
                        users[user] = new_capacity
                        out.append("true")
                else:
                    out.append("true")
        elif op == "GET_FILE_SIZE":
            filepath = q[1]
            
            if filepath not in files:
                out.append("false")
            else:
                out.append(str(files[filepath][0]))
        elif op == "DELETE_FILE":
            filepath = q[1]
            if filepath not in files:
                out.append("false")
            else:
                (filesize,owner) = files[filepath]
                
                if owner != "admin":
                    used[owner] -= filesize
                
                del files[filepath]
                out.append(str(filesize))
               
                
            
                
            
            
            
            
                

                
                
                

            

            






