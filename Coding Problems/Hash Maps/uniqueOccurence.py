def uniqueOccurrences(arr: list[int]) -> bool:
    dict = {}

    #first pass im going to construct my dictionary...
    for num in arr:
        dict[num] = dict.get(num,0) + 1
    
    values = dict.values()
    return len(values) == len(set(values))

nums = [2,2,3,3,1]

print(uniqueOccurrences(nums))