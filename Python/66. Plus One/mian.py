from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        for i in range(l-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


if __name__ == '__main__':
    sol = Solution()
    # print(sol.plusOne([1,2,3]))  # Output: [1,2,4]
    # print(sol.plusOne([4,3,2,1]))  # Output: [4,3,2,2]
    # print(sol.plusOne([0]))  # Output: [1]
    # print(sol.plusOne([9]))  # Output: [1,0]
    print(sol.plusOne([9, 9]))  # Output: [1,0,0]
