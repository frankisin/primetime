def maxVowels(str,k):
    vowels = {'a','e','i','o','u'}

    curr = str[:k]

    maxVowels,count = 0,0

    for ch in curr:
        if ch in vowels:
            count += 1
    maxVowels = count
    
    for i in range(k,len(str)):
        if str[i] in vowels:
            count += 1
        if str[i-k] in vowels:
            count -= 1

        maxVowels = max(maxVowels,count)
    return maxVowels


