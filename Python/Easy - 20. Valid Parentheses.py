class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        hm = {'(': ')', '{': '}', '[': ']'}

        for char in s:
            if char in hm:
                stack.append(hm[char])
            elif not stack or char != stack.pop():
                return False

        return not stack