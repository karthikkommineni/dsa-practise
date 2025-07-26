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
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for num in nums:
            freqMap[num] = freqMap.get(num, 0) + 1  # count how many times each number appears

        minHeap = []
        for num, freq in freqMap.items():
            heapq.heappush(minHeap, (freq, num))     # add (frequency, number) to min heap
            if len(minHeap) > k:
                heapq.heappop(minHeap)               # remove smallest frequency to keep top K only

        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])    # extract numbers from the heap

        return res

"""
************** LOGIC ********************

1. Count how many times each number appears in the list.
2. Use a min-heap to keep only the K most frequent numbers:
   - Always keep the heap size ≤ K by removing the least frequent ones.
3. At the end, the heap contains the top K frequent numbers.
4. Remove all from heap and return them as result.

*****************************************
"""
