"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(n log n)
    - T(n) = 2T(n/2) + O(n)
    - n splits * n comparisons during merge

Space: O(n)
    - Extra space for temporary arrays L and R during merge

*****************************************

********** GENERAL IDEA **********

Use the classic divide-and-conquer Merge Sort algorithm to sort a list of `Pair` objects by their `key`.

- Divide the input list into halves until size becomes 1.
- Recursively sort both halves.
- Merge the sorted halves while preserving stability.

It guarantees O(n log n) time even in worst-case scenarios and is **stable**, making it ideal for sorting custom objects.

*****************************************
"""


# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    # ✅ Merge Sort entry point
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs

        # The middle index of the array
        m = (s + e) // 2

        # Sort the left half
        self.mergeSortHelper(pairs, s, m)

        # Sort the right half
        self.mergeSortHelper(pairs, m + 1, e)

        # Merge sorted halves
        self.merge(pairs, s, m, e)

        return pairs

    # ✅ Merge in-place
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # Copy the sorted left & right halves to temp arrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i = 0  # index for L
        j = 0  # index for R
        k = s  # index for arr

        # Merge the two sorted halves into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # One of the halves may have elements remaining
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


"""
************** LOGIC ********************

1. Base case: If the subarray has ≤ 1 element, it's already sorted.
2. Recursively split the array at the midpoint.
3. Sort each half individually using merge sort.
4. Merge the two sorted halves:
    - Use two pointers to compare values from left and right temp arrays.
    - Fill the original array with smaller values in sorted order.
    - Copy remaining values (if any) from either half.

*****************************************
"""
