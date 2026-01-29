def kidsWithCandies(candies,extraCandies):
    result = []
    maximum = max(candies)

    for i in range(len(candies)):
        if candies[i] + extraCandies >= maximum:
            result.append(True)
        else:
            result.append(False)
    return result
    
candies = [4,2,1,1,2]
extraCandies = 2

print(kidsWithCandies(candies,extraCandies))


