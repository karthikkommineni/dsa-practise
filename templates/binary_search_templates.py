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
