from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 24th, 2020.
    '''
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        '''
        Return the largest possible score you can achieve after playing any
        number of tokens.
        
        You have an initial power of P, an initial score of 0, and a bag of
        tokens where tokens[i] is the value of the ith token (0-indexed).

        Your goal is to maximize your total score by potentially playing each
        token in one of two ways:

        - If your current power is at least tokens[i], you may play the ith
          token face up, losing tokens[i] power and gaining 1 score.
        - If your current score is at least 1, you may play the ith token face
          down, gaining tokens[i] power and losing 1 score.

        Each token may be played at most once and in any order. You do not have
        to play all the tokens.
        
        Params:
            tokens - A list of integers. Each element is the token value.
            
            P - The Acts as a currency for playing tokens.
            
        Returns:
            int - The maximum score possible after playing the most tokens.
            
        Examples:
            bagOfTokensScore([100], 50)                ->   0
            bagOfTokensScore([100,200], 150)           ->   1
            bagOfTokensScore([100,200,300,400], 200)   ->   2
            bagOfTokensScore([81,91,31], 73)           ->   1
            bagOfTokensScore([[71,55,82], 54)          ->   0
        '''
        if not tokens or not P:
            return 0
        
        tokens.sort()
        res = low = best = 0
        high = len(tokens) - 1
        while low <= high:
            if P >= tokens[low]:
                P -= tokens[low]
                low += 1
                res += 1
            elif res:
                P += tokens[high]
                res -= 1
                high -= 1
            else:
                break
            
            best = max(best, res)
            
        return best
