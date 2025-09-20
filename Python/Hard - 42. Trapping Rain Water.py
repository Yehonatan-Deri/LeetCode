class Solution(object):
    # Not efficient run time, always call max/min functions
    # def trap(self, height):
    #     """
    #     :type height: List[int]
    #     :rtype: int
    #     """
    #
    #     res = 0
    #     left = 0
    #     right = len(height) - 1
    #     max_left = height[left]
    #     max_right = height[right]
    #
    #     # the formula to know how much collected is min height of left and right minuse the spot
    #     # min(left-side, right-side) - spot
    #     while (left < right):
    #         # checking which side of max height is smaller so need shifting.
    #         # this act as min(left-side, right-side)
    #         if (max_left < max_right):
    #             res += max(0, min(max_left, max_right) - height[left])
    #             left += 1
    #             max_left = max(max_left, height[left])
    #         else:
    #             res += max(0, min(max_left, max_right) - height[right])
    #             right -= 1
    #             max_right = max(max_right, height[right])
    #
    #     return res


    """
    We start with maxLeft = height[0], maxRight = height[n-1], using 2 pointers left point to the next bar on the left side, right point to the next bar on the right side.
    How to decide to move left or move right?
        - If maxLeft < maxRight, it means the water level is based on the left side (the left bar is smaller) then move left side:
            * If height[left] > maxLeft then there is no trap water, we update maxLeft by maxLeft = height[left].
            * Else if height[left] < maxLeft then it can trap an amount of water, which is maxLeft - height[left].
            *Move left by left += 1
        - Else if maxLeft > maxRight, it means the water level is based on the right side (the right bar is smaller) then move right side:
            * If height[right] > maxRight then there is no trap water, we update maxRight by maxRight = height[right].
            * Else if height[right] < maxRight then it can trap an amount of water, which is maxRight - height[right].
            * Move right by right -= 1.
    """
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        res = 0
        left = 0
        right = len(height) - 1
        max_left = height[left]
        max_right = height[right]

        # the formula to know how much collected is min height of left and right minuse the spot
        # min(left-side, right-side) - spot
        while left <= right:
            # checking which side of max height is smaller so need shifting.
            # this act as min(left-side, right-side)
            if max_left < max_right:
                if height[left] >  max_left:
                    max_left = height[left]
                else:
                    res += max_left - height[left]
                left += 1
            else:
                if height[right] > max_right:
                    max_right = height[right]
                else:
                    res += max_right - height[right]
                right -= 1

        return res


