"""
******** TIME & SPACE COMPLEXITY ********

Insert / Get / Remove:
- Average: O(1)
- Worst-case (hash collisions): O(N) — when chaining is long

Space:
- O(C + N), where C = capacity, N = number of keys

*****************************************
"""

class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_function(self, key: int) -> int:
        return key % self.capacity

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        node = self.table[index]

        # If table entry is empty, insert node
        if not node:
            self.table[index] = Node(key, value)
            self.size += 1
        else:
            # If table entry has nodes, check for key update or append to the end
            prev = None
            while node:
                if node.key == key:
                    node.value = value
                    return
                prev, node = node, node.next
            prev.next = Node(key, value)
            self.size += 1

        # Check if resizing is needed
        if self.size / self.capacity >= 0.5:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.table[index]

        while node:
            if node.key == key:
                return node.value
            node = node.next

        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        n
