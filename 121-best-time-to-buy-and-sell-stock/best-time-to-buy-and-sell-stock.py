class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        best=0
        cur=float('inf')

        for price in prices:
            if price<cur:
                cur=price
            elif price-cur>best:
                best=price-cur
        return best
        