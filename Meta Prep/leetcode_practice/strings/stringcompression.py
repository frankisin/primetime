def stringCompression(chars:str)->str:
    n = len(chars)
    read = 0 
    write = 0 

    while read < n:
        ch = chars[read]
        start = read 

        while read < n and chars[read] == ch:
            read += 1
        
        count = read - start 

        chars[write] = ch
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1
        
    return chars 