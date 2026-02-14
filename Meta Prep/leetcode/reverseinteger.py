def reverse(self, x: int) -> int:
    INT_MAX = 2**31-1
    INT_MIN = -2**31

    sign = None

    if x < 0:
        sign = -1
    else:
        sign = 1

    x = abs(x)
    rev = 0 

    while x != 0:
        digit = x % 10 
        x = x // 10 

        #check for overflow 
        if rev > INT_MAX // 10 or (rev == INT_MAX // 10 and digit > 7):
            return 0 # overflow
        
        rev = rev * 10 + digit 

    if sign * rev <= INT_MAX and sign * rev >= INT_MIN:
        return sign * rev
    
    return 0 