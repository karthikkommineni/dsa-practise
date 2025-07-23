import streamlit as st

def render_dfs_template():
    st.subheader("🌲 DFS Templates")

    # Recursive DFS
    st.markdown("### ✅ Recursive DFS")
    recursive_dfs_code = """
def dfs_recursive(node, visited):
    if not node or node in visited:
        return

    visited.add(node)
    for neighbor in node.neighbors:
        dfs_recursive(neighbor, visited)
"""
    st.code(recursive_dfs_code, language="python")

    # Iterative DFS
    st.markdown("### 🌀 Iterative DFS using Stack")
    iterative_dfs_code = """
def dfs_iterative(start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)
        for neighbor in reversed(node.neighbors):  # Reverse to match recursive order
            stack.append(neighbor)
"""
    st.code(iterative_dfs_code, language="python")

    # Notes
    st.subheader("📘 Logic & Notes")
    st.markdown(r"""
- **Recursive DFS**: Simple and elegant for small graphs.
- **Iterative DFS**: Prevents stack overflow on deep graphs. Uses explicit `stack`.
- `visited` set is key to avoid infinite loops in cyclic graphs.
- Time: `O(V + E)` | Space: `O(H)` for recursive, `O(V)` for iterative.
""")
