from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        # Always binary search the smaller array
        if len(A) > len(B):
            A, B = B, A

        m, n = len(A), len(B)
        total = m + n
        half = (total + 1) // 2  # left side size

        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2      # cut in A
            j = half - i            # cut in B

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
                hi = i - 1
            else:
                lo = i + 1

        # Should never reach here if inputs are valid
        raise ValueError("Input arrays are not sorted or invalid.")