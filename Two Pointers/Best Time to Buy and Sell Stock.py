class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1 #left buying, right selling
        maxP = 0

        while r<len(prices):
            if prices[r] > prices[l]:
                maxP = max(prices[r] - prices[l], maxP)
            else:
                l=r
            r+=1

        return maxP
            