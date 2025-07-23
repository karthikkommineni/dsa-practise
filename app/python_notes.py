import streamlit as st

def show_python_notes():
    st.title("🐍 Python Notes")

    with st.expander("🔤 Underscore Conventions"):
        st.code("""
_var         # Single leading underscore: internal use, not imported by *
__var        # Double leading: name mangling → _ClassName__var
__var__      # Dunder methods: special Python methods like __init__, __len__
""", language="python")

    with st.expander("✅ Truthy / Falsy Values"):
        st.code("""
if my_list:        # True if list is not empty
if not my_dict:    # True if dict is empty
while data:        # Runs while data is not falsy

# Falsy values: None, [], {}, '', 0, False
""", language="python")

    with st.expander("🧠 Ternary Operation"):
        st.code("""
# Syntax: value_if_true if condition else value_if_false
result = "even" if x % 2 == 0 else "odd"
""", language="python")

    with st.expander("🔁 Declaring Infinity"):
        st.code("""
min_val = float('inf')
max_val = float('-inf')
""", language="python")

    with st.expander("🧩 String Patterns & Combinatorics"):
        st.code("""
# Permutations (order matters, no repeat)
from itertools import permutations
for p in permutations("ABC", 2):
    print(''.join(p))  # AB, AC, BA, BC, CA, CB

# Combinations (order doesn't matter, no repeat)
from itertools import combinations
for c in combinations("ABC", 2):
    print(''.join(c))  # AB, AC, BC

# Product (order matters, with repeat)
from itertools import product
for p in product("AB", repeat=2):
    print(''.join(p))  # AA, AB, BA, BB

# Substrings (all continuous substrings)
def all_substrings(s):
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            print(s[i:j])

all_substrings("ABC")  # A, AB, ABC, B, BC, C
""", language="python")

    with st.expander("📊 Python Data Structures: Complete Comparison"):
        st.markdown("""
| Data Structure  | Mutable | Ordered | Duplicates | Indexable | Add                        | Remove                        | Update                      |
|-----------------|---------|---------|------------|-----------|-----------------------------|-------------------------------|------------------------------|
| `list`          | ✅      | ✅      | ✅         | ✅        | `append()`, `insert()`      | `pop()`, `remove()`           | `lst[i] = x`                |
| `set`           | ✅      | ❌      | ❌         | ❌        | `add(x)`                    | `remove(x)`, `discard(x)`     | ❌                          |
| `dict`          | ✅      | ✅\*    | ✅ (keys unique) | ✅ by key | `d['k'] = v`               | `del d['k']`, `pop()`         | `d['k'] = new_val`         |
| `tuple`         | ❌      | ✅      | ✅         | ✅        | ❌                          | ❌                             | ❌                          |
| `stack (list)`  | ✅      | ✅      | ✅         | ✅        | `append(x)`                 | `pop()`                        | `stack[-1] = x` (not typical)|
| `queue (deque)` | ✅      | ✅      | ✅         | ✅ (ends) | `append()`, `appendleft()`  | `pop()`, `popleft()`          | ❌                          |
| `queue.Queue`   | ✅      | ✅      | ✅         | ❌        | `put(x)`                    | `get()`                        | ❌                          |
| `deque`         | ✅      | ✅      | ✅         | ✅ (ends) | `append()`, `appendleft()`  | `pop()`, `popleft()`          | ❌                          |
""", unsafe_allow_html=True)

        st.caption("*Note: `dict` maintains insertion order from Python 3.7+")

    with st.expander("🎯 Built-in Functions & Shortcuts"):
        st.code("""
# Enumerate
for i, val in enumerate(my_list):
    print(i, val)

# List comprehension
[x * 2 for x in range(5)]

# Map / Filter
map(str, [1, 2, 3])
filter(lambda x: x % 2 == 0, nums)
""", language="python")
