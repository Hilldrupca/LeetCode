from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 21st, 2020.
    '''
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        '''
        Returns the state of asteroids after all collisions.
        
        - All asteroids are moving at the same speed.
        - Values in asteroids are the sizes of each asteroid.
        - The integer sign indicates which direction that asteroid is moving.
          Negative moves left, positive moves right.
        - If two asteroids collide, the smaller explodes. If they are the same
          size, both explode.
          
        Params:
            asteroids - A list of integers representing the size of each
                        asteroid, and which direction it is travelling.
                        (negative left, positive right)
                        
        Returns:
            List[int] - The state of asteroids after all collisions have been
                        processed.
                        
        Examples:
            asteroidCollision([5,10,-5])     ->   [5,10]
            asteroidColliison([8,-8])        ->   []
            asteroidCollision([10,2,-5])     ->   [10]
            asteroidCollision([-2,-1,1,2])   ->   [-2,-1,1,2]
        
        '''
        stack = []
        for x in asteroids:
            if x < 0:
                while stack and 0 < stack[-1] < -x:
                    stack.pop()
                
                if stack and stack[-1] == -x:
                    stack.pop()
                elif stack and stack[-1] < 0 or not stack:
                    stack.append(x)
                
            else:
                stack.append(x)
            
        return stack
