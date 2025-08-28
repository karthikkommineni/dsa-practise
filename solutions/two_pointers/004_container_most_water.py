"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → Single pass using two pointers
Space: O(1) → Constant space

*****************************************
"""

from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # heights of bars, max vol - max(length of short bar out of two x width)

        l, r = 0, len(heights) - 1
        max_vol = 0

        while l < r:
            vol = min(heights[l], heights[r]) * (r - l)
            if heights[l] < heights[r]:  # only changin shorter length can increase vol
                curr_height = heights[l]
                l += 1
                # while l < r and heights[l] <= curr_height:  micro optimized
                #     l += 1
            else:
                curr_height = heights[r]
                r -= 1
                # while l < r and heights[r] <= curr_height:
                #     r -= 1
            max_vol = max(vol, max_vol)
        return max_vol

    # vol - 1*7, max - 7 - l+


# vol - 6*6 max -36 - r-,r-


"""
-bf, optz, edge,dryrun
- bf - o(n2) - eliminate few case with two pointer
- move pointer on shorter side because potential to increase 
vol by decreasing width is when height is more
- search for taller height

"""

"""
*************** GENERAL IDEA ***************

Use two-pointer approach to calculate area between lines.
Maximize area by moving inward from both ends, always
moving the shorter line to potentially find taller one.

*******************************************

*************** LOGIC **********************

1. Initialize two pointers `l` (left) and `r` (right).
2. Calculate area as: `(r - l) * min(h[l], h[r])`.
3. Track the maximum area seen so far.
4. Move the pointer pointing to the shorter height:
   - If `h[l] < h[r]`, move `l += 1`
   - Else move `r -= 1`
5. Repeat until pointers meet.

*******************************************
"""
