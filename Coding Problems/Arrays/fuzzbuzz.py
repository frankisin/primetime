
def fizzbuzz(n):
    result = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result

print(fizzbuzz(15))
#For this problem we traverse all numbers from 1 to N using range(1,n+1)
#We need to check that i is divisible by 3 and 5 by doing i % 3 == 0 and i % 5 == 0 

