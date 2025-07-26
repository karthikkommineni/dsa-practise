from typing import List


class Solution:
    def has_duplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            seen.add(num)
        return len(nums) != len(seen)
