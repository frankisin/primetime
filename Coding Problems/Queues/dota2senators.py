from collections import deque 

def senators(sens):
    radiant = deque([])
    dire = deque([])
    length = len(sens)

    
    #populate radiant and dire queues...
    for i in range(length):
        if sens[i] == "R":
            radiant.append(i)
        elif sens[i] == "D":
            dire.append(i)
    
    while radiant and dire:
        #take the first element at each queue..
        curradiant = radiant[0]
        currdire = dire[0]

        if curradiant < currdire:
            #radiant senator goes first...
            print("Radiant's turn banning Dire")
            dire.popleft() #he will ban next dire...
            radiant.popleft() # remove it from the queue 
            radiant.append(curradiant + length) # append the senator to end of the queue...
        else: 
            #dire goes first...
            print("Dire's turn banning Radiant")
            radiant.popleft()
            dire.popleft()
            dire.append(currdire + length) 
            
            
    if(radiant):
        return "Radiant"
    elif(dire):
        return "Dire"


senate = "DRRDR"
print(senators(senate))
