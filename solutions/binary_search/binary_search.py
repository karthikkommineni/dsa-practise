from typing import List



def search(self, nums: List[int], target: int) -> int:
    l ,r = 0, len(nums ) -1
    while l <= r:
        mid = l+ ((r - l) // 2)
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            l = mid + 1
        else:
            r = mid - 1

    return -1

