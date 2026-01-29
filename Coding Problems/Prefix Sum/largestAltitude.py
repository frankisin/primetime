def largestAltitude(gain):
    highest = 0 
    alt_sum = 0 

    for dy in gain:
        alt_sum += dy
        highest = max(alt_sum,highest)
    return highest
    
print(largestAltitude([-5, 1, 5, 0, -7]))
