
class Solution:
    '''
    LeetCode Monthly Challenge problem for October 26th, 2020.
    '''
    def champagneTower(self, poured: int, query_row: int,
                       query_glass: int) -> float:
        '''
        Returns how full the jth (query_glass) cup is on the ith (query_row)
        row.
        
        We stack glasses in a pyramid, where the first row has 1 glass, the
        second row has 2 glasses, and so on until the 100th row.  Each glass
        holds one cup (250ml) of champagne.

        Then, some champagne is poured in the first glass at the top.  When the
        topmost glass is full, any excess liquid poured will fall equally to
        the glass immediately to the left and right of it.  When those glasses
        become full, any excess champagne will fall equally to the left and
        right of those glasses, and so on.  (A glass at the bottom row has its
        excess champagne fall on the floor.)

        For example, after one cup of champagne is poured, the top most glass
        is full.  After two cups of champagne are poured, the two glasses on
        the second row are half full.  After three cups of champagne are
        poured, those two cups become full - there are 3 full glasses total
        now.  After four cups of champagne are poured, the third row has the
        middle glass half full, and the two outside glasses are a quarter full,
        as pictured below.
        
        Params:
            poured - (integer) Number of champagne cups poured.
            
            query_row - The row of interest.
            
            query_glass - The glass of interest within the query_row.
            
        Returns:
            float - How full the jth glass is in the ith row.
            
        Examples:
            champagneTower(1,1,1)               ->   0.000
            champagneTower(2,1,1)               ->   0.500
            champagneTower(100000009, 33, 17)   ->   1.000
        '''
        if poured <= 0:
            return 0
        
        prev = [poured]
        row = 0
        while row < query_row:
            
            next_row = [0] * (len(prev) + 1)
            
            for i in range(len(prev)):
                if prev[i] > 1:
                    excess = (prev[i]-1)/2
                    next_row[i] += excess
                    next_row[i+1] += excess
            
            row += 1
            prev = next_row
            
        return min(1, prev[query_glass])
