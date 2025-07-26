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
        nums_set = set(nums)  # To enable O(1) lookup
        max_len = 0

        for num in nums:
            if (num - 1) not in nums_set:  # Start of a new sequence
                length = 1
                while (num + length) in nums_set:
                    length += 1
                max_len = max(max_len, length)

        return max_len

"""
************** LOGIC ********************

1. Convert the list to a set for quick lookup.
2. Loop through each number:
   - If it's the start of a sequence (num - 1 not in set), begin counting.
   - Extend the count while num + 1, num + 2, ... exist.
3. Track the maximum sequence length found.

*****************************************
"""
