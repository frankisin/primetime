from collections import deque

def asteroidCollision(asteroids):
    stack = deque([asteroids])
    survivor = []

    while stack:
        curr = stack.pop()
        if stack[-1] is None:
            survivor.append(curr)
            return 
        next = stack[-1]

        if abs(curr) == abs(next):
            survivor.append(curr)
            survivor.append(next)
            stack.pop()

        if curr < 0: # current asteroid is negative...
            if next > 0: # asteroid at top of stack is pos
                if abs(curr) > next: #current asteriod is larger  
                    survivor.append(curr)
                    stack.pop()
                else: 
                    survivor.append(next)
                    stack.pop()
            else: # next asteroid is also negative (they both survive)
                survivor.append(curr)
                survivor.append(next)
                stack.pop()
        else:            #current asteroid is positive 
            if next < 0: # asteroid at top of stack is negative
                if curr < abs(next): # current asteroid is smaller
                    survivor.append(next)
                    stack.pop()
                else: 
                    survivor.append(curr)
                    stack.pop()
            else: #both asteroids survive...(same direction)
                survivor.append(curr)
                survivor.append(next)
                stack.pop()
    return survivor

asteroids = [5,10,-5]

print(asteroidCollision(asteroids))


