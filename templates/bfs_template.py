import streamlit as st

def render_bfs_template():
    st.subheader("🧮 BFS Templates")

    # Basic BFS
    st.markdown("### ✅ Standard BFS (Level Order)")
    bfs_code = """
from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node in visited:
            continue

        visited.add(node)
        for neighbor in node.neighbors:
            queue.append(neighbor)
"""
    st.code(bfs_code, language="python")

    # Layered BFS
    st.markdown("### 🧭 Layered BFS (With Levels)")
    layered_bfs_code = """
from collections import deque

def bfs_levels(start):
    visited = set([start])
    queue = deque([(start, 0)])

    while queue:
        node, level = queue.popleft()
        print(f"Node: {node.val}, Level: {level}")

        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, level + 1))
"""
    st.code(layered_bfs_code, language="python")

    # Notes
    st.subheader("📘 Logic & Notes")
    st.markdown(r"""
- **Standard BFS**: Uses queue, visits neighbors level-by-level.
- **Layered BFS**: Adds `level` tracking — useful for shortest path, graph depth, etc.
- Time: `O(V + E)` | Space: `O(V)`
""")
