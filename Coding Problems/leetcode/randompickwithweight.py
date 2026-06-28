import random
import bisect
class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.prefix = []
        running = 0 

        for num in w:
            running += num 
            self.prefix.append(running)
        
        self.total = running
    def pickIndex(self):
        """
        :rtype: int
        """
        target = random.randint(1,self.total)

        return bisect.bisect_left(self.prefix,target)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()