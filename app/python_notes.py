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
my_list = ['apple', 'banana', 'cherry']
for i, val in enumerate(my_list):
    print(i, val)
# Output:
# 0 apple
# 1 banana
# 2 cherry

# List comprehension
doubled = [x * 2 for x in range(5)]
print(doubled)
# Output: [0, 2, 4, 6, 8]

# Map
mapped = list(map(str, [1, 2, 3]))
print(mapped)
# Output: ['1', '2', '3']

# Filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
# Output: [2, 4, 6]

# Zip
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for a, b in zip(list1, list2):
    print(a, b)
# Output:
# 1 a
# 2 b
# 3 c
-> Note: `zip` stops at the shortest input
""", language="python")
    with st.expander("🧠 Misc Interview Concepts"):
        st.markdown("""
### ✅ Topic 1: Why `sorted()` Needs `.join()`
- `sorted(s)` returns a list → not usable as dict key.
- Lists are mutable → unhashable.
- `''.join(sorted(s))` creates an immutable string.
- Strings are hashable → valid for dict keys.
- Common use: grouping anagrams.

### ✅ Topic 2: Why List Can’t Be a Key — Use `tuple`
- Lists are mutable and unhashable.
- Tuples are immutable and hashable.
- Convert `[0]*26` to `tuple(...)` before using as dict key.
- Used for grouping anagrams by character frequency.
- Avoids runtime `TypeError`.

### ✅ Topic 3: `defaultdict` vs `dict`
- `dict` needs key check or initialization.
- `defaultdict` provides default value automatically.
- Prevents `KeyError` when accessing missing keys.
- Ideal for grouping or counting.
- Syntax: `defaultdict(list)`, `defaultdict(int)`, etc.

### ✅ Topic 4: Shallow vs Deep Copy
- Shallow copy shares nested objects.
- Deep copy duplicates all levels.
- `.copy()` vs `copy.deepcopy()`.
- Shallow reflects changes in inner data.
- Deep ensures full isolation.


### ✅ Topic 5: What Are View Objects?
- `.keys()`, `.values()`, `.items()` return **view objects**, not lists.
- View objects reflect **live updates** in the dictionary.
- They are **memory-efficient** because they don’t copy data.
- You can iterate over them, but not index directly.
- Wrap with `list()` if you need indexing or materialized copy.
- for key,val in dict.items:   -> we can access key and value directly

```python
# Example:
d = {'a': 1, 'b': 2}
keys = d.keys()           # dict_keys(['a', 'b'])
d['c'] = 3
print(keys)               # dict_keys(['a', 'b', 'c'])  ← auto-updated
print(list(d.items()))    # [('a', 1), ('b', 2), ('c', 3)]

d = {'a': 1, 'b': 2}
d.keys()        # → dict_keys(['a', 'b'])
d.values()      # → dict_values([1, 2])
d.items()       # → dict_items([('a', 1), ('b', 2)])


d = {'a': 1, 'b': 2}

for key, val in d.items():
    print(key, val)
# Output:
a1
b2
```

### ✅ Topic 6: `dict.get()` method
- Syntax: `dict.get(key, default)`
- Returns value if key exists, else returns default (e.g. 0).
- Helps avoid `KeyError` without if-checks.
- Common in frequency/count problems.
- Alternative to `defaultdict` when default is fixed.

### ✅ Topic 7: `counter(num)` method
- gets frequency of each element in a list.
-From collections module.
-Counts frequencies of elements.
-Returns a dict-like object.
-Supports most_common(), arithmetic, etc.
- Cleaner alternative to manual counting.

- example: 
nums = [1, 2, 2, 3, 3, 3]
count = Counter(nums)
print(count)
# Output: Counter({3: 3, 2: 2, 1: 1})

Topic 7:Notes on `range(start, stop, step)`

1️⃣ Default usage:
   - `range(n)` ⇒ starts at 0, ends at n-1
   - Example: `range(5)` → [0, 1, 2, 3, 4]

2️⃣ Positive step:
   - `range(2, 7, 1)` → [2, 3, 4, 5, 6]
   - Iterates forward by +1 (or any +ve value)

3️⃣ Negative step (reverse loop):
   - `range(5, -1, -1)` → [5, 4, 3, 2, 1, 0]
   - Stops **before** hitting -1

4️⃣ Mixing positive with negative step gives empty result:
   - `range(5, 10, -1)` → []  ❌ (won’t run because direction mismatch)

5️⃣ Common patterns:
   - Reverse iteration: `range(n-1, -1, -1)`
   - Slicing last elements: use negative indices like `range(-1, -len(arr)-1, -1)`

Topic 8: Python String Slicing: `s[start:stop:step]`

1️⃣ Basic Substring Access:
   - `s[i:j]` gives characters from index `i` up to (but not including) `j`.
   - Example: `'abcdef'[1:4]` → `'bcd'`

2️⃣ Step Parameter (`::step`):
   - Skips characters by step size.
   - Example: `'abcdef'[::2]` → `'ace'` (every 2nd character)
   - Reverse a string: `'abcdef'[::-1]` → `'fedcba'`

3️⃣ Common Mistake:
   - `s[i::j]` is NOT the same as `s[i:j]`
   - `s[i::j]` means → start at `i`, skip every `j` characters.
   - Example: `'abcdef'[1::4]` → `'bf'`, not `'bcd'`

4️⃣ Full Format:
   - `s[start:stop:step]`
   - Any of the three parts can be omitted.
   - Defaults: `start=0`, `stop=len(s)`, `step=1`

5️⃣ More Examples:
   - `s = "abcdef"`
   - `s[2:5:2]` → `'ce'`
   - `s[:3]` → `'abc'`
   - `s[3:]` → `'def'`
   - `s[-3:]` → `'def'` (last 3 characters)

✅ Use `s[i:j]` for substrings  
✅ Use `s[::-1]` for reverse  
❌ Avoid `s[i::j]` when trying to extract up to index `j`

        """)