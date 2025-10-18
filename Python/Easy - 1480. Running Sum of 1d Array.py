class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum = 0
        n = len(nums)
        for i in range(n):
            saved = nums[i]
            nums[i] = nums[i] + sum
            sum += saved

        return nums