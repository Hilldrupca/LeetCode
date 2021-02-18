from typing import List

class Solution:
    '''
    LeetCode Monthly Challenge problem for January 6th, 2021.
    '''
    def findKthPositive(self, arr: List[int], k: int) -> int:
        '''
        Given a list of positive integers sorted in strictly increasing order,
        finds the kth missing positive integer.
        
        Constraints:
            1 <= len(arr) <= 1000
            1 <= arr[i] <= 1000
            1 <= k <= 1000
            arr[i] < arr[j] for 1 <= i < j <= len(arr)
            
        Params:
            arr - A list of positive, distinct integers sorted in strictly
                  increasing order.
        
        Returns:
            int - The kth missing positive integer.
            
        Examples:
            findKthPositive([2,3,4,7,11], 5)   ->   9
            findKthPositive([1,2,3,4], 2)      ->   6
            findKthPositive([4,5,6], 3)        ->   3
        '''
        count = idx = 0
        num = 1
        while count != k and idx < len(arr):
            if arr[idx] == num:
                idx += 1
            else:
                count += 1
                
            num += 1
            
        return num + k - count - 1
