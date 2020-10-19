from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 18th, 2020.
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        '''
        Returns the maximum profit when making k transactions. Buying and then
        selling is considered one transaction. Must sell stock before buying
        again.
        
        ### NOTE: Most of this code comes from geeksforgeeks. The only
        changes I made are what to do when k is larger than a half the length
        of prices, and changing the space complexity from O(kn) to O(n).
        
        Params;
            prices - A list of integers. Each value represents the price of stock
                     at that time.
                     
            k - Number of transactions allowed.
            
        Returns:
            int - The maximum profit possible.
            
        Exaples:
            maxProfit([2,4,1], 2)         ->   2
            maxProfit([3,2,6,5,0,3], 2)   ->   7
        '''
        n = len(prices)
        
        if k//2 >= n:
            res = 0
            for i in range(1, n):
                res += max(0, prices[i] - prices[i-1])
                
            return res
        else:
            prev = [0 for _ in range(n+1)]
            for i in range(1, k + 1):
                current = [0 for _ in range(n+1)]
                prevDiff = float('-inf') 
                for j in range(1, n):  
                    prevDiff = max(prevDiff, prev[j-1] - prices[j - 1])  
                    current[j] = max(current[j-1], prices[j] + prevDiff)  

                prev = current

            return prev[n - 1]  
