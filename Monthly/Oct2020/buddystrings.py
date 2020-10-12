
class Solution:
    '''
    LeetCode Monthly Challenge for October 12th, 2020.
    '''
    def buddyStrings(self, A: str, B: str) -> bool:
        '''
        Returns whether or not two letters in A can be swapped so that it will
        equal B. Does not swap a letter with itself.
        
        Params:
            A - A string of lowercase letters.
            
            B - A string of lowercase letters.
            
        Returns:
            bool - Whether two letters can be swapped in A so it equals B.
            
        Examples:
            buddyStrings('ab','ba')   ->   True
            buddyStrings('ab','ab')   ->   False
            buddyStrings('aa','aa')   ->   True
            buddyStrings('', 'aa')    ->   False
        '''
        if len(A) != len(B):
            return False
        
        # If A == B, check if any letters have duplicates
        if A == B:
            visited = set()
            for a in A:
                if a in visited:
                    return True
                visited.add(a)
                
            return False
        
        else:
            # Check for positional differences
            diff = []
            for i in range(len(A)):            
                if A[i] != B[i]:
                    diff.append([A[i], B[i]])
                    
            # Only one swap allowed, means only two differences will work
            return len(diff) == 2 and diff[0] == diff[1][::-1]
