class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed_x = int(str(x)[::-1])
        return x == reversed_x



if __name__ == '__main__':
    x = -121
    solution = Solution()
    print(solution.isPalindrome(x))