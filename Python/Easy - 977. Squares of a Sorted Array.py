class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        l, r = 0, n - 1
        res = [0] * n

        for i in range(n - 1, -1, -1):
            if abs(nums[l]) > abs(nums[r]):
                res[i] = nums[l] ** 2
                l += 1
            else:
                res[i] = nums[r] ** 2
                r -= 1

        return res
