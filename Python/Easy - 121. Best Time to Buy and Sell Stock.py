class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best_val = 0
        min_price = float("inf")

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > best_val:
                best_val = price - min_price

        return best_val
