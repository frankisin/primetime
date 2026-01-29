def mergeStringsAlternatively(word1,word2)->str:
    result = ""
    m = len(word1)
    n = len(word2)

    i,j = 0,0 # initialize my pointers at the start

    while i < m and j < n:
        result += str(word1[i] + word2[j])
        i += 1
        j += 1
    #remainder...
    while i < m:
        result += word1[i]
        i += 1
    while j < n:
        result += word2[j]
        j += 1
    return result

word1 = "taco"
word2 = "bellll"

print(mergeStringsAlternatively(word1,word2))





  