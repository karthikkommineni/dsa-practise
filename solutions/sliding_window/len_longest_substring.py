class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # end window - no repeating char, maxlen
        l, r = 0, 0
        seen = set()
        max_length = 0

        for r in range(len(s)):
            while s[r] in seen:  # while because - remove till duplicate present
                seen.remove(s[l])
                l += 1
                continue
            seen.add(s[r])
            max_length = max(max_length, r - l + 1)

        return max_length


"""
Goal: Find the length of the longest substring without repeating characters.

Approach: Sliding window with two pointers (l, r) and a set (seen) to track current window chars.

Logic:

Expand r one char at a time.

If s[r] is a duplicate, shrink window by removing s[l] until duplicate is gone (while).

Update max_length as the window grows.

Complexity: Time O(n), Space O(min(n, Σ)).

"""
