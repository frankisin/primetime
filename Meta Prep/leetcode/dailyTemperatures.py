def dailyTemperatures(temps):
    n = len(temps)

    res = [0] * n
    stack = []

    for i,t in enumerate(temps):
        while stack and t > temps[stack[-1]]:
            prev = stack.pop()
            res[prev] = i - prev 
        stack.append(i)
    return res 




