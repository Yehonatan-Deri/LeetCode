class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # XOR act as canceler and can be rearranged in any
        # for example: s = "abcd", t = "abcde" will be loaded to a string: new string: abcdabcde
        # can be arranged as: aabbccdde when between each we can do XOR.
        # or we take counter c and load the XOR operation on each letter we will be left with the added letter

        # A^0 = A

        c = 0

        for char in s:
            c ^= ord(char)
        for char in t:
            c ^= ord(char)

        return chr(c)