"""
******** TIME & SPACE COMPLEXITY ********

Push / Pop / Top:
- Time: O(log N) for push/pop, O(1) for top
- Space: O(N) where N = number of elements in heap

Heapify:
- Time: O(N) → Efficient bottom-up heap construction
- Space: O(N)

*****************************************
"""


# MinHeap Class Implementation
class MinHeap:
    def __init__(self):
        self.heap = [0]  # Initialize heap with a dummy value at index 0

    def push(self, val: int) -> None:
        """Pushes a value onto the heap."""
        self.heap.append(val)
        self._bubble_up(len(self.heap) - 1)

    def pop(self) -> int:
        """Pops the smallest value off the heap."""
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        # Move the las
