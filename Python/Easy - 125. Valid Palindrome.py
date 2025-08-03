class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s) - 1
        l, r = 0, n
        s = s.lower()

        while l <= r:
            if l == r and s[l] == s[r]:
                return True
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if s[l].isalnum() and s[r].isalnum() and (s[l] != s[r]):
                    return False
                elif s[l].isalnum() and not s[r].isalnum():
                    r -= 1
                elif not s[l].isalnum() and s[r].isalnum():
                    l += 1
                else:
                    l += 1
                    r -= 1

        return True