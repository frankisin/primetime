def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num not in seen:
            seen.add(num)
        else:
            return True #we've seen it already return False
    return False