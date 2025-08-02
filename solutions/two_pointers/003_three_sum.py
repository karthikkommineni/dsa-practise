"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N^2) → Outer loop + two-pointer scan
Space: O(1)   → Ignoring output list

*****************************************
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Sorting helps eliminate duplicates and apply 2-pointer

        for i, a in enumerate(nums):
            if a > 0:
                break  # Since array is sorted, no possible triplet after this

            if i > 0 and a == nums[i - 1]:
                continue  # Skip duplicate values for 'a'

            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # Skip duplicate values for 'l'
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        return res

"""
*************** GENERAL IDEA ***************

Find all unique triplets in array that sum to zero using:
1. Sorting
2. Two-pointer scanning for each fixed first element

*******************************************

*************** LOGIC **********************

1. Sort the array
2. Iterate each index `i` with value `a`:
   - If `a > 0`, break (no further triplets can sum to 0)
   - If `a` is same as previous, skip to avoid duplicates
3. Use two pointers `l` and `r` to scan from `i+1` to end:
   - If sum > 0 → move `r` left to reduce sum
   - If sum < 0 → move `l` right to increase sum
   - If sum == 0 → add triplet to result
     - Move `l` and `r` while skipping duplicates

*******************************************
"""
