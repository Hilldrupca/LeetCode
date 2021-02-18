from collections import Counter
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        Finds all unique triplets in nums that sum to zero. Returns an empty
        list if nums is empty or has fewer than three elements.
        
        Examples:
            threeSum([-1,0,1,2,-1,-4])   ->   [[-1,-1,2],[-1,0,1]]
            threeSum([])                 ->   []
            threeSum([0])                ->   []
        '''
        
        counts = Counter(nums)
        
        # Limit none 0 numbers to only 2
        # if -1 + -1 + x, x can never be -1
        # but allow 3 0's
        for x in counts:
            if counts[x] > 2 and x:
                counts[x] = 2
            elif counts[x] > 3:
                counts[x] = 3
        
        # Recreate nums list, will already be sorted
        count_list = []
        for x,y in counts.items():
            count_list.extend([x]*y)
        
        count_list.sort()
        
        # Iterate through some possibilities
        res = []
        for left in range(len(count_list)-2):
            a = count_list[left]
            
            # If a is greater than 0, everything after will be as well
            if a > 0:
                break
                
            mid = left + 1
            right = len(count_list) - 1
            
            # Iterate primarily from left to right
            while mid < right:
                b = count_list[mid]
                c = count_list[right]
                
                # Narrow possibilities by working towards the middle
                if a + b + c == 0:
                    res.append((a,b,c))
                    mid += 1
                    right -= 1
                elif a + b + c < 0:
                    mid += 1
                else:
                    right -= 1
                    
        # Remove duplicate triplets
        return list(set(res))
