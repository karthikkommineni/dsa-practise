"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → Each index is pushed and popped at most once
Space: O(N) → For the stack and output array

*****************************************

*************** GENERAL IDEA ***************

Use a **monotonic decreasing stack** to keep track of indices of temperatures
that haven’t found a warmer day yet.

*******************************************

***************** LOGIC ********************

1. Initialize a stack to store **indices** of temperatures.
2. Traverse each temperature `t` at index `i`:
   - While the stack is not empty and `t` is **greater than** temperature at stack's top index:
     - Pop the index from the stack.
     - Compute the difference in days: `i - popped_index`.
     - Store that in `output[popped_index]`.
3. Push current index `i` onto the stack.
4. Return the output array, which contains days to wait for a warmer temperature.

*******************************************
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # stores indices of unresolved temps
        output = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                idx = stack.pop()
                output[idx] = i - idx
            stack.append(i)

        return output
