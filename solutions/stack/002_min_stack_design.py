"""
******** TIME & SPACE COMPLEXITY ********

Time:
- push, pop, top, getMin → O(1) each

Space:
- O(N) → for maintaining two stacks

*****************************************

*************** GENERAL IDEA ***************

Use two stacks:
1. `stack` holds all pushed values.
2. `minStack` keeps track of the **minimum** value at each level.

This enables constant-time min retrieval by always storing the current minimum at each push.

*******************************************

***************** LOGIC ********************

1. On `push(val)`:
   - Push `val` to `stack`.
   - Push `min(val, current_min)` to `minStack`.

2. On `pop()`:
   - Pop from both `stack` and `minStack`.

3. On `top()`:
   - Return the top of `stack`.

4. On `getMin()`:
   - Return the top of `minStack`.

*******************************************
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
