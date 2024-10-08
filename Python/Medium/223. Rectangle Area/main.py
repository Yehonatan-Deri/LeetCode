class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        # find the overlap space
        left = max(ax1, bx1)
        right = min(ax2, bx2)
        top = min(ay2, by2)
        bot = max(ay1, by1)

        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        overlap = 0
        # check if overlap space
        if left < right and bot < top:
            overlap = (top - bot) * (right - left)

        return area_a + area_b - overlap
