"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N log K) → N = total numbers, K = top frequent elements
Space: O(N)       → For frequency map and heap

*****************************************

************** GENERAL IDEA **************

To find the top K frequent elements:
- First, count frequency of each number using a dictionary.
- Then use a min-heap of size K to track the top K frequent numbers.
- Whenever heap size exceeds K, pop the smallest frequency.
- Extract the remaining elements from the heap as result.

Why min-heap?
- Maintains only K largest frequencies efficiently in O(log K) per insert.

*****************************************
"""

import heapq
from typing import List, Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        min_heap = []  # Min-heap to keep top k frequent elements
        res = []
        frq_map = Counter(nums)  # Frequency map in O(N)

        for key, freq in frq_map.items():
            heapq.heappush(min_heap, (freq, key))     # O(logK) operation
            if len(min_heap) > k:
                heapq.heappop(min_heap)               # Maintain size K → O(logK)

        while min_heap:
            res.append(heapq.heappop(min_heap)[1])    # Extract element → O(logK)

        return res[::-1]  # Optional: reverse if you want highest freq first
                                        #start:stop:step -> -1 is backward step

    def topKFrequent_heapify(self, nums: List[int], k: int) -> List[int]:
        freqMap = Counter(nums)  # count frequencies: O(n)

        # Use negative frequency to simulate max-heap
        maxHeap = [(-freq, num) for num, freq in freqMap.items()]  # O(n)
        heapq.heapify(maxHeap)  # convert list to heap: O(n)

        return [heapq.heappop(maxHeap)[1] for _ in range(k)]  # extract k elements: O(k log n) - give only k elements not all


"""
************** LOGIC ********************

1. Count how many times each number appears in the list.
2. Use a min-heap to keep only the K most frequent numbers:
   - Always keep the heap size ≤ K by removing the least frequent ones.
3. At the end, the heap contains the top K frequent numbers.
4. Remove all from heap and return them as result.
5. Heapify - o(n), heappush - o(log n), heappop - o(log n)
6. heapify converts all elements in list to heap in O(n) time.

*****************************************

Alternate so

✅ Python heapq Time Complexities

heapq.heapify(list)
- Converts a list to a valid heap
- Time: O(n)

heapq.heappush(heap, x)
- Inserts an element into the heap
- Time: O(log n)

heapq.heappop(heap)
- Removes and returns the smallest element
- Time: O(log n)

heapq.heappushpop(heap, x)
- Pushes x, then pops and returns the smallest
- Time: O(log n)

heapq.nlargest(k, iterable)
- Returns k largest elements
- Time: O(n log k)

heapq.nsmallest(k, iterable)
- Returns k smallest elements
- Time: O(n log k)
"""
