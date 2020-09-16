from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Maximum profit if you could only buy and sell one stock once.
        
        Params:
            prices - A list of integers of stock prices.
            
        Returns:
            int - The maximum profit. Returns 0 if money would be lost.
            
        Examples:
            maxProfit([7,1,5,3,6,4])   ->   5
            maxProfit([7,6,4,3,1])     ->   0
            maxProfit([1,2])           ->   1
        '''
        low = float('inf')
        best = 0
        for x in prices:
            best, low = max(best, x - low), min(low, x)
            
        return best
