"""
******** TIME & SPACE COMPLEXITY ********

Encode:
- Time:  O(N) → N = total length of all strings
- Space: O(1) auxiliary (excluding output string)

Decode:
- Time:  O(N)
- Space: O(N) for result list

*****************************************

************** GENERAL IDEA **************

The main challenge is to encode and decode a list of strings without losing boundaries.
- Use a special delimiter (`#`) along with each string's length to encode unambiguously.
- While decoding, use the delimiter to extract the length and correctly slice the string.
- This avoids delimiter collision by explicitly storing string lengths.

*****************************************
"""

from typing import List

class Solution:
    class Solution:

        def encode(self, strs: List[str]) -> str:
            # 4#neet4#code4#love3you
            res = ""
            for s in strs:
                res = res + str(len(s)) + "#" + s
            return res

        def decode(self, s: str) -> List[str]:
            res = []
            i = 0

            while i < len(s):
                j = i
                while s[j] != '#':
                    j += 1
                length = int(s[i:j])  # extract number before #
                word = s[j + 1: j + 1 + length]  # extract the word
                res.append(word)
                i = j + 1 + length  # move to the start of next encoded part

            return res

    """
    - just having length - will break when len is 2 digits 
    ex: 4neet4code - if word is more than 10 breaks 
    - hence use delimiter    

    - in decode use while loop as we are jumping in diff steps
    """

"""
************** LOGIC ********************

Encode:
1. For each string, add its length + '#' + string itself.
2. Join all encoded pieces into a single string.

Decode:
1. Start from index `i`, and move `j` to find the next '#'.
2. The number before '#' tells the length of the next word.
3. Slice out the word and move to the next encoded chunk.
4. Repeat until the entire string is processed.

*****************************************
"""
