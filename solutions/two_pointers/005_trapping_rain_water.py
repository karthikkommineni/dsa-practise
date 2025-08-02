"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → Single pass through height array
Space: O(1) → Constant extra space (no extra arrays used)

*****************************************
"""

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]

        return res

"""
*************** GENERAL IDEA ***************

Water trapped at any index depends on the shorter of the
tallest bars on left and right. Using two pointers with
tracked max heights allows computing trapped water in one pass.

*******************************************

*************** LOGIC **********************

1. Initialize two pointers `l` and `r` at both ends.
2. Track `leftMax` and `rightMax` for current boundaries.
3. Move the pointer at the smaller max height inward:
   - If `leftMax < rightMax`: update `leftMax`, compute trapped water.
   - Else: update `rightMax`, compute trapped water.
4. Add the difference between current max and height at index.
5. Repeat until both pointers meet.

*******************************************
"""
