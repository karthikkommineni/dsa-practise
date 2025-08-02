"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(2^2n) → Each position has 2 choices, total 2n positions
Space: O(2n)   → Stack depth and result string size

*****************************************

*************** GENERAL IDEA ***************

Use **backtracking** to generate valid parentheses:
- We build the string step-by-step using decisions.
- Only add '(' if we still have open slots.
- Only add ')' if it doesn't exceed open count.

*******************************************

***************** LOGIC ********************

1. Use a recursive function `addParenthesisIfValid(opc, cpc)`:
   - `opc`: count of open parentheses added
   - `cpc`: count of closed parentheses added

2. Base case:
   - If `opc == cpc == n`, we have a valid string.
   - Join characters from stack and store in `res`.

3. Recursive steps:
   - If `opc < n`: we can add `'('`, recurse, then backtrack.
   - If `cpc < opc`: we can add `')'`, recurse, then backtrack.

4. Use a list `stack` to build characters incrementally (faster than string concat).

*******************************************
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def addParenthesisIfValid(opc, cpc):
            if opc == cpc == n:
                res.append("".join(stack))  # convert list to string
                return

            if opc < n:
                stack.append("(")
                addParenthesisIfValid(opc + 1, cpc)
                stack.pop()  # backtrack

            if cpc < opc:
                stack.append(")")
                addParenthesisIfValid(opc, cpc + 1)
                stack.pop()  # backtrack

        addParenthesisIfValid(0, 0)
        return res

       #execute
        # addParenthesisIfValid(0,0)
        # addParenthesisIfValid(1,0)
        # addParenthesisIfValid(2,0)
        # addParenthesisIfValid(3,0)
        # addParenthesisIfValid(3,1)X
        # addParenthesisIfValid(3,2)x
        # addParenthesisIfValid(3,3) x