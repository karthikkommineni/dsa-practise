"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N)
Space: O(1) extra (excluding output list `res`)

*****************************************

************** GENERAL IDEA **************

To find the product of all elements except self without using division:
- Use two passes:
  1. First pass: build prefix product (left of index)
  2. Second pass: multiply with suffix product (right of index)
- Maintain one output array and one running variable for space efficiency.
- This avoids using division and handles zero values correctly.

*****************************************
"""

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]  # res[0] = 1 (no elements to the left)

        # Pass 1: Prefix product from left
        for i in range(1, len(nums)):
            res.append(nums[i - 1] * res[i - 1])

        prod = 1  # right-side running product

        # Pass 2: Multiply with suffix product from right
        for i in range(len(nums) - 2, -1, -1):
            prod *= nums[i + 1]
            res[i] *= prod

        return res

"""
************** LOGIC ********************

1. Initialize result array `res` with [1] as the first prefix.
2. Loop 1 (Left to Right):
   - At each index i, set res[i] = product of all nums[0..i-1]
3. Loop 2 (Right to Left):
   - Maintain running product of elements after index i.
   - Multiply current res[i] with this right-side product.
4. Avoids using division and works even if zeros are present.

*****************************************
"""
