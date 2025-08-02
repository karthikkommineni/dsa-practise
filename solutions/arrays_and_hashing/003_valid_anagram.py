class Solution:
    def isAnagram_sorting(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return sorted(s) == sorted(t)
        #sorted() returns a new sorted list and can be used for comparison
        # .sort() sorts a list in-place and returns None.


    def isAnagram_hashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)   # in java it countS.getOrDefault(s[i], 0) + 1
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT   # compares all keys and values - in java sm.equals(tm)



    def isAnagram_arr(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True

    """
 -> 🔤 ord() stands for ordinal.
 -> Returns the Unicode code point (i.e., integer) of a given character.
 -> Opposite of chr(), which converts an integer to its corresponding character.
 -> Commonly used to map characters to array indices (e.g., 'a' → 0 using ord(ch) - ord('a')).
 -> Only works on a single character.
 """