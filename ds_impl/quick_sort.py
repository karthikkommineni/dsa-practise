"""
******** TIME & SPACE COMPLEXITY ********

Time:
- Best/Average: O(n log n)
- Worst: O(n^2) if pivot is poorly chosen (but rare with randomized pivot)

Space:
- O(log n) average (for recursion stack)
- O(n) worst case (if pivot leads to unbalanced partitions)

*****************************************

********** GENERAL IDEA **********

Quick Sort is a **divide-and-conquer** algorithm that:

1. Picks a pivot element (here: last element)
2. Partitions the array into two:
    - Left: elements < pivot
    - Right: elements ≥ pivot
3. Recursively sorts the left and right parts

⚠️ It's not stable and has poor worst-case guarantees without randomized pivot,
but is **very fast in practice** due to in-place sorting and good cache usage.

*****************************************
"""

# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    # ✅ Quick Sort entry point
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return

        pivot = arr[e]  # pick pivot as last element
        left = s        # partition index

        # Move smaller elements to left of pivot
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        # Place pivot in its correct position
        arr[left], arr[e] = arr[e], arr[left]

        # Recursively sort left and right subarrays
        self.quickSortHelper(arr, s, left - 1)
        self.quickSortHelper(arr, left + 1, e)

"""
************** LOGIC ********************

1. Base case: If subarray has ≤ 1 element, it's sorted
2. Choose a pivot (last element in this case)
3. Partition:
    - All elements < pivot are moved to the left side
    - Track index `left` for where next smaller item should go
4. Swap pivot to its correct sorted index
5. Recursively sort left and right of pivot

*****************************************
"""
