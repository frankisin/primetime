class Solution:
    def compress(self,chars)->int:
        write = 0
        read = 0
        n = len(chars)
        
        while read < n:
            ch = chars[read]
            start = read 
            
            while read < n and chars[read] == ch:
                read += 1
            
            count = read-start
            
            chars[write] = ch
            write += 1
            
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        return write 