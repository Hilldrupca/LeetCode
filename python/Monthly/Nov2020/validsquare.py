from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 11th, 2020.
    '''
    def validSquare(self, p1: List[int], p2: List[int],
                    p3: List[int], p4: List[int]) -> bool:
        '''
        Returns whether the four given points could construct a square.
        
        Params:
            p1,p2,p3,p4 - A list of integers of the form [int, int].
            
        Returns:
            bool - If a sqaure can be made from the four points.
            
        Examples:
            validSquare([[0,0],[1,1],[1,0],[0,1]])     ->   True
            validSquare([[-1,0],[1,0],[0,1],[0,-1]])   ->   True
            validSquare([[0,0],[1,1],[1,0],[1,1]])     ->   False
            validSquare([[0,0],[5,0],[5,4],[0,4]])     ->   False
            validSquare([0,0],[0,0],[0,0],[0,0]])      ->   False
        '''
        coords = sorted([p1, p2, p3, p4])
        unique = set()
        for x in coords:
            if not x:
                return False # empty coordinate
            unique.add(tuple(x))
            
        if len(unique) < 4:
            return False # four unique points needed to make square
        
        # First parallel sides
        a1 = ((coords[2][0] - coords[0][0])**2 + (coords[2][1] - coords[0][1])**2)**.5
        a2 = ((coords[3][0] - coords[1][0])**2 + (coords[3][1] - coords[1][1])**2)**.5
        
        # Second parallel sides
        b1 = ((coords[1][0] - coords[0][0])**2 + (coords[1][1] - coords[0][1])**2)**.5
        b2 = ((coords[3][0] - coords[2][0])**2 + (coords[3][1] - coords[2][1])**2)**.5
        
        # Diagonols
        c1 = ((coords[3][0] - coords[0][0])**2 + (coords[3][1] - coords[0][1])**2)**.5
        c2 = ((coords[2][0] - coords[1][0])**2 + (coords[2][1] - coords[1][1])**2)**.5
        
        return a1 == a2 == b1 == b2 and c1 == c2
