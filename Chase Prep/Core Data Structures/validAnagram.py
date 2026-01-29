def isAnagram(string1:str,string2:str):
    seen1 = {}
    seen2 = {}

    for char in string1: #O(n + m)
        if char in seen1:
            seen1[char] += 1
        else:
            seen1[char] = 1
    
    for char in string2:
        if char in seen2:
            seen2[char] += 1
        else:
            seen2[char] = 1 

    return seen1 == seen2
