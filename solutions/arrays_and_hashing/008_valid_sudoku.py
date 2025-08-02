"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(1) → Board is always 9×9
Space: O(1) → Fixed number of sets

*****************************************

************** GENERAL IDEA **************

Use hash sets to track seen digits:
- For each cell, check if the digit is already present in:
   • The same row
   • The same column
   • The same 3×3 sub-box (based on row//3, col//3)

If a digit repeats in any of the above — board is invalid.

*****************************************

"""

import collections
from typing import List

class Solution:
    class Solution:
        def isValidSudoku(self, board: List[List[str]]) -> bool:
            row_map = collections.defaultdict(set)  # row_num: set of values
            col_map = collections.defaultdict(set)  # col_num: set of values
            box_map = collections.defaultdict(set)  # box_num: set of values

            for i in range(9):
                for j in range(9):
                    curr_val = board[i][j]
                    if curr_val == ".":
                        continue  # Skip empty cells
                    box_num = (i // 3) * 3 + (j // 3)
                    if curr_val in row_map[i] or curr_val in col_map[j] or curr_val in box_map[box_num]:
                        return False

                    row_map[i].add(curr_val)
                    col_map[j].add(curr_val)
                    box_map[box_num].add(curr_val)

            return True

    """
    - box_num is calculated based on row number and column number box_num = (i//3)*3 + (j//3)
    - i//3 will give if - top,middle,bottom row
    - j//3 will give if - top,middle,bottom col
    - *3 shifts to the correct row in the flattened 1D array of boxes
    """

"""
******************* LOGIC *******************

1. Initialize 3 hash maps with sets:
   - `rows_map[r]` for row-wise tracking
   - `col_map[c]` for column-wise tracking
   - `sq_map[(r//3, c//3)]` for 3x3 sub-boxes

2. Traverse board:
   - If cell is '.', skip
   - If digit exists in any of the 3 maps → return False
   - Otherwise, record digit into row/col/box sets

3. If no duplicate is found → return True

**********************************************
"""
