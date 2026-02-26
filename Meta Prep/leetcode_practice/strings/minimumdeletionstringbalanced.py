def minimumDeletionBalancedString(chars:str):
    b_count = 0 
    deletions = 0 


    for char in chars:
        if char == "b":
            b_count += 1
        else:
            deletions = min(deletions + 1,b_count)
    return deletions