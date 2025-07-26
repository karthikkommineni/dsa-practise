"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N * K)   → N = # of strings, K = max string length
Space: O(N * K)   → For hash map and result storage

*****************************************

************** GENERAL IDEA **************

To group anagrams:
- Anagrams share the same letter frequency.
- Use a fixed-size (26) frequency array for each word.
- Convert it into a tuple (hashable) and group all words under that key.
- Finally, return grouped lists from the hashmap.

Why use frequency count?
- Sorting takes O(K log K), while frequency takes O(K), which is faster.

*****************************************
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resultMap = defaultdict(list)

        for s in strs:
            count = [0] * 26  # frequency of characters a–z
            for c in s:
                count[ord(c) - ord("a")] += 1
            resultMap[tuple(count)].append(s)

        return list(resultMap.values())

"""
************** LOGIC ********************

1. Build a frequency count (26-length array) for each string.
2. Convert it to a tuple to act as a hashable key.
3. Use a hash map to group strings with the same key.
4. Return the grouped anagram lists.

*****************************************
"""
