class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hm = {}
        counter = 0

        if len(magazine) < len(ransomNote):
            return False

        for i in magazine:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1

        for i in ransomNote:
            if i not in hm or hm[i] <= 0:
                return False
            if i in hm:
                hm[i] -= 1

        return True

