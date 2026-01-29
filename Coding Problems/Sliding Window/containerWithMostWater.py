def containerWithMostWater(container):
    best = 0 
    left = 0 
    right = len(container) - 1

    while left < right : 
        leftHeight = container[left]
        rightHeight = container[right]

        containerVolume = min(leftHeight,rightHeight) * (right - left)

        best = max(best,containerVolume)

        if leftHeight < rightHeight : 
            left += 1
        else:
            right -= 1
    return best



height = [1,8,6,2,5,4,8,3,7]
print(containerWithMostWater(height))