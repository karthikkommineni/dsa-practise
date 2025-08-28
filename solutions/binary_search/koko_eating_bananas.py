import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            mid = (l + r) // 2
            hours = self._get_total_hours(mid, piles)
            if hours <= h:
                res = min(mid, res)  # possible answer, optimize- remove min
                r = mid - 1  # try smaller speed
            else:
                l = mid + 1  # too slow, increase speed

        return res

    def _get_total_hours(self, speed, piles):
        hours = 0
        for pile in piles:
            hour = math.ceil(pile / speed)  # pile/speed - time taken to finish that pile, ceil -rounds it
            hours = hours + hour
        return hours


"""
 - start thinking in brute force - range of elements 1 to max_ele
 - instead of trying for all ele in range use binary serach
 - why max ele
   -to finish all bananas you need atleast as many hours as number of elements in list
   -so no oh hours h > len(piles) , hence max min ele is biggest value in piles
   -binary search with understanding of problem
-math.ceil - rounds to next integer - 0.1 -> 1
- adjusting l = l+1 and r=r-1

 """       