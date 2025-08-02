"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → Each number is visited at most once
Space: O(N) → Set to store all unique numbers

*****************************************

************** GENERAL IDEA **************

To find the longest sequence of consecutive integers:
- Add all numbers to a set for O(1) lookups.
- Only start counting when the number is the beginning of a sequence (i.e., num-1 is not in the set).
- Extend the streak while next numbers exist in the set.
- Track and update the maximum streak.

This avoids sorting (which is O(N log N)) and ensures linear time.

*****************************************
"""

from typing import List

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:

        seen = set(nums)
        max_len = 0

        for i in range(len(nums)):
            n = nums[i]
            if n - 1 not in seen:
                length = 1
                while n + length in seen:
                    length += 1
                max_len = max(length, max_len)
            else:
                continue

        return max_len

    """
    - The elements do not have to be consecutive in the original array - hence we can use hashing
    - start count only if its frist num in seq - means n-1 wont exists
    - count increase as long as next number  exists
    - dont have to see it as one list - 
    seq can number exist or not is enough logic
    """

"""
************** LOGIC ********************

1. Convert the list to a set for quick lookup.
2. Loop through each number:
   - If it's the start of a sequence (num - 1 not in set), begin counting.
   - Extend the count while num + 1, num + 2, ... exist.
3. Track the maximum sequence length found.

*****************************************
"""
