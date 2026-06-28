from collections import defaultdict

def groupanagrams(words):
    groups = defaultdict(list)
    
    for word in words:
        count = [0] * 26 
        
        for ch in word:
            count[ord(ch)-ord('a')] += 1
        
        groups[tuple(count)].append(word)
    
    return list(groups.values())

    