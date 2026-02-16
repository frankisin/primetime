def validAbbreviation(word,abbr):
    i=0
    j=0 
    n = len(word)
    m = len(abbr)

    while j < m:
        if abbr[j].isalpha():
            if i >= n or abbr[j] != word[i]:
                return False 
            else:
                j += 1
                i += 1
        else:
            if abbr[j] == '0':
                return False
            num = 0 
            while j < m and abbr[j].isdigit():
                num = num * 10 + (ord(abbr[j])-ord('0'))
                j += 1
            
            i += num

            if i > n:
                return False 
    return i == n 