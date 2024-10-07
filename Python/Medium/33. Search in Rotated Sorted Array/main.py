from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        l = 0
        r = n

        # find where is the minimum 
        while l < r:
            m = (l + r) // 2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        m = l

        # normal binary search
        if m == 0:
            l = 0
            r = n
        # if target from 0 to m-1
        elif target >= nums[0] and target <= nums[m - 1]:
            l = 0
            r = m - 1
        # if target is from m to n-1
        else:
            l = m
            r = n

        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m - 1

        return -1

