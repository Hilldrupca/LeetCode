from math import comb
from collections import Counter
from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for December 8th, 2020.
    '''
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        Given a list of song durations in seconds, returns the number of pairs
        whose duration sum is evenly divisible by sixty.
        
        Constraints:
            1 <= len(time) <= 6 * 10**4
            1 <= time[i] <= 500
            
        Params:
            time - A list of integer song durations in the range [1,500].
            
        Returns:
            int - Number of song pair durations divisible evenly by sixty.
            
        Examples:
            numPairsDivisibleBy60([30,20,150,100,40])   ->   3
            numPairsDivisibleBy60([60,60,60])           ->   3
            numPairsDivisibleBy60([20,40])              ->   1
        '''
        if not time or len(time) < 2:
            return 0
        
        counts = Counter(x % 60 for x in time)
        get = counts.get
        
        # sum of pairs for times % 60 between 1 and 59
        pairs = sum(get(i,0) * get(60-i,0) for i in range(1,30))
            
        # sum pairs, and special cases where times % 60 is 0 and 30
        return pairs + comb(get(0,0),2) + comb(get(30,0),2)
