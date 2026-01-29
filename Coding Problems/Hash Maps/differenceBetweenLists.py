def differenceBetweenLists(list1,list2):
        diff1 = set()
        diff2 = set()
        set1 = set(list1) 
        set2 = set(list2)

        for num in list1:
            if num not in set2:
                diff1.add(num)
        
        for num in list2:
            if num not in set1:
                diff2.add(num)
        
        return [list(diff1),list(diff2)]
