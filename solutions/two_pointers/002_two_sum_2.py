"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → N = number of elements in the list
Space: O(1) → Two-pointer uses constant space

*****************************************
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # sorted - nlogn , t = x + y, x =! y, o(1) - space - no extra
        l, r = 0, len(numbers) - 1

        while l < r:
            num_sum = numbers[l] + numbers[r]
            if target == num_sum:
                return [l + 1, r + 1]
            elif num_sum > target:
                r -= 1
            else:
                l += 1


"""
- brute force - o(n2), o(1)
- code -optimize
- edge case
- trail run
"""

"""
*************** GENERAL IDEA ***************

Use the two-pointer technique on a sorted array to find two numbers
that add up to the target.

*******************************************
"""
