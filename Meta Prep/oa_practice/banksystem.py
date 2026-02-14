def solution(queries):
    accounts = {} #accountId(str):balance(int)
    out = []
    
    def account_exists(accountId):
        return accountId in accounts
    
    for q in queries:
        op = q[0]
        
        if op == "CREATE_ACCOUNT": #accountId
            accountId = q[1]
            
            if account_exists(accountId):
                out.append("false")
                continue
            
            accounts[accountId] = 0 
            out.append("true")
            
        elif op == "DEPOSIT": #accountId amount
            accountId = q[1]
            amount = int(q[2])
            
            if not account_exists(accountId):
                out.append("false")
                continue
            
            account_balance = accounts[accountId]
            
            accounts[accountId] += amount
            
            out.append(str(account_balance+amount))
            
        elif op == "WITHDRAW": #accountId amount
            accountId = q[1]
            amount = int(q[2])
            
            if not account_exists(accountId) or amount <= 0:
                out.append("false")
                continue
            
            account_balance = accounts[accountId]
            
            if account_balance < amount:
                out.append("false")
                continue
            
            accounts[accountId] -= amount
            
            new_balance = accounts[accountId]
            
            out.append(str(new_balance))
            
        elif op == "TRANSFER": #fromAccountId toAccountId amount
            fromAccountId = q[1]
            toAccountId = q[2]
            amount = int(q[3])
            
            if amount <= 0 or not account_exists(fromAccountId) or not account_exists(toAccountId) or fromAccountId == toAccountId:
                out.append("false")
                continue
            from_balance = accounts[fromAccountId] # assuming int 
            if from_balance < amount:
                out.append("false")
                continue 
            
            accounts[fromAccountId]-= amount
            accounts[toAccountId]+= amount
            
            new_balance = accounts[fromAccountId]
            out.append(str(new_balance))
            
        elif op == "TOP_ACCOUNTS":#k 
            k = int(q[1])
            fetched = []
            
            if len(accounts) == 0:
                out.append("")
                continue
            
            for account,balance in accounts.items():
                fetched.append((account,balance))
            fetched.sort(key = lambda x:(-x[1],x[0]))
            fetched = fetched[:k]
            
            out.append(",".join(f"{account}({balance})" for account,balance in fetched))
            
            
        
    
    