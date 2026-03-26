class blind:
    def validWordAbbrev(self,word,abbr):
        i,j = 0,0
        m = len(abbr)
        n = len(word)

        while j < m :
            if abbr[j].isalpha():
                if i >= n or abbr[j] != word[i]:
                    return False
                i += 1
                j += 1
            else:
                if abbr[j] == "0":
                    return False # no leading zeros
                
                num = 0 

                while j < m and abbr[j].isdigit():
                    num = num * 10 + (ord(abbr[j])-ord('0'))
                    j += 1
                
                i += num

                if i > n:
                    return False # out of bounds
        return i == n
    def validPalindrome(s:str)->bool:
        left = 0 
        right = len(s)-1

        while left < right:
            if s[left] != s[right]:
                return False 
            left +=1
            right -=1

        return True 
    
    def validParenthesis(s:str):

