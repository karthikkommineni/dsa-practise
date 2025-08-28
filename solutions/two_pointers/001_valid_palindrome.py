"""
******** TIME & SPACE COMPLEXITY ********

Time:  O(N) → N = length of string
Space: O(1) → uses constant extra space

*****************************************
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left, right = 0, len(s) - 1

        while left <= right:

            # edge = spaces - ignore them
            while left < right and not self.is_alpha_numeric(s[left]):
                left += 1
            while left < right and not self.is_alpha_numeric(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower(): return False
            left += 1
            right -= 1

        return True

    def is_alpha_numeric(self, c):
        return ((ord('A') <= ord(c) <= ord('Z')) or
                (ord('a') <= ord(c) <= ord('z')) or
                (ord('0') <= ord(c) <= ord('9')))


"""

*************** LOGIC **********************

1. Logic:
   - Use two-pointer approach: left at start, right at end
   - Skip non-alphanumeric chars using custom is_alpha_numeric()
   - Compare s[left].lower() vs s[right].lower()
   - If mismatch, return False

2. Edge Cases:
   - Empty string → should return True
   - Only special characters → True
   - Single character → True
   - Case-insensitive matching
   - Handles input like "A man, a plan, a canal: Panama"

3. Dry Run:
   Input: "race a car"
   Cleaned: "raceacar" — not a palindrome → returns False

   Input: "A man, a plan, a canal: Panama"
   Cleaned: "amanaplanacanalpanama" → True

Notes 
on why left < right is important:
   - Used in the **main loop** to stop comparison when pointers meet or cross
   - Prevents over-comparing the same character (especially in odd-length strings)
   - Ensures we **don’t compare characters after skipping has moved pointers out of range**
   - In the **skip loops**, it avoids out-of-bounds errors when skipping special characters
   - Helps handle cases like:
     - `"!!!"` → all characters skipped safely
     - `"a"` or `""` → loop never enters, returns True without errors
   - Guarantees every comparison is valid and necessary, and nothing is checked twice


*******************************************
--> Reverse the string and compare it to the original
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


Misc:
-java initialize all data types
- methods
- template:

"""
