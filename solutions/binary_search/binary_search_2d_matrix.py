from typing import List

# ---------------------------------------------------------
# ✅ Approach 1: Brute Row-wise Binary Search
# ---------------------------------------------------------

"""
LOGIC:
step 1: For each row in the matrix, perform binary search
step 2: Works if each row is sorted individually
step 3: Time: O(m * log n), Space: O(1)
"""

class SolutionBrute:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for x in matrix:
            result = self.simple_binary_search(x, target)
            if result:
                return True
        return False

    def simple_binary_search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return False



# ---------------------------------------------------------
# ✅ Approach 2: Optimized 2-Level Binary Search
# ---------------------------------------------------------
"""
LOGIC:
- Step 1: Use binary search to find the valid row
- Step 2: Perform binary search within that row
- Requires fully sorted matrix (row-to-row sorted)
- Time: O(log m + log n), Space: O(1)
"""
class SolutionOptimized:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # first find the row which has value using modified bs
        firstRow, lastRow = 0, len(matrix) - 1

        while firstRow <= lastRow:
            midRow = (firstRow + lastRow) // 2
            # last element in midRow
            if target > matrix[midRow][-1]:
                firstRow = midRow + 1
            elif target < matrix[midRow][0]:
                lastRow = midRow - 1
            else:
                return self.simple_binary_search(matrix[midRow], target)
        return False  # if value is not found in midRow #Target not in range of any row

    def simple_binary_search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if target == nums[mid]:
                return True
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1

        return False






