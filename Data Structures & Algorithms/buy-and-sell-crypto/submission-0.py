class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret_val = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > ret_val:
                    ret_val = prices[j] - prices[i]
        
        return ret_val

        