from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        Return Pascal's triangle up to numRows.
        '''
        if numRows < 1:
            return []
        
        res = [[1]]
        
        for x in range(1, numRows):
            res.append([1])
            prev = res[x-1]
            for y in range(1, len(prev)):
                res[x].append(prev[y-1] + prev[y])
                
            res[x].append(1)
            
        return res
    
    
        # The following also works
        #res = []
        #for i in range(0, numRows):
            #res.append([])
            #for x in range(0,i+1):
                #res[i].append(factorial(i)//(factorial(x) * factorial(i-x)))
