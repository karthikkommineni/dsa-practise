import streamlit as st

def render_two_pointer_template():
    st.subheader("👣 Two Pointers - Template")

    code = """
def two_pointer(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        # Do some logic with arr[left] and arr[right]
        if some_condition:
            left += 1
        else:
            right -= 1
"""
    st.code(code, language='python')

    st.subheader("📘 Logic Steps")
    st.markdown(r"""
1. Start with `left` at 0 and `right` at end.
2. Loop while `left < right`
3. Adjust pointers based on condition.
""")

    st.subheader("🧠 Key Notes")
    st.markdown(r"""
- Efficient for sorted arrays, palindromes, etc.
- Avoids nested loops (O(n²) → O(n))
- Classic problems: Two Sum II, Container with Most Water
- Time: `O(n)` | Space: `O(1)`
""")
