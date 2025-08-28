import streamlit as st


def render_sliding_window_template():
    st.subheader("🪟 Sliding Window - Template")

    code = """
def sliding_window_fixed(nums, k):
    # left pointer marks the start of the window
    left = 0
    # running sum of the current window
    window_sum = 0
    # to store results of each window
    result = []

    for right in range(len(nums)):
        # expand window
        window_sum += nums[right]

        # shrink window once it reaches size k
        if right - left + 1 == k:
            result.append(window_sum)  # process current window
            window_sum -= nums[left]   # remove left element
            left += 1  # move window forward

    return result


def max_sum_subarray(nums, k):
    # initialize left pointer, running sum, and max
    left, window_sum, max_sum = 0, 0, float('-inf')
    for right in range(len(nums)):
        window_sum += nums[right]
        if right - left + 1 == k:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[left]
            left += 1
    return max_sum


def sliding_window_variable(s):
    \"\"\"
    Returns the length of the longest substring without repeating characters.
    Example:
      s = "abcabcbb" → 3 ("abc")
    \"\"\"
    # left pointer tracks start of window
    left = 0
    # dictionary to count characters inside window
    seen = {}
    # track max length of valid substring
    max_len = 0

    for right in range(len(s)):
        # expand window
        char = s[right]
        seen[char] = seen.get(char, 0) + 1

        # shrink while condition is violated
        while seen[char] > 1:  # duplicate found
            seen[s[left]] -= 1
            left += 1

        # update answer
        max_len = max(max_len, right - left + 1)

    return max_len
"""
    st.code(code, language='python')

    st.subheader("📘 Logic Steps")
    st.markdown(r"""
### Fixed-Size Window
1. **Expand window** → Add new element to the running sum.
2. **Check size** → When window size = `k`, record result.
3. **Process result** → Store sum, max, or other aggregate.
4. **Shrink window** → Remove leftmost element to slide forward.

👉 Solves problems like:
- Find all subarray sums of size `k`
- Find maximum/minimum sum of subarray of size `k`
- Moving averages
---
### Variable-Size Window
1. Expand window by moving `right` pointer and include new element.
2. Check validity condition (e.g., unique characters, sum ≥ target).
3. If condition breaks → shrink window from `left` until valid again.
4. Update result (`max_len`, `min_len`, etc.) whenever valid.

👉 Solves problems like:
- Longest substring without repeating characters
- Smallest subarray with sum ≥ target
- Longest substring with at most K distinct characters
""")

    st.subheader("🧠 Key Notes")
    st.markdown(r"""
- **Fixed-size window**: For problems with exact window length `k`.  
- **Variable-size window**: For dynamic window problems where validity depends on conditions.  
- Sliding window reduces `O(n*k)` brute force → `O(n)` efficient solution.  
- Time: `O(n)` | Space: `O(1)` for fixed window, `O(k)`/`O(charset)` for variable window.  
""")
