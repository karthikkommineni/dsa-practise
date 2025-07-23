import streamlit as st

def render_queue_template():
    st.subheader("🟦 Queue & Deque Templates")

    st.markdown("### ✅ Queue (FIFO) using `deque`")
    st.code("""
from collections import deque

queue = deque()
queue.append('a')     # enqueue
item = queue.popleft()  # dequeue
front = queue[0]      # peek front
""", language="python")

    st.markdown("### ✅ Thread-safe Queue using `queue.Queue`")
    st.code("""
from queue import Queue

q = Queue()
q.put('a')         # enqueue
item = q.get()     # dequeue
""", language="python")

    st.markdown("### 🔁 Deque (Double-Ended Queue)")
    st.code("""
from collections import deque

dq = deque()

dq.append(x)        # add to right
dq.appendleft(x)    # add to left
dq.pop()            # remove from right
dq.popleft()        # remove from left

front = dq[0]
back = dq[-1]
""", language="python")

    st.subheader("📘 Notes")
    st.markdown(r"""
- **Queue** = First In First Out (FIFO)
- **Deque** = Double-ended queue (supports both ends)
- Use `deque` for:
  - Sliding window problems
  - Palindrome check
  - Two-pointer pattern
- Use `queue.Queue` when thread-safety is needed
- Time Complexity:
  - `append`, `popleft`, `appendleft`, `pop` → O(1)
""")
