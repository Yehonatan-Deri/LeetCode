from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while (l < r):
            for i in range(r - l):
                top = l
                bot = r

                # save top left
                topleft = matrix[top][l + i]

                # replace top-left with bot-left
                matrix[top][l + i] = matrix[bot - i][l]

                # replace bot-left with bot-right
                matrix[bot - i][l] = matrix[bot][r - i]

                # replace bot-right with top-right
                matrix[bot][r - i] = matrix[top + i][r]

                # replace top-right with top-left
                matrix[top + i][r] = topleft

            # move to inner layer
            l = l + 1
            r = r - 1

