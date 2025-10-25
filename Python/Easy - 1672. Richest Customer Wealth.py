from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0

        for i in accounts:
            isum = sum(i)
            if isum > max_wealth:
                max_wealth = isum

        return max_wealth
