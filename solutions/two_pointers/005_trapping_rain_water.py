"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → Single pass through height array
Space: O(1) → Constant extra space (no extra arrays used)

*****************************************
"""

from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        #+ve,
        l,r = 0, len(heights)-1

        left_max,right_max,water = heights[l],heights[r],0

        while l < r:

            if left_max < right_max:
                water += left_max - heights[l]
                l+=1
                left_max = max(heights[l],left_max)
            else:
                water += right_max - heights[r]
                r-=1
                right_max = max(heights[r],right_max)

        return water

    #sol 2 - cleaner version
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        ans = 0

        while l < r:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max <= right_max:
                ans += left_max - height[l]
                l += 1
            else:
                ans += right_max - height[r]
                r -= 1

        return ans

"""
*************** GENERAL IDEA ***************
- calculate left_max - at that bar - max of left till that point including the heigt of curr bar
- similarly right_bar
- compare left_max and right_max - to know which side to start calculating water on that bar
- if left_max<right_max:
    scenario1: actual right_max > left_max --- no issue as we want lower boundary only
    scenario2: actual right_max < left_max -- still the water on that bar wont change

*******************************************

*************** LOGIC **********************
Intuition (Two Pointers + Loop Invariant)

Definitions
- left_max  := max(heights[0..l])      # best wall seen so far from the left (inclusive)
- right_max := max(heights[r..n-1])    # best wall seen so far from the right (inclusive)

Decision Rule
- If left_max <= right_max:
    - The left side is the limiting wall now.
    - Water at index l is exactly (left_max - heights[l]); add it, then l += 1.
- Else:
    - The right side is the limiting wall.
    - Water at index r is exactly (right_max - heights[r]); add it, then r -= 1.

Why comparing maxes is correct
- For current l, the true right maximum over (l+1..n-1) is >= right_max.
  If left_max <= right_max, then min(left_max, trueRightMax(l)) = left_max,
  so water at l depends only on left_max. Symmetric argument for the right.
- We do NOT need the exact far-side maximum at every index—only which side is
  the smaller bound right now.

Edge Cases & Guarantees
- Length < 3 ⇒ 0 water.
- Subtractions are non-negative because left_max ≥ heights[l] and right_max ≥ heights[r].

Complexity
- Time: O(n) single pass
- Space: O(1)

*******************************************
"""
