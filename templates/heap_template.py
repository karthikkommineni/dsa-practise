import streamlit as st

def render_heap_template():
    st.subheader("🔺 Heap Templates (Min & Max)")

    # Min Heap
    st.markdown("### ✅ Min Heap (Default in Python)")
    min_heap_code = """
import heapq

nums = [5, 2, 8, 3]
heapq.heapify(nums)     # In-place convert to min-heap

heapq.heappush(nums, 1) # Push element
min_val = heapq.heappop(nums)  # Pop smallest

print(min_val)  # 1
"""
    st.code(min_heap_code, language="python")

    # Max Heap
    st.markdown("### 📦 Max Heap (Using Negative Values)")
    max_heap_code = """
import heapq

nums = [5, 2, 8, 3]
max_heap = [-n for n in nums]
heapq.heapify(max_heap)

heapq.heappush(max_heap, -10)
max_val = -heapq.heappop(max_heap)

print(max_val)  # 10
"""
    st.code(max_heap_code, language="python")

    # Kth Largest Element
    st.markdown("### 🧭 Kth Largest Element (Min Heap of size K)")
    kth_largest_code = """
import heapq

def kth_largest(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)

    return heap[0]
"""
    st.code(kth_largest_code, language="python")

    # Notes
    st.subheader("📘 Logic & Notes")
    st.markdown(r"""
- **Min-heap** is default in Python `heapq`.
- **Max-heap** is simulated using negative values.
- Great for top-K problems, streaming median, scheduling.
- Time:
  - Heapify: `O(n)`
  - Push/Pop: `O(log k)`
  - Kth largest: `O(n log k)`
""")
