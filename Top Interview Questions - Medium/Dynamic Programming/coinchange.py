from typing import List
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Returns the minimum number of coins to make up the desired amount.
        Coins can be of any positive denomination.
        
        To see a history of implementations, see bottom of code.
        
        Params:
            coins - A list of coin denominations.
            
            amount - The desired amount to make.
            
        Returns;
            int - The minimum coins needed to make a certain amount. If that
                  amount cannot be made, returns -1.
                  
        Examples:
            coinChange([1,2,5], 11)   ->   3
            coinChange([2], 3)        ->   -1
            coinChange([1], 0)        ->   0
            coinChange([1], 1)        ->   1
            coinChange([1], 2)        ->   2
        '''
        coins.sort(reverse=True)
        best = float('inf')
        stack = [(0,amount,0)]
        while stack:
            count, rem, idx = stack.pop()
            
            if count + rem//coins[idx] + (rem%coins[idx] != 0) >= best:
                continue
            
            if rem%coins[idx] == 0:
                best = min(best, count + rem//coins[idx])
                continue
            
            if idx == len(coins)-1:
                continue
            
            for c in range(rem//coins[idx] + 1):  
                stack.append((count+c, rem - c*coins[idx], idx+1))
        
        return best if best != float('inf') else -1


'''
Initial implementation. Makes use of a list whose length equals amount + 1.
This list tracks the minimum coins to reach each value until the last element.
This works, however, it's not the most performant.
        
        dp = [float('inf')]*(amount+1)
        for c in coins:
            if c < len(dp):
                dp[c] = 1
                
        for i in range(len(dp)):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
                    
        return dp[amount] if dp[amount] != float('inf') else -1
        

Second implementation. Makes use of a queue to visit possible values. Uses
a set to prevent repeat values. Again, this works and is a bit more performant
than the above approach.

        visited = set()
        bfs = deque([(0,0)])
        while bfs:
            count, total = bfs.popleft()
            
            for c in coins:
                temp = total + c
                
                if temp not in visited:
                    
                    if temp < amount:
                        bfs.append((count+1, temp))
                        visited.add(temp)
                    
                    elif temp == amount:
                        return count + 1
                    
        return -1 if amount else 0


I did not come up with the following recursive approach. However it is the
basis for the remaining approache and the current implementation. Tied with the
current implementation for fastest run time, and memory usage.

        coins.sort(reverse=True)
        self.best = float('inf')
        
        def dfs(count, rem, idx):
            
            if count + rem//coins[idx] + (rem%coins[idx] != 0) >= self.best:
                return
            
            if rem%coins[idx] == 0:
                self.best = min(self.best, count + rem//coins[idx])
                return
            
            if idx == len(coins) - 1:
                return
            
            for c in range(rem//coins[idx],-1,-1):
                dfs(count + c, rem - c*coins[idx], idx + 1)
                
        dfs(0,amount,0)
        return self.best if self.best != float('inf') else -1
        
        
Incorporated the logic from the recursive version into my queue version.
Performance is much better than the original queue version, but still roughly
twice as slow as the recursive method. Changing the queue to a stack results in
equivalent perforamnce to the recursive method.
        
        coins.sort(reverse=True)
        best = float('inf')
        bfs = deque([(0,amount,0)])
        while bfs:
            count, rem, idx = bfs.popleft()
            
            if count + rem//coins[idx] + (rem%coins[idx] != 0) >= best:
                continue
            
            if rem%coins[idx] == 0:
                best = min(best, count + rem//coins[idx])
            
            if idx == len(coins)-1:
                continue
            
            for c in range(rem//coins[idx],-1,-1):  
                bfs.append((count+c, rem - c*coins[idx], idx+1))
        
        return best if best != float('inf') else -1
        
        
        '''
