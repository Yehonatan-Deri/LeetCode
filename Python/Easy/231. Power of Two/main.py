class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        if (n < 0):
            n = n * (-1)

        return False if n & 1 == 1 else True


    def isPowerOfTwo1(self, n: int) -> bool:
        # n - check if not zero (0 == false)
        # (n & (n - 1)) - check if power of 2 exmp: n=4  4 & 3 => 100 & 011 => 000 = 0=False !0 = True
        return n and not (n & (n - 1))

