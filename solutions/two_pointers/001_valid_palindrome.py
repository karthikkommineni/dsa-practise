"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → N = length of string
Space: O(1) → uses constant extra space

*****************************************
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):  # Skip non-alphanumeric characters
                l += 1
            while r > l and not self.alphaNum(s[r]):  # Skip non-alphanumeric characters
                r -= 1

            if s[l].lower() != s[r].lower():          # Compare lowercase versions
                return False

            l, r = l + 1, r - 1

        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))

"""
*************** GENERAL IDEA ***************

Use two pointers to scan from both ends and compare characters
while skipping all non-alphanumeric characters. Check if characters
match when normalized to lowercase.

*******************************************

*************** LOGIC **********************

1. Initialize two pointers: `l = 0` and `r = len(s) - 1`
2. Skip all non-alphanumeric characters from both ends
3. Compare characters at `l` and `r` (case-insensitive)
4. If mismatch, return False; otherwise move inward
5. If entire scan completes, return True (valid palindrome)

*******************************************
--> Reverse the string and compare it to the original
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
"""
