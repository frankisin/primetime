def myAtoi(self, s: str) -> int:
    i = 0 
    n = len(s)

    INT_MAX = 2**32-1
    INT_MIN = -2**32

    sign = 1
    num = 0 

    while i < n and s[i] == " ":
        i += 1
    
    if i == n:
        return 0
    
    if s[i] == "+":
        sign = 1
        i += 1
    elif s[i] == "-":
        sign = -1
        i += 1
    
    while i < n and s[i].isdigit():
        digit = ord(s[i]) - ord('0')

        if num > INT_MAX // 10 or (num == INT_MAX // 10 and digit > INT_MAX % 10 ):
            if sign == 1:
                return INT_MAX
            elif sign == -1:
                return INT_MIN
        
        num = num * 10 + digit
        i += 1
    return sign * num 