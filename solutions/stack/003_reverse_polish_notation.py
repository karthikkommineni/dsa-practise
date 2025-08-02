"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → One pass through the tokens
Space: O(N) → Stack size grows with number of operands

*****************************************

*************** GENERAL IDEA ***************

Use a stack to evaluate the expression:
- When you see a number, push it onto the stack.
- When you see an operator, pop the top two numbers, apply the operator, and push the result back.

*******************************************

***************** LOGIC ********************

1. Traverse each token:
   - If it is a number, push to stack.
   - If it is an operator:
     a. Pop top two elements (order matters for '-' and '/')
     b. Apply the operator.
     c. Push result back.

2. Special handling:
   - For division `/`, cast result to `int(float(x) / y)` to truncate toward zero (Python style).

3. Return the final value in the stack (only one element should remain).

*******************************************
"""

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)  # Order matters

            elif c == "*":
                stack.append(stack.pop() * stack.pop())

            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))  # Truncate toward 0

            else:
                stack.append(int(c))  # Convert number string to int

        return stack[0]
