def validAbbreviation(word,abbr):
    i = 0 # pointer in word
    j = 0 # pointer in abbr

    n = len(word)
    m = len(abbr)

    while j < m:
        if abbr[j].isalpha():
            if i >= n or word[i] != abbr[j]:
                return False 
            i += 1
            j += 1
        else:
            if abbr[j] == '0':
                return False # zeros not allowed 
            
            num = 0 
            while j < m and abbr[j].isdigit():
                num = num * 10 + (ord(abbr[j]) - ord('0'))
                j += 1
            i += num 

            if i > n:
                return False
    return i == n