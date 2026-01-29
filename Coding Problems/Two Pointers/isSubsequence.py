#for this problem were traversing all the characters in our string t
#and were indexing our substring, if there's a match and index is in bounds
#increment i and if we've reached the end of bounds, the entire substring is 
#in the string and we return true, otherwise return false.
#   
#
def isSubsequence(t:str,s:str)->bool:
    #t - string were checking against
    #s - substring were checking for
    i = 0           #index for substring s
    n = len(s)      #length of substring n

    for char in t:
        if(i < n and char == s[i]):
            i+=1
            if i == n:
                return True
                
    return False
