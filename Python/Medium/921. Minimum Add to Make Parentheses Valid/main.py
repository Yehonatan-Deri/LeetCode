class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        l, r = 0, 0

        for i in s:
            if i == ')' and r == 0:
                l += 1
            else:
                r += 1 if i == '(' else -1

        return l + r