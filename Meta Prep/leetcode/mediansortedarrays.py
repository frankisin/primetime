class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        A,B = nums1,nums2

        if len(A) > len(B): # we need A to be shorter 
            A,B = B,A
        
        m,n = len(A),len(B)

        total = (m + n)

        half = (total + 1) // 2 # we want half to contain one more element (we want it to hold the median when the set is odd)

        #partition indexes
        low = 0 
        high = m 

        while low <= high:
            i = (low + high) // 2
            j = half - i 

            Aleft  = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i]     if i < m else float("inf")
            Bleft  = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j]     if j < n else float("inf")

            # correct partition
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return float(max(Aleft, Bleft))
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2.0

            # move left in A
            if Aleft > Bright:
                high = i - 1
            else:
                low = i + 1





