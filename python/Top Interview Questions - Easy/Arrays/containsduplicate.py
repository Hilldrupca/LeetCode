from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int], speed='consist') -> bool:
        '''
        Find if a list contains duplicates. 
        
        Note: This implementation requires that the list
              only contain hashable types.
        
        Params:
            nums - list of integers
            
            (custom)
            speed - choose between consistent time complexity or possibly O(1).
                    If going with 'lucky', note the worst case may be slower than
                    'consist'.
                    
                    default: 'consist'
                    options: 'consist' or 'lucky'
            
        Returns:
            boolean - whether or not nums contains duplicates
            
        Examples:
            containsDuplicate([1,2,3,1]) -> True
            
            containsDuplicate([1,2,3,4]) -> False
            
            containsDuplicate([1,1,1,3,3,4,3,2,4,2]) -> True
        '''
        
        if speed not in ['lucky','consist']:
            speed = 'consist'
        
        if speed == 'lucky':
            num_set = set()
            
            for x in nums:
                if x in num_set:
                    return True
                
                num_set.add(x)
                
            return False
        
        if speed == 'consist':
            
            num_set = set(nums)
            return not len(num_set) == len(nums)
