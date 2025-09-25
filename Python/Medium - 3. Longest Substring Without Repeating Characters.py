class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = 0
        l, r = 0, 0
        map = {}

        for r, c in enumerate(s):
            if c in map:
                l = max(l, map[c])

            max_length = max(max_length, r - l + 1)
            map[c] = r + 1
        return max_length