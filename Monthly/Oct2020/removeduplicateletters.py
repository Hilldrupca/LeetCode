
class Solution:
    '''
    LeetCode Monthly Challenge for October 11th, 2020.
    '''
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        Removes duplicate letters, and returns remaining letters in smallest
        lexicographical order. No distinction is made between upper and 
        lowercase letters.
        
        Params:
            s - A string of letters.
            
        Returns:
            str - Remaining letters in smallest lexicographical order.
            
        Examples:
            removeDuplicateLetters('bcabc')      ->   'abc'
            removeDuplicateLetters('cbacdcbc')   ->   'acdb'
        '''
        # Count letter occurences
        counts = {}
        for l in s:
            counts[l] = counts.get(l, 0) + 1
            
        
        stack = []
        visited = set()
        for l in s:
            
            # Visit each letter and add to stack if not already visited.
            if l not in visited:
                
                # Remove letters at the top of the stack while they are greater
                # than the current letter, and we haven't seen the last one
                while stack and l < stack[-1] and counts[stack[-1]]:
                    visited.remove(stack.pop())
                    
                stack.append(l)
                visited.add(l)
                
            counts[l] -= 1
        
        return ''.join(stack)
