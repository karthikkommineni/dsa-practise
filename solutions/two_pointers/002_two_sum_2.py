"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → N = number of elements in the list
Space: O(1) → Two-pointer uses constant space

*****************************************
"""

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        L, R = 0, len(numbers) - 1

        while L < R:
            s = numbers[L] + numbers[R]

            if s == target:
                return [L + 1, R + 1]  # 1-based indexing

            if s > target:
                R -= 1
            else:
                L += 1


"""
*************** GENERAL IDEA ***************

Use the two-pointer technique on a sorted array to find two numbers
that add up to the target.

*******************************************

*************** LOGIC **********************

1. Initialize two pointers:
   - L = 0 (start)
   - R = len(numbers) - 1 (end)

2. While L < R:
   - Calculate sum = numbers[L] + numbers[R]
   - If sum == target → return 1-based indices [L+1, R+1]
   - If sum > target → move R left to decrease sum
   - If sum < target → move L right to increase sum

*******************************************
"""
