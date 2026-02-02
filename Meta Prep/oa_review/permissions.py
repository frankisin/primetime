def solution(queries):
    users = {} # userId (str) : roles set(roleName)
    roles = {} #roleName (str) : permissions set(permissions)

    out = []
    
    for q in queries:
        op = q[0]
        
        if op == "CREATE_ROLE" : #roleName
            roleName = q[1]

            if roleName in roles:
                out.append("false")
                continue

            roles[roleName] = set()
            out.append("true")
        elif op == "ADD_PERMISSION": #roleName permission
            roleName = q[1]
            permission = q[2]
            
            if roleName not in roles:
                out.append("false")
                continue 

            permissions = roles[roleName]

            if permission in permissions:
                out.append("false")
                continue

            permissions.add(permission) # add permission to the set 
            out.append("true")
        elif op == "CREATE_USER": #userId
            userId = q[1]

            if userId in users:
                out.append("false")
                continue

            users[userId] = set()
            out.append("true")
        elif op == "ASSIGN_ROLE": #userId roleName
            userId = q[1]
            roleName = q[2]

            if userId not in users or roleName not in roles:
                out.append("false")
                continue
            
            user_roles = users[userId]

            if roleName in user_roles:
                out.append("false")
                continue

            user_roles.add(roleName)
            out.append("true")




    
    