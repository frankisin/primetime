def solution(queries):
    out = []

    accounts = {} #accountId (str): balance (int)

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
        elif op == "DEPOSIT": # accountId amount 
            accountId = q[1]
            amount = int(q[2])

            if not account_exists(accountId) or amount <= 0: # I'm assuming amount is always positive but just in case!
                out.append("false")
                continue

            accounts[accountId] += amount
            balance = str(accounts[accountId])
            out.append(balance)
        elif op == "WITHDRAW": #accountId amount
            accountId = q[1]
            amount = int(q[2])

            if not account_exists(accountId):
                out.append("false")
                continue

            balance = accounts[accountId]

            if balance < amount:
                out.append("false")
                continue 

            accounts[accountId] -= amount
            balance = accounts[accountId]
            out.append(str(balance))
        elif op == "TRANSFER": #fromAccountId toAccountId amount 
            fromAccountId = q[1]
            toAccountId = q[2]
            amount = int(q[3])
            
            if amount <= 0 or not account_exists(fromAccountId) or not account_exists(toAccountId) or fromAccountId == toAccountId:
                out.append("false")
                continue 

            balance = accounts[fromAccountId]
            if balance < amount:
                out.append("false")
                continue 

            accounts[toAccountId] += amount
            accounts[fromAccountId] -= amount

            balance = accounts[fromAccountId]

            out.append(str(balance))
        elif op == "_TOP_ACCOUNTS": #k 
            k = min(int(q[1]),len(accounts))
            matches = []
            output = []

            for account,balance in accounts.items():
                matches.append((account,balance))
            matches.sort(key=lambda x:(-x[1],x[0]))

            for i in range(k):
                output.append(matches[i])
                
            out.append(",".join(f"{account}({balance})" for account,balance in output))
        elif op == "TOP_ACCOUNTS": #k
            k = int(q[1])
            k = min(k,len(accounts))

            results = []

            for account,balance in accounts.items():
                results.append((account,balance))
            results.sort(key=lambda x:(-x[1],x[0]))

            results = results[:k]

            out.append(",".join(f"{account}({balance})" for account,balance in results))








            



