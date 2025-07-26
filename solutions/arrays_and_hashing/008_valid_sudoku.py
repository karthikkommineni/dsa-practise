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
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows_map = collections.defaultdict(set)
        col_map = collections.defaultdict(set)
        sq_map = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows_map[r] or
                    board[r][c] in col_map[c] or
                    board[r][c] in sq_map[(r // 3, c // 3)]):
                    return False

                rows_map[r].add(board[r][c])
                col_map[c].add(board[r][c])
                sq_map[(r // 3, c // 3)].add(board[r][c])

        return True

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
