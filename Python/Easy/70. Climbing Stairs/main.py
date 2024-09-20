class Solution:
    def climbStairs(self, n: int) -> int:
        one_step, two_step = 1, 1

        # dynamic back-programing (with fibonachi algorithm based)
        for i in range(n-1):
            temp = one_step
            one_step = one_step + two_step
            two_step = temp
        return one_step

    # recursive solution
    def climbStairs1(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)