from typing import Lists

class Solution:
    '''
    LeetCode Monthly Challege problem for August 22nd, 2020
    '''
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        
        # total points across all rectangles
        self.total_points = 0
        
        # area associated with each rectangle
        self.rect_points = []
        for x in rects:
            width = abs(x[2] - x[0]) + 1
            height = abs(x[3] - x[1]) + 1
            points = width * height
            self.total_points += points
            self.rect_points.append(self.total_points)
        
    def pick(self) -> List[int]:
        '''
        Given a list of non-overlapping axis-aligned rectangles rects, write a
        function pick which randomly and uniformily picks an integer point in
        the space covered by the rectangles.

        Note:

            - An integer point is a point that has integer coordinates. 
            - A point on the perimeter of a rectangle is included in the space
              covered by the rectangles. 
            - ith rectangle = rects[i] = [x1,y1,x2,y2], where [x1, y1] are the
              integer coordinates of the bottom-left corner, and [x2, y2] are
              the integer coordinates of the top-right corner.
            - length and width of each rectangle does not exceed 2000.
            - 1 <= rects.length <= 100
            - pick return a point as an array of integer coordinates [p_x, p_y]
            - pick is called at most 10000 times.

        Returns:
            list - random [x,y] coordinate from a random rectangle
        '''
        from random import randint
        
        # choose a random point from all points
        point = randint(0,self.total_points)
        
        # find which rectangle that point belongs to
        # rectangles with more area are weighted more
        idx = 0
        for i in range(len(self.rect_points)):
            if self.rect_points[i] >= point:
                idx = i
                break
        
        rect = self.rects[idx]
        
        # return random point within that rectangle
        return [randint(rect[0],rect[2]), randint(rect[1],rect[3])]

 
