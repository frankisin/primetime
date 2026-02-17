from collections import defaultdict
def isIsomorphic(s,t)->bool:
    mapST = {}
    mapTS = {}
    
    res = False
    
    if len(s) != len(t):
        return res 
    
    for c1, c2 in zip(s, t):
        
        if c1 in mapST and mapST[c1] != c2:
            return False 

        if c2 in mapTS and mapTS[c2] != c1:
            return False 
        
        mapST[c1] = c2
        mapTS[c2] = c1 

    res = True 
    return res
