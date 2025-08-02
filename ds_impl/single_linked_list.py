"""
******** TIME & SPACE COMPLEXITY ********

- get(index):      O(N)
- insertHead(val): O(1)
- insertTail(val): O(1)
- remove(index):   O(N)
- getValues():     O(N)
- Space:           O(N) for storing N nodes

*****************************************
"""

class ListNode:
    def __init__(self, val: int, next_node=None):
        self.val = val
        self.next = next_node


class LinkedList:
    def __init__(self):
        node = ListNode(0)
        self.head, self.tail = node, node  # Dummy node initially

    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        while curr is not None:
            if index == i:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node

    def insertTail(self, val: int) -> None:
        new_node = ListNode(val)
        self.tail.next = new_node
        self.tail = self.tail.next

    def remove(self, index: int) -> bool:
        curr = self.head
        i = 0
        while curr and i < index:
            i += 1
            curr = curr.next
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> list[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


"""
******************** LOGIC ********************

1. `ListNode`: Basic node with value and next pointer.
2. `LinkedList.__init__`:
   - Use dummy head node for easier edge case handling.
   - `head` points to dummy, `tail` starts same.

3. `get(index)`:
   - Traverse list to desired index and return value.
   - Return -1 if index out of range.

4. `insertHead(val)`:
   - Insert new node after dummy head.
   - Update `tail` if list was empty.

5. `insertTail(val)`:
   - Add node after `tail`.
   - Update `tail`.

6. `remove(index)`:
   - Traverse to node before index.
   - Re-link to skip node at index.
   - Update `tail` if removing last node.

7. `getValues()`:
   - Traverse list and collect all node values in order.

***********************************************
"""
