from typing import List


class Solution:
    def has_duplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)

"""
#brute force - o(n2)
#sorting - o(nlogn)
#hashing - o(n)
#hashing
    def has_duplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            seen.add(num)
        return len(nums) != len(seen)
        
"""



