from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for November 30th, 2020.
    '''
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        '''
        Given a set of building geometric information, returns the key points
        of the skyline. A key point is the left endpoint of a horizontal line
        segment. This function uses a merge sort approach.
        
        NOTE: I required external resources to solve this challenge.
        
        Params:
            buildings - Building geometry information. Each building should be
                        of form [x1,x2,h]. Where x1 is the left x coordinate,
                        x2 is the right x coordinate, and h is the building
                        height.
            
        Returns:
            List[List[int]] - The key points of the skyline. Each key point is
                              the left x coordinate of a horizontal line, and
                              its height. A horizontal line ends at the start
                              of the next key point.
                              
        Examples:
            getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) -> 
                        [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
                        
            getSkyline([[1,2,1],[1,2,2],[1,2,3]])   ->   [[1,3],[2,0]]
        '''
        if not buildings:
            return []
        
        def merge_sort(start, end):
            if end - start == 1:
                b = buildings[start]
                return [[b[0],b[2]],[b[1],0]]
            
            return merge(merge_sort(start, (start+end)//2),
                         merge_sort((start+end)//2, end))
            
        def merge(s1, s2):
            h1 = h2 = i = j = 0
            points = []
            
            while i < len(s1) and j < len(s2):
                if s1[i][0] < s2[j][0]:
                    h1 = s1[i][1]
                    next_point = [s1[i][0], max(h1,h2)]
                    i += 1
                elif s1[i][0] > s2[j][0]:
                    h2 = s2[j][1]
                    next_point = [s2[j][0], max(h1,h2)]
                    j += 1
                elif s1[i] == s2[j]:
                    next_point = s1[i]
                    h1 = h2 = max(h1, h2, s1[i][1])
                    i, j = i + 1, j + 1
                else:
                    h1, h2 = s1[i][1], s2[j][1]
                    next_point = [s1[i][0], max(h1,h2)]
                    i, j = i + 1, j + 1
                    
                if points and points[-1][1] == next_point[1]:
                    continue
                points.append(next_point)
            
            return points + s1[i:] + s2[j:]
        
        return merge_sort(0,len(buildings))
