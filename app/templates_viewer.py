import streamlit as st
from templates.binary_search_templates import render_binary_search_template
from templates.dfs_template import render_dfs_template
from templates.bfs_template import render_bfs_template
from templates.queue_template import render_queue_template
from templates.sorting_template import render_sorting_template
from templates.two_pointer_template import render_two_pointer_template
from templates.sliding_window_template import render_sliding_window_template

from templates.stack_template import render_stack_template
from templates.heap_template import render_heap_template

TEMPLATE_RENDERERS = {
    "Two Pointer": render_two_pointer_template,
    "Sliding Window": render_sliding_window_template,
    "Stack": render_stack_template,
    "Heap": render_heap_template,
    "Sorting": render_sorting_template,
    "Binary Search": render_binary_search_template,
    "DFS": render_dfs_template,
    "BFS": render_bfs_template,
    "Queue": render_queue_template,
}


def show():
    st.title("📚 Templates Viewer")

    selected_template = st.selectbox("Select a Template", list(TEMPLATE_RENDERERS.keys()))

    TEMPLATE_RENDERERS[selected_template]()  # Call the selected template renderer
