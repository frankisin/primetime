def mergeSortedLists(list1,list2):
    i = 0
    j = 0 

    m = len(list1)
    n = len(list2)

    merged = []

    while(i < m and j < n):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    while( i < m ):
        merged.append(list1[i])
        i += 1
    while( j < n ): 
        merged.append(list2[j])
        j+= 1
    return merged 



