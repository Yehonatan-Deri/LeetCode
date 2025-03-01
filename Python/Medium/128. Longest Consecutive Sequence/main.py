from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_sequence = 0
        # for each number in the set check if it is the start of a sequence
        # if it is, then count the sequence
        # if its i - 1 is in the set it means that it is not the start of a sequence
        # so we can skip it
        # goal is to loop over the set once per sequence

        # O(n) time complexity
        for i in nums_set:
            # if i - 1 is not in the set, then it is a start of a sequence,
            # we can start counting the sequence from i
            if (i -1)  not in nums_set:
                cur_sequence = 1
                # while i + 1 is in the set, we can keep counting the sequence
                while (i + 1) in nums_set:
                    cur_sequence += 1
                    i += 1
                max_sequence = max(max_sequence, cur_sequence)

        return max_sequence

if __name__ == '__main__':
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]))
    print(solution.longestConsecutive([0,3,7,2,5,8,4,6,0,1, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]))