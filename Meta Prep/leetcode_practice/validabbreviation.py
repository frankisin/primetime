def validAbbreviation(word,abbr):
    #rules:
    #we're going to implement two pointers, 
    #we're going to traverse about abbr 
    #Function should return false if rules are violated or if 
    #execution of abbreviation rules go out of bounds 
    i = 0 
    j = 0 

    n = len(word)
    m = len(abbr)

    while j < m : 
        if abbr[j].isalpha():
            if abbr[j] != word[i] and i <= n:
                return False 
            else:
                i += 1
                j += 1 
        else:

            if abbr[j] == '0':
                return False
            num = 0 
            while j < m and abbr[j].isdigit():
                num = num * 10 + (ord(abbr[j])-ord('0')) #ASCII 
                j += 1 
            i += num 
            
            if i > n: 
                return False 
    
    return i == n







