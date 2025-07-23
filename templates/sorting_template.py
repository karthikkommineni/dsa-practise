import streamlit as st

def render_sorting_template():
    st.subheader("🔀 Sorting Algorithms")

    st.markdown("### ✅ Merge Sort")
    st.code("""
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
""", language="python")

    st.markdown("### ⚡ Quick Sort (in-place)")
    st.code("""
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1
""", language="python")

    st.markdown("### 🔺 Heap Sort")
    st.code("""
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
""", language="python")

    st.markdown("### 🧠 Built-in Sort")
    st.code("""
arr = [4, 1, 9, 2]
arr.sort()                      # in-place
sorted_arr = sorted(arr)        # returns new sorted list
""", language="python")

    st.subheader("📘 Notes")
    st.markdown(r"""
- **Merge Sort**: Stable, safe for large inputs. Time: `O(n log n)`, Space: `O(n)`
- **Quick Sort**: Fast average case, but worst-case `O(n²)`. In-place.
- **Heap Sort**: Consistent `O(n log n)`, but not stable.
- **Built-in Timsort**: Hybrid of merge/insertion sort → optimal in practice
""")
