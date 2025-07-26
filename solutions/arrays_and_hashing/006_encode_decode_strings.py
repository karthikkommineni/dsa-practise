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

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:  # 'neet'
            res = res + str(len(s)) + '#' + s
        return res

    # Encoded example: '4#neet5#codes'
    def decode(self, s: str) -> List[str]:
        # 2 pointers - i, j
        i, res = 0, []
        while i < len(s):
            j = i
            while j < len(s):
                if s[j] != '#':
                    j += 1
                else:
                    length = int(s[i:j])
                    word = s[j+1 : j+1+length]
                    res.append(word)
                    i = j + 1 + length
                    break
        return res

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
