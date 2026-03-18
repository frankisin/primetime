class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0 
        sign = '+'

        n = len(s)

        for i,char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in "+-/*" or i == n-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(int(stack.pop() * num))
                elif sign == "/":
                    stack.append(int(stack.pop() / num))
                
                sign = char
                num = 0 
        return sum(stack)

