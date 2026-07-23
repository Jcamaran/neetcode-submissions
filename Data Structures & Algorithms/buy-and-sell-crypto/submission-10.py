class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we initilialize a left and right pointer, the left to find a buydate, and right to sell
        if not prices:
            return 0

        l,r = 0,1
        n = len(prices)
        maxP = 0
        

        while r < n:
            if prices[r] <= prices[l]:
                l = r
            else:
                currP = prices[r] - prices[l]
                maxP = max(maxP,currP)
            r += 1
        return maxP
            
        