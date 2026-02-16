from collections import defaultdict
def topKelements(nums,k):
    d = defaultdict(int)
    result = []

    for num in nums:
        d[num] += 1

    sorted_nums = sorted(d.items(), key = lambda x: x[1],reverse=True)

    for i in range(k):
        result.append(sorted_nums[i][0])
    return result



nums = [5,5,2,1,6,7,3,3,4,4,4]

print(topKelements(nums,3))