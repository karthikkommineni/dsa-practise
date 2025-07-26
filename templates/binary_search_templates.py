import streamlit as st

def render_binary_search_template():
    st.subheader("🚀 Binary Search (Iterative) - Code Template")

    binary_search_code = """
def binary_search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        mid_val = nums[mid]

        if mid_val == target:
            return True
        elif mid_val > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
"""
    st.code(binary_search_code, language='python')

    st.subheader("📘 Logic Steps")
    st.markdown(r"""
1. Initialize `left = 0` and `right = len(nums) - 1`
2. While `left <= right`:
   - Compute `mid = left + (right - left) // 2`
   - ✅ If `nums[mid] == target`: return `True`
   - ❌ If `nums[mid] > target`: search left
   - ❌ If `nums[mid] < target`: search right
3. Loop exits → return `False`
""")

    st.subheader("🧠 Key Notes")
    st.markdown(r"""
- **Two-pointer approach**
- `left <= right` ensures middle is checked
- `left + (right - left) // 2` avoids overflow
- Time: `O(log n)` | Space: `O(1)`
""")

    st.subheader("💡 Example Problems (Iterative)")

    st.markdown(r"""
- [Binary Search](https://neetcode.io/problems/binary-search?list=neetcode150)
- [2D-search matrix](https://neetcode.io/problems/search-2d-matrix?list=neetcode150)
""")

    st.subheader("🔍 Binary Search on a Range with Custom Condition")

    range_search_code = """
# Custom binary search on range [low, high]
def binarySearch(low, high):
    while low <= high:
        mid = (low + high) // 2

        if isCorrect(mid) > 0:
            high = mid - 1
        elif isCorrect(mid) < 0:
            low = mid + 1
        else:
            return mid
    return -1

# Custom check function (e.g., target = 10)
def isCorrect(n):
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0
"""
    st.code(range_search_code, language='python')

    st.markdown(r"""
- Useful when working with a **range** of values, not a list
- `isCorrect()` simulates external logic (e.g., API response)
- Replace with your logic (`guess()`, `canComplete()`, etc.)
- Time: `O(log n)` | Space: `O(1)`
""")

    st.subheader("💡 Example Problems (Range-Based)")

    st.markdown(r"""
- [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/)
- [69. Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)
- [1283. Find the Smallest Divisor Given a Threshold](https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/)
""")

    st.subheader("🌀 Binary Search (Recursive)")

    recursive_search_code = """
def binary_search_recursive(nums, target, left, right):
    if left > right:
        return False

    mid = left + (right - left) // 2

    if nums[mid] == target:
        return True
    elif nums[mid] > target:
        return binary_search_recursive(nums, target, left, mid - 1)
    else:
        return binary_search_recursive(nums, target, mid + 1, right)

# Example usage:
# binary_search_recursive(nums, target, 0, len(nums) - 1)
"""
    st.code(recursive_search_code, language='python')

    st.markdown(r"""
- Recursive variant of binary search
- Reduces problem size in each call
- Time: `O(log n)` | Space: `O(log n)` due to call stack
""")

    st.subheader("💡 Example Problems (Recursive)")

    st.markdown(r"""
- [704. Binary Search (can be done recursively)](https://leetcode.com/problems/binary-search/)
- [34. Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [240. Search a 2D Matrix II](https://leetcode.com/problems/search-a-2d-matrix-ii/)
""")
