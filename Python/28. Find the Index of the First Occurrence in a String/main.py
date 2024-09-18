class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i, j,  = 0, 0
        for i in range(len(haystack) - len(needle) + 1):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle) - 1:
                    return i
        return -1


if __name__ == '__main__':
    sol = Solution()
    # print(sol.strStr("hello", "ll"))  # 2
    # print(sol.strStr("aaaaa", "bba"))  # -1
    # print(sol.strStr("", ""))  # 0
    # print(sol.strStr("a", "a"))  # 0
    # print(sol.strStr("mississippi", "issip"))  # 4
    print(sol.strStr("leetcode", "leeto"))  # -1