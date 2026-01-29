class RecentCounter:

    def __init__(self):
        self.Queue = []

    def ping(self, t: int) -> int:
        self.Queue.append(t) # append entry...
        
        while(self.Queue and self.Queue[0] < t - 3000):
            self.Queue.pop(0) #check the next one...
        return len(self.Queue)
    
recentCount = RecentCounter()
print(recentCount.ping(1))
print(recentCount.ping(100))
print(recentCount.ping(1000))
print(recentCount.ping(3001))
print(recentCount.ping(6001))

        
            




        
        