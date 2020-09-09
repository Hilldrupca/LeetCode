
class Solution:
    '''
    LeetCode Monthly Challenge problem for September 9th, 2020.
    '''
    def compareVersion(self, version1: str, version2: str) -> int:
        '''
        Compares two version numbers. Leading zeroes at each revision level
        are ignored, ('1.01' == '1.001').
        
        Params:
            version1 - first version to compare.
            
            version2 - second version to compare.
            
        Returns:
            int - 1 if version1 > version2,
                  -1 if version1 < version2,
                  0 if version1 = version2.
                  
        Examples:
            compareVersion('0.1', '1.1')         ->   -1
            comvareVersion('1.0.1', '1')         ->   1
            compareVersion('7.5.2.4', '7.5.3')   ->   -1
            compareVersion('1.01', '1.001')      ->   0
            compareVersion('1.0', '1.0.0')       ->   0
            compareVersion('01', '1')            ->   0
        '''
        
        v1_split = version1.split('.')
        v2_split = version2.split('.')
        
        # add zeroes if lengths are't equal
        v1_split.extend([0]*(len(v2_split) - len(v1_split)))
        v2_split.extend([0]*(len(v1_split) - len(v2_split)))
        
        for ver1, ver2 in zip(v1_split, v2_split):
            ver1 = int(ver1)
            ver2 = int(ver2)
            
            if ver1 < ver2:
                return -1
            
            if ver1 > ver2:
                return 1
            
        return 0
