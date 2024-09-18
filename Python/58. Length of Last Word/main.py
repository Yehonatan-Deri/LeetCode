class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        is_word = False
        counter = 0
        i = len(s) - 1

        while i >= 0:
            if s[i] != ' ':
                is_word = True
                counter += 1
            if is_word and s[i] == ' ':
                return counter
            i -= 1

        return counter
