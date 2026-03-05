def customSortString(s:str,order:str):
    rank = {ch : i for i,ch in enumerate(order)}

    return ''.join(sorted(s,key = lambda ch: rank.get(ch,len(order))))