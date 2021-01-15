
class Solution:
    '''
    LeetCode Monthly Challenge problem for January 15th, 2021.
    '''
    def getMaximumGenerated(self, n: int) -> int:
        '''
        Given an integer, returns the maximum integer in an array of length
        n + 1 that is generated following these rules:
        
            nums[0] = 0
            nums[1] = 1
            nums[2 * i] = nums[i] when 2 <= 2 * i <= n
            nums[2 * i + 1] = nums[i] + nums[i=1] when 2 <= 2 * i + 1 <= n
            
        Constraints:
            0 <= n <= 100
            
        Params;
            n - An integer length of desired array - 1.
            
        Returns:
            int - The maximum integer in the generated array.
            
        Examples:
            getMaximumGenerated(7)   ->   3
            getMaximumGenerated(3)   ->   2
            getMaximumGenerated(2)   ->   1
        '''
        if not n:
            return 0
        
        arr = [0] * (n + 1)
        arr[1] = high = 1
        
        for idx in range(2, n + 1):
            if not idx % 2:
                arr[idx] = arr[idx // 2]
            else:
                i = (idx - 1) // 2
                arr[idx] = arr[i] + arr[i+1]
                
            high = max(high, arr[idx])
            
        return high
