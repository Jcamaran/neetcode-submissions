class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Left checks for buy and right checks for sale
        left, right = 0,1

        maxp = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxp = max(maxp,profit)
            else:
                # we set the left pointer to right after we find right val less than left to get a new buy position 
                
                left = right
            right += 1
            
        return maxp


