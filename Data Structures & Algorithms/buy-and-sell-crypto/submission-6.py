class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # the idea for the sliding window is that we have a left pointer looking for a buy day and a right pointer looking for a sell day

        left = profit =maxP = 0

        for right in range(len(prices)):
            if prices[left] > prices[right]:
                left = right
                
            else:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
        return maxP

            


        