
class Solution:
    def __init__(self):
        self.first_bad_version = 0
        
    def isBadVersion(self, ver: int) -> bool:
        '''
        My attempt at recreating LeetCode provided API
        '''
        return ver >= self.first_bad_version
    
    def firstBadVersion(self, n: int) -> int:
        '''
        Given n number of versions, uses a bisect method to find the first
        version that fails a quality check.
        
        Params:
            n - The most recent version count.
            
        Returns:
            int - The first version that fails. Returns -1 if no bad version.
            
        Examples:
            Given n=5, and the first bad version = 4
            firstBadVersion(5)   ->   4
            
            Given n=100000, and the first bad version = 49867
            firstBadVersion(100000)   ->   49867
        '''
        low = 0
        high = n
        current = n//2
        while current != high and current != low:
            check = self.isBadVersion(current)
            check_plus = self.isBadVersion(current+1)
            if not check and check_plus:
                return current+1
            elif check:
                low, high, current = low, current, (current-low)//2
            elif not check:
                low, high, current = current, high, (current+high)//2
                
        return -1
