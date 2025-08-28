"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N^2) → Outer loop + two-pointer scan
Space: O(1)   → Ignoring output list

*****************************************
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # target =0, i,j,k not equal, no duplicates in solution
        res = []
        target = 0
        nums.sort()  # brutefore -o(n3) - we want in n2 - sorted -o(nlogn)

        for i, n in enumerate(nums):
            if n > 0:
                break
            # i>0 to avoid index out of range
            if i and (nums[i] == nums[i - 1]):
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                s = nums[j] + nums[k] + nums[i]
                if s == 0:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1  # move
                    k -= 1
                    # skip duplicates on both sides
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif s > 0:
                    k -= 1
                else:
                    j += 1

        return res


"""
*************** GENERAL IDEA ***************
- at first place i - we calculate all possible two sums and check
- next to second place - all possibe two sums and check
- continue till loop ends
    - in two sum - we skip duplicates
- 
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
