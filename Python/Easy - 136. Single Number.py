class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        for num in nums:
            sum ^= num
        return sum