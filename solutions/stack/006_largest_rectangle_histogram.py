"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N)     → Each bar is pushed and popped at most once
Space: O(N)     → Stack used to store indices

*****************************************

*************** GENERAL IDEA ***************

Use a **monotonic increasing stack** to track bars and compute area when the current bar breaks the increasing sequence.

- For each bar, if it's taller than the stack's top → push index.
- If shorter → keep popping and calculate area using the popped height as the smallest bar.

We also append a sentinel (index n) to flush out remaining bars in the stack.

*******************************************

***************** LOGIC ********************

1. Traverse the heights array including an extra iteration (n+1) with imaginary 0 height.
2. Maintain a stack to keep indices of increasing heights.
3. When current height is less than top of stack:
   - Pop the height
   - Compute width:
     - If stack is empty: width = i
     - Else: width = i - stack[-1] - 1
   - Compute area = height * width, update maxArea
4. Push current index `i` onto the stack.
5. Return `maxArea` after loop ends.

*******************************************
"""

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n or heights[i] < heights[stack[-1]]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)

        return maxArea
