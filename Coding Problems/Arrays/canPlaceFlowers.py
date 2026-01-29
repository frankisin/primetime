def canPlaceFlowers(flowers,flowerBed)->bool:
    n = len(flowerBed)
    flowersPlaced = 0

    for i in range(n):
        left = (i == 0) or (flowerBed[i-1] == 0)
        right = (i == n-1) or (flowerBed[i+1] == 0)

        if left and right:
            flowerBed[i] = 1 # place the flower...
            flowersPlaced += 1

            if flowersPlaced >= flowers:
                return True 
    if flowers == 0:
        return True
    return False 

flowerBed = [0,1,0,1,0]
flowers = 2

print(canPlaceFlowers(flowers,flowerBed))

