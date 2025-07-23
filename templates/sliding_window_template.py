import streamlit as st

def render_sliding_window_template():
    st.subheader("🪟 Sliding Window - Template")

    code = """
def sliding_window(nums, k):
    window_sum = sum(nums[:k])
    max_sum = window_sum

    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum
"""
    st.code(code, language='python')

    st.subheader("📘 Logic Steps")
    st.markdown(r"""
1. Compute sum of first window of size `k`.
2. Slide window: subtract leftmost, add rightmost.
3. Track max sum or result.
""")

    st.subheader("🧠 Key Notes")
    st.markdown(r"""
- Used for problems involving subarrays, substrings, etc.
- Works for fixed-size and variable-size window problems.
- Efficient alternative to nested loops.
- Time: `O(n)` | Space: `O(1)`
""")
