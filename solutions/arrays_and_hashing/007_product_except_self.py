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
    class Solution:
        def productExceptSelf_leftRightArr(self, nums: List[int]) -> List[int]:
            # product  = left x right
            # 1 2 4 6 -> 1, 1, 2, 6  * 48,24,6,1

            left, right = [1] * len(nums), [1] * len(nums)

            # left products
            for i in range(1, len(nums)):
                left[i] = left[i - 1] * nums[i - 1]

            # right producst
            for j in range(len(nums) - 2, -1, -1):
                right[j] = nums[j + 1] * right[j + 1]

            return [a * b for a, b in zip(left, right)]


        def productExceptSelf_singleArr(self, nums: List[int]) -> List[int]:
            n = len(nums)
            res = [1] * n  # This will hold the final result

            # Step 1: Fill res with left products
            for i in range(1, n):
                res[i] = res[i - 1] * nums[i - 1]

            # Step 2: Multiply with right products on the fly
            right = 1
            for i in range(n - 1, -1, -1):
                res[i] = res[i] * right
                right *= nums[i]  # accumulate right product

            return res

    """
    - idea : product is leftproduct * right product (alternate -single arr
    - iteration always uses positive indices only 
    """


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
