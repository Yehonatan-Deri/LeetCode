class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0
        r = len(height) - 1

        while l < r:
            curr_area = min(height[l], height[r]) * (r - l)

            if curr_area > res:
                res = curr_area

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return res

if __name__ == '__main__':
    sol = Solution()
