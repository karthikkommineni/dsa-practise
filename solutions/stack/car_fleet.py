"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N log N) → Due to sorting cars by position
Space: O(N)       → For storing times in the stack

*****************************************

*************** GENERAL IDEA ***************

Simulate how each car takes time to reach the target and track **fleets** based on their arrival time.

- Cars that **can't overtake** will form a fleet with slower cars ahead of them.
- Sort cars from farthest to closest to the target and simulate their progress.

*******************************************

***************** LOGIC ********************

1. Create `(position, speed)` pairs for each car.
2. Sort the list in descending order by position — farthest from target comes first.
3. For each car:
   - Calculate its **time** to reach the target.
   - Push it to the stack.
   - If the car behind catches up (equal or faster time), it's **not** a new fleet → pop it.
4. Return the number of fleets = number of elements in the stack.

*******************************************
"""

from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]  # (position, speed)
        pair.sort(reverse=True)  # sort from closest to farthest from target

        stack = []  # store time taken by each fleet to reach target

        for p, s in pair:
            time = (target - p) / s
            stack.append(time)
            # merge fleet if current car catches up with the one ahead
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()  # same fleet, discard current
        return len(stack)
