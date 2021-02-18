from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        Returns the intersetion of two lists. The count of each item in the
        result is equal to the number of times it shows up in both lists.
        
        Result can be in any order.
        
        Params:
            nums1 - list of integers
            nums2 - list of integers
        
        Returns
            list - list of itersecting items between nums1 and nums2
            
        Examples:
            intersect([1,2,2,1], [2,2]) -> [2,2]
            
            intersect([4,9,5], [9,4,9,8,4])
        '''
        
        # one and two are essentially simple collections.Counter objects
        one = {}
        for x in nums1:
            if x not in one:
                one[x] = 0
            one[x] += 1
            
        two = {}
        for y in nums2:
            if y not in two:
                two[y] = 0
            two[y] += 1
        
        # set() of the intersection between the dictionary keys
        shared = one.keys() & two.keys()
        res = []
        
        for s in shared:
            
            # min() is the number of times it appears in both lists
            res += [s] * min(one[s],two[s])
            
        return res
