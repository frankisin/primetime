def addBinary(a,b):
    i = len(a) - 1
    j = len(b) - 1

    result = []
    carry = 0 

    while i >= 0 or j >= 0 or carry:
        
        bit_a = a[i] if i >= 0 else 0 
        bit_b = b[j] if i >=0 else 0 

        total = bit_a + bit_b + carry

        result.append(str(total%2))

        carry = total // 2 

        i -= 1
        j -= 1
    return ''.join(reversed(result))
    


