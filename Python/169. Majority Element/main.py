from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        counter = 0
        for i in nums:
            if i == res:
                counter = counter + 1
            else:
                counter = counter - 1
                if counter == 0:
                    counter = counter + 1
                    res = i
        return res
"""
Cleaner code for finding the majority element in a list of integers using Boyer-Moore Voting Algorithm.
The algorithm is based on the fact that if a majority element exists in a list, it will be the final value of the 'res' variable.
The algorithm iterates through the list, maintaining a count of the current majority element.
If the count reaches 0, the current element becomes the new majority element.
This algorithm has a time complexity of O(n) and a space complexity of O(1).
    

    def majorityElement(self, nums: List[int]) -> int:
        res = nums[0]
        counter = 0
        for i in nums:
            if counter == 0:
                res = i
            counter += 1 if i == res else -1
        return res

"""

