def reverseVowelsInString(word:str)->str:
    vowels = set("AEIOUaeiou")
    length = len(word)
    chars = list(word)

    left = 0 
    right = length - 1 

    while left < right:
        if chars[left] not in vowels:
            left += 1
        elif chars[right] not in vowels:
            right -= 1 
        else:
            chars[left],chars[right] = chars[right],chars[left]
            left += 1
            right -= 1
    return "".join(chars)
        
    
        
