import streamlit as st

def render_stack_template():
    st.subheader("📦 Stack Templates")

    # Basic usage
    st.markdown("### ✅ Basic Stack Usage")
    basic_stack = """
stack = []

# Push
stack.append(5)

# Peek
top = stack[-1]

# Pop
val = stack.pop()
"""
    st.code(basic_stack, language="python")

    # Valid Parentheses
    st.markdown("### 🧩 Valid Parentheses Check")
    valid_parens = """
def is_valid(s):
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False

    return not stack
"""
    st.code(valid_parens, language="python")

    # Monotonic Stack
    st.markdown("### 📉 Monotonic Decreasing Stack (Next Greater Element)")
    mono_stack = """
def next_greater(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result
"""
    st.code(mono_stack, language="python")

    # Notes
    st.subheader("📘 Logic & Notes")
    st.markdown(r"""
- **Stack** follows LIFO: last-in, first-out.
- Use cases: undo history, DFS, string parsing, balancing symbols.
- **Monotonic stack** helps solve "next greater/smaller" problems in linear time.
- Time: `O(n)` in monotonic use (each element pushed/popped once)
""")
