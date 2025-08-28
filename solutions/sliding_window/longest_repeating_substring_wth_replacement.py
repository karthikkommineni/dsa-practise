class Solution:
    def characterReplacement_sol1(self, s: str, k: int) -> int:

        l = 0
        max_len = 0
        count = {}

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            # every substring - calculate len if its valid
            if (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len

    def characterReplacement_optimal(self, s: str, k: int) -> int:

        l = 0
        max_len = 0
        count = {}
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxf = max(maxf, count[s[r]])
            if (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            # every substring - calculate len if its valid
            max_len = max(max_len, r - l + 1)

        return max_len


    def characterReplacement_wrong(self, s: str, k: int) -> int:
        l = 0
        max_len = 0
    
        for r in range(1, len(s)):
            if s[r] != s[l]:
                if k > 0:
                    max_len = max(r - l + 1, max_len)
                    k -= 1
                else:
                    l = r
            else:
                max_len = max(r - l + 1, max_len)

        return max_len


"""
k

"""

"""
set - if substring is distinct
k is like a counter
when seq breaks - do count,max count, update l = r


"""
