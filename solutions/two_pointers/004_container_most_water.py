"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → Single pass using two pointers
Space: O(1) → Constant space

*****************************************
"""

from typing import List

class Solution:
    def maxArea(self, h: List[int]) -> int:

        # v = (r - l) * min(h[l], h[r])
        # Always move the shorter line inward

        max_vol = 0
        l, r = 0, len(h) - 1

        while l < r:
            min_h = min(h[l], h[r])
            max_vol = max(max_vol, (r - l) * min_h)

            if min_h == h[r]:
                r -= 1
            else:
                l += 1

        return max_vol

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
