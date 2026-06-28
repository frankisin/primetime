class SparseVector:
    def __init__(self,nums):
        self.map = {}
        
        for i,num in enumerate(nums):
            if num != 0:
                self.map[i] = num
        
    def dotProduct(self,vec):
        result = 0 
        
        if len(self.map) > len(vec.map):
            return vec.dotPorduct(self)
        
        for i,val in self.map.items():
            if i in vec.map:
                result += val * vec.map[i]

        return result 