
class Solution:
    '''
    LeetCode Monthly Challenge problem for February 5th, 2021.
    '''
    def simplifyPath(self, path: str) -> str:
        '''
        Given the absolute path to a file or directory in a Unix-style file
        system, returns the canonical path. Multiple consecutive slashes are
        treated as a single slash, and three or more consecutive periods are
        treated as a file or direcctory name.
        
        Constraints:
            - 1 <= len(path) <= 3000
            - path consists of English letters, digits, period ".", slash "/",
              or "_"
            - path is a valid absolute Unix path
            
        Params;
            path - A valid absolute Unix path.
            
        Returns:
            str - The canonical path.
            
        Examples:
            simplifyPath('/home/')           ->   '/home'
            simplifyPath('/../')             ->   '/'
            simplifyPath('/home//foo/')      ->   '/home/foo'
            simplifyPath('/a/./b/../../c')   ->   '/c'
        '''
        res = []
        
        for p in path.split('/'):
            if p == '..':
                if res:
                    res.pop()
                    
            elif p and p != '.':
                res.append(p)
                
        return '/' + '/'.join(res)
