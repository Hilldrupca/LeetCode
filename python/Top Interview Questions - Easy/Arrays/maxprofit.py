from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Given an array of stock prices, find the maximum profit
        when alternating between buying and selling.
        
        Params:
            prices - list of stock prices
            
        Returns:
            itn - maximum profit if stocks are bought at lows,
                  and sold at highs
                  
        Examples:
            maxProfit([7,1,5,3,6,2]) returns 7
            
            maxProfit([1,2,3,4,5]) returns 4
            
            maxProfit([7,6,4,3,1]) returns 0
        '''
        if len(prices) == 1:
            return 0
        
        profit = 0
        buy = True
        for x in range(len(prices) - 1):
            
            # If able to buy stock, buy if next time step price is larger
            if buy and prices[x] < prices[x+1]:
                profit -= prices[x]
                buy = False
            
            # If stock has been bought, sell if next time step price is lower
            if not buy and prices[x] > prices[x+1]:
                profit += prices[x]
                buy = True
                
        # If price only increased since we last bought stock,
        # sell at the last price
        if not buy:
            profit += prices[-1]
            
        return profit
