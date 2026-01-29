def numberPalindrome(n)->bool:

    number = str(n)
    length = len(number)

    if n < 0:
        return False
    for i in range(length // 2):
        left = number[i]
        right = number[length - 1 - i]

        if left != right:
            return False
    return True

#For this problem we implement the classic two pointer approach when left traverses up until the 
#middle of the dataset and right starts at the end and traverses to the middle...
#We check and compare the digits at every step and if they differ then this problem is not a palindrome...

