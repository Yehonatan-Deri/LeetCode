from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        counter = 0

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            # if we hit '1' switch to '0' for not stepping again
            grid[i][j] = '0'
            # check 1 up
            dfs(i - 1, j)
            # check 1 bot
            dfs(i + 1, j)
            # check 1 left
            dfs(i, j - 1)
            # check 1 right
            dfs(i, j + 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    counter = counter + 1
                    dfs(i, j)

        return counter
