"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → N = length of input string
Space: O(N) → For stack in worst case

*****************************************

*************** GENERAL IDEA ***************

Use a stack to track opening brackets.
When a closing bracket appears, check if it matches the top of the stack.
If mismatch or stack is empty, return False.
At the end, stack should be empty for a valid string.

*******************************************

***************** LOGIC ********************

1. Traverse the string character by character.
2. If it's a closing bracket:
   - Check if stack is empty or top doesn't match → return False.
   - Else, pop from the stack.
3. If it's an opening bracket:
   - Push to the stack.
4. At the end, if stack is empty → all brackets matched → return True.

*******************************************
"""

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or s is None:
            return False

        b_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for c in s:
            if c in b_map:
                if not stack or b_map[c] != stack.pop():
                    return False
            else:
                # add to stack
                stack.append(c)

        return not stack
