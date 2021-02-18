from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for October 10th, 2020.
    '''
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
        Returns the minimum number of arrows required to burst all balloons.
        
        Arrows are fired vertically, travel forever in one direction, and only
        horizontal coordinates are considered.
        
        Params:
            points - A list of lists containing the start and end x coordinates
                     of each balloon.
                     
        Returns:
            int - Minimum number of arrows required to pop all balloons.
            
        Examples:
            findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])   ->   2
            findMinArrowShots([[1,2],[3,4],[5,6],[7,8]])      ->   4
            findMinArrowShots([[1,2],[2,3],[3,4],[4,5]])      ->   2
            findMinArrowShots([[2,3],[2,3])                   ->   1        
        '''
        points.sort(key=lambda x: x[1])
        arrows = 0
        end = float('-inf')
        for x in points:
            if x[0] > end:
                arrows += 1
                end = x[1]
                
        return arrows
